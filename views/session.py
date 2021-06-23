"""
// ---------------------------------------------------------------------------
//
//	Security Advising Modules (SAM) for Cloud IoT and Mobile Ecosystem
//
//  Copyright (C) 2020 Instituto de Telecomunicações (www.it.pt)
//  Copyright (C) 2020 Universidade da Beira Interior (www.ubi.pt)
//
//  This program is free software: you can redistribute it and/or modify
//  it under the terms of the GNU General Public License as published by
//  the Free Software Foundation, either version 3 of the License, or
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful,
//  but WITHOUT ANY WARRANTY; without even the implied warranty of
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//  GNU General Public License for more details.
//
//  You should have received a copy of the GNU General Public License
//  along with this program.  If not, see <http://www.gnu.org/licenses/>.
// 
//  This work was performed under the scope of Project SECURIoTESIGN with funding 
//  from FCT/COMPETE/FEDER (Projects with reference numbers UID/EEA/50008/2013 and 
//  POCI-01-0145-FEDER-030657) 
// ---------------------------------------------------------------------------
"""
import shutil
from api import app, mysql
from flask import request
import json, os
import modules.error_handlers, modules.utils # SAM's modules
import views.user, views.module, views.dependency # SAM's views

"""
[Summary]: Adds a new session to a user.
[Returns]: Response result.
"""
@app.route('/api/session', methods=['POST'])
def add_session():
    DEBUG = False
    if request.method != 'POST': return
    data = {}

    # 1. Check if the user has permissions to access this resource.
    views.user.isAuthenticated(request)

    # 2. Let's get our shiny new JSON object
    #    Always start by validating the structure of the json, if not valid send an invalid response.
    try:
        obj = request.json
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 
    
    # 3. Let's validate the data of our JSON object with a custom function.
    if (not modules.utils.valid_json(obj, {"email", "module_id"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)

    # 4. Before starting a new session, let's just check if there are any dependencies. That is if the user needs to answer questions from any other module before the current one.
    module_dependencies = views.module.find_module(obj['module_id'], True)[0]['dependencies']
    
    if (DEBUG): modules.utils.console_log("['POST']/api/session", "List of dependencies for module " + str(obj['module_id']) + "=" + str(module_dependencies))
    if (len(module_dependencies) != 0):
        # 4.1. Let's iterate the list of dependencies and check if the user answered the questions to that module (i.e., a closed session exists)
        for module_dependency in module_dependencies:
            dep_module_id = module_dependency['module']['id']
            user_id = views.user.find_user(obj['email'], True)['id']

            # 4.2. Let's get the sesions of the current user for the dependency
            user_sessions = count_sessions_of_user_module(dep_module_id, user_id)
            if (user_sessions == 0):
                data = {}
                data['message']      = "A session was not created, the module dependencies are not fulfilled, the module is dependent on one or more modules."
                data['dependencies'] = module_dependencies
                return (modules.utils.build_response_json(request.path, 404, data))


    # 5. Check if there is an identical session closed, 
    #    if true, notify the user on the return response object that a new session will be created; otherwise, 
    #    delete all that of the previously opened session.
    destroySessionID = -1
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, ended FROM Session WHERE userID=(SELECT ID FROM User WHERE email=%s) AND moduleID=%s ORDER BY ID DESC LIMIT 1", (obj['email'], obj['module_id']))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)

    if (len(res) != 0):
        for row in res:
            if (row[1] == 1):
                data['message'] = "A session for this module was previously created and closed, a new one will be created."
            else:
                destroySessionID = int(row[0])
                data['message'] = "A session for this module was previously created, but it is still open. The session will be deleted and recreated."
    cursor.close()

    if (destroySessionID != -1):
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("DELETE FROM Session WHERE ID=%s", destroySessionID)
            conn.commit()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
        finally:
            cursor.close()

    
    # 6. Connect to the database and add a new session.
    try:
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO Session (userID, moduleID) VALUES ((SELECT ID FROM User WHERE email=%s), %s)", (obj['email'],obj['module_id']))
        data['id'] = conn.insert_id()
        conn.commit()

    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    data['module'] = views.module.find_module(obj['module_id'], True)

    # 7. The request was a success, the user 'took the blue pill'.
    return (modules.utils.build_response_json(request.path, 200, data))

"""
[Summary]: Updates the session with the set of answers given and the corresponding questions.
[Returns]: Response result.
"""
@app.route('/api/session/<ID>', methods=['PUT'])
def update_session(ID):
    if request.method != 'PUT': return
    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get our shiny new JSON object.
    # - Always start by validating the structure of the json, if not valid send an invalid response.
    try:
        obj = request.json
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 
    
    # print(obj)
    answer_user_inputted = False
    # 3. Let's validate the data of our JSON object with a custom function.
    if (not modules.utils.valid_json(obj, {"question_id","answer_id"})):
        if (modules.utils.valid_json(obj, {"question_id","input"})): 
            answer_user_inputted = True
        else:
            raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)

    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        if (not answer_user_inputted):
            cursor.execute("INSERT INTO Session_User_Answer (sessionID, questionAnswerID) VALUES (%s, (SELECT ID FROM Question_Answer WHERE questionID=%s AND answerID=%s))", (ID, obj['question_id'], obj['answer_id']))
        else:
            cursor.execute("INSERT INTO Session_User_Answer (sessionID, questionID, input) VALUES (%s, %s, %s)", (ID, obj['question_id'], obj['input']))
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 5. The Update request was a success, the user 'is in the rabbit hole'
    return (modules.utils.build_response_json(request.path, 200))


"""
[Summary]: Get sessions (opened and closed)
[Returns]: Returns response result.
"""
@app.route('/api/sessions', methods=['GET'])
def get_sessions():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's existing sessions from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, userID, moduleID, ended, createdOn, updatedOn FROM Session")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.1. Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']          = row[0]
            data['user_id']     = row[1]
            data['module_id']   = row[2]
            data['ended']       = row[3]
            data['createdOn']   = row[4]
            data['updatedOn']   = row[5]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you'.
        return(modules.utils.build_response_json(request.path, 200, datas))    

"""
[Summary]: Ends a user's session.
[Returns]: Response result.
"""
@app.route('/api/session/<ID>/end', methods=['PUT'])
def end_session(ID):
    if request.method != 'PUT': return

    # 1. Check if the user has permissions to access this resource.
    views.user.isAuthenticated(request)

    # 2. End a session by defining the flag ended to one.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("UPDATE Session SET ended=1 WHERE ID=%s", ID) 
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()
        # 3. The request was a success, let's generate the recommendations.
        return find_recommendations(request, ID)

"""
[Summary]: Gets a session that was previsouly closed. A session is considered closed when all answers were given by the end user.
[Returns]: Response result.
"""
@app.route('/api/session/<ID>/closed', methods=['GET'])
def find_session_closed(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return
    
    # 0. Check if the user has permissions to access this resource.
    if (not internal_call): views.user.isAuthenticated(request)

    # 1. Let's get the data of the session that has ended.
    print("getting data of the session that has ended.") 
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT session_ID, session_userID, session_moduleID, session_ended, session_createdOn, session_updatedOn, question_ID, question, answer_input, module_logic, answer_id, answer FROM View_Session_Answers WHERE session_ID=%s AND session_ended=1 ORDER BY question_ID", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2. Check for empty results.
    print("Checking emoty results")
    if (len(res) == 0):
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, userID, moduleID, ended, createdOn, updatedOn FROM Session WHERE ID = %s" , ID)
        res = cursor.fetchall()
        data = {}
        # 3. Let's get the info about the session.
        for row in res:
            data['id']           = row[0]
            data['user_id']       = row[1]
            data['module_id']     = row[2]
            # data['module_logic'] = row[9] 
            data['ended']        = row[3]
            data['createdOn']    = row[4]
            data['updatedOn']    = row[5]
            break

        try:
            cursor  = conn.cursor()
            cursor.execute("SELECT recommendation_id, recommendation, recommendation_description, recommendation_guide  FROM View_Session_Recommendation WHERE session_id=%s", ID)
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)

        if (len(res) != 0):
            recommendations = []
            for row in res:
                recommendation = {}
                recommendation['id']                  = row[0]
                recommendation['content']             = row[1]
                recommendation['description']         = row[2]
                recommendation['recommendation_guide'] = row[3]
                recommendations.append(recommendation)
            data.update({"recommendations": recommendations})
        conn.close()
        cursor.close()

        if (internal_call):
            return(data)
        else:
            return(modules.utils.build_response_json(request.path, 400))
    else:
        data = {}
        previous_question_id = 0 # To support multiple choice questions
        # 3. Let's get the info about the session.
        for row in res:
            data['id']           = row[0]
            data['user_id']       = row[1]
            data['module_id']     = row[2]
            # data['module_logic'] = row[9] 
            data['ended']        = row[3]
            data['createdOn']    = row[4]
            data['updatedOn']    = row[5]
            break
        # 4. Let's get the questions and inputted answers.
        questions = []
        for row in res:
            question = {}
            if previous_question_id == 0 or previous_question_id != row[6]:
                previous_question_id = row[6]
            else:
                continue
            question['id']           = row[6]
            question['content']      = row[7]

            answers = [] # Empty array of answers
            for row in res:
                if row[6] != question['id']:
                    continue
                # Let's check if the answer was user inputted, or selected from the database.
                if (row[8] != None):
                    answers.append({ "ID": -1, "content": row[8]})
                else:
                    answers.append({ "ID": row[10], "content": row[11]})
            
            question['answer'] = answers
            questions.append(question)
        data.update({"questions":  questions})
    cursor.close()
    
    # 5. Let's now get the recommendations, if any, stored for this session
    print("Getting recomendations stored")
    try:
        cursor  = conn.cursor()
        cursor.execute("SELECT recommendation_id, recommendation, recommendation_description, recommendation_guide  FROM View_Session_Recommendation WHERE session_id=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)

    if (len(res) != 0):
        recommendations = []
        for row in res:
            recommendation = {}
            recommendation['id']                  = row[0]
            recommendation['content']             = row[1]
            recommendation['description']         = row[2]
            recommendation['recommendation_guide'] = row[3]
            recommendations.append(recommendation)
        data.update({"recommendations": recommendations})
    conn.close()
    cursor.close()

    if (internal_call): 
        return(data) 
    else: 
        return(modules.utils.build_response_json(request.path, 200, data))


"""
[Summary]: Gets closed sessions. A session is considered closed when all answers were given by the end user.
[Returns]: Response result.
"""
@app.route('/api/sessions/closed', methods=['GET'])
def get_sessions_closed(internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return
    
    # Check if the user has permissions to access this resource.
    if (not internal_call): views.user.isAuthenticated(request)

    # Let's get the list of sessions from the db.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT id FROM Session WHERE ended =1")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (internal_call):
            return(None)
        else:
            return(modules.utils.build_response_json(request.path, 400))

    sessions = []
    for row in res:
        session = find_session_closed(row[0], True)
        if (session): sessions.append(session)
    cursor.close()
    conn.close()

    # 'May the Force be with you'.
    if (internal_call): 
        return(sessions) 
    else: 
        return(modules.utils.build_response_json(request.path, 200, sessions))


"""
[Summary]: Finds a session by ID (opened or closed)
[Returns]: Returns response result.
"""
@app.route('/api/session/<ID>', methods=['GET'])
def find_session(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # 2. Let's existing sessions from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, userID, moduleID, ended, createdOn, updatedOn FROM Session WHERE ID=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.1. Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)
    else:
        # 2.2. Check if the session requested was ended.
        if (res[0][3] == 1):
            cursor.close()
            conn.close()
            datas = find_session_closed(ID, True)
            if (datas == None):
                if (not internal_call):
                    return(modules.utils.build_response_json(request.path, 404))
                else: 
                    return(None)
            else:
                if (not internal_call):
                    return(modules.utils.build_response_json(request.path, 200, datas)) 
                else:
                    return(datas)
        
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']          = row[0]
            data['user_id']     = row[1]
            data['module_id']   = row[2]
            data['ended']       = row[3]
            data['createdOn']   = row[4]
            data['updatedOn']   = row[5]
            datas.append(data)
        cursor.close()
        conn.close()

        # 3. 'May the Force be with you'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))    
        else:
            return(datas)

"""
[Summary]: Finds sessions by user email (opened or closed)
[Returns]: Returns response result.
"""
@app.route('/api/sessions/user/<user_email>', methods=['GET'])
def find_sessions_of_user(user_email, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    if (not internal_call): 
        views.user.isAuthenticated(request)

    # Let's existing sessions from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT session_id, user_id, user_email, moduleID, ended, createdon, updatedon FROM View_User_Sessions WHERE user_email=%s", user_email)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']          = row[0]
            data['user_id']     = row[1]
            data['user_email']  = row[2]
            data['ended']       = row[4]
            data['createdOn']   = row[5]
            data['updatedOn']   = row[6]
            session         = find_session_closed(data['id'], True)
            if session:
                if ("questions" in session): 
                    questions               = session['questions']
                    data['questions']       = questions
                if ("recommendations" in session):
                    recommendations         = session['recommendations']
                    data['recommendations'] = recommendations
            module = views.module.find_module(row[3], True)
            del module[0]['recommendations']
            del module[0]['tree']
            if (module): data['module'] = module[0]
            datas.append(data)
        cursor.close()
        conn.close()
        
        # 'May the Force be with you'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))
        else:
            return(datas)

"""
[Summary]: Finds sessions by module ID and user email (closed)
[Returns]: Returns response result.
"""
@app.route('/api/sessions/module/<module_id>/user/<user_id>', methods=['GET'])
def find_sessions_of_user_module(module_id, user_id, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    if (not internal_call): 
        views.user.isAuthenticated(request)

    # Let's existing sessions from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT session_id, user_id, user_email, moduleID, ended, createdon, updatedon FROM View_User_Sessions WHERE moduleID=%s AND user_id=%s AND ended=1 ORDER BY session_id DESC", (module_id, user_id))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']          = row[0]
            data['user_id']     = row[1]
            data['user_email']  = row[2]
            data['module_id']   = row[3]
            data['ended']       = row[4]
            data['createdOn']   = row[5]
            data['updatedOn']   = row[6]
            datas.append(data)
        cursor.close()
        conn.close()
        
        # 'May the Force be with you'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))
        else:
            return(datas)

"""
[Summary]: After closing the session we need to find the recommendations based on the answers given on that session <ID>.
[Returns]: Response result.
"""
def find_recommendations(request, ID):
    # 1. Is there a logic file to process the set of answers given in this session? If yes, then, run the logic file. 
    #    This element will be in charge of calling the service to return one or more recommendations, depending on the implemented logic.  
    #    Otherwise, use the static information present in the database to infer the set of recommendations.
    session = (find_session_closed(ID, True))
    
    if (session is None):
        raise modules.error_handlers.BadRequest(request.path, "Unable to find recommendations for this session, maybe, there is something wrong with the answers given in this session.", 403) 

    module               = views.module.find_module(session['module_id'], True)
    tree                 = views.module.get_module_tree(str(session['module_id']), True)
    # Checks if tree exists
    if (tree != None):
        ordered_questions    = modules.utils.order_questions(tree, session['questions'], [])

    #if (session['module_logic'] != None):
    if (module[0]['logic_filename'] != None):
        try:
            # 2.1. Get information related to the current session. This includes the information about the module, the set of related questions, and the answers given by the user to those questions.
            json_session = json.loads(json.dumps(find_session(ID, True), indent=4, sort_keys=False, default=str))
            # Replace the questions with ordered questions
            # If questions exist
            if(tree != None):
                json_session['questions'] = ordered_questions
            # 2.2. Get the set of available recommendations.
            json_recommendations = json.loads(json.dumps(views.recommendation.get_recommendations(True), indent=4, sort_keys=False, default=str))
            
            # 2.3 Get dependencies of the current module, including the last sessions there were flagged has being closed.
            module_id   = json_session['module_id']
            user_id     = json_session['user_id']
            dependencies = views.dependency.find_dependency_of_module(module_id, True)

            if (dependencies):
                for dependency in dependencies:
                    del dependency['id']
                    del dependency['createdon']
                    del dependency['updatedon']
                    dep_module_id = dependency['module']['id']
                    # Get the last session of each dependency
                    last_session_id    = (find_sessions_of_user_module(dep_module_id, user_id, True)[0])['id']
                    # Get the answers given to that last session 
                    last_session = find_session(last_session_id, True)
                    dependency['module']['last_session'] = last_session
            
            json_session['dependencies'] =  json.loads(json.dumps(dependencies, indent=4, sort_keys=False, default=str))

            # 2.4. Dynamically load the logic element for the current session.
            module_logic_filename = module[0]['logic_filename']
            module_logic_filename = module_logic_filename[0: module_logic_filename.rfind('.')] # Remove file extension
            # name = "external." + module_logic_filename + "." + module_logic_filename
            mod = __import__('external.' + module_logic_filename, fromlist=[''])
            try:
                provided_recommendations = mod.run(json_session, json_recommendations)
            except Exception as e:
                modules.utils.console_log("logic_file", str(e))
                raise modules.error_handlers.BadRequest(request.path, str(e), 500)
                
            # 2.5. Make the recommendations taking into account the results of the logic element.
            if (len(provided_recommendations) != 0):
                for recommendation_id in provided_recommendations:
                    add_logic_session_recommendation(ID, recommendation_id)

        except Exception as e:
            modules.utils.console_log("end_session", str(e))
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)

    # 2. Get the list of recommendations to be stored in the session.
    #    -> Some redundancy is expected to exist on the database, however, it avoids further 
    #       processing when checking the history of sessions.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        if (module[0]['logic_filename'] != None):
            table_name = "View_Recommendation_Logic"
        else:
            table_name = "View_Recommendation"
        
        cursor.execute("SELECT session_id, recommendation_id, recommendation, recommendation_description, guideFileName FROM " + table_name + " WHERE session_id=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
    # 2.1 Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))
    
    result = {}
    recommendations = []
    result['recommendations'] = recommendations
    for row in res:
        if ("id" not in result): result['id']   = row[0]
        recommendation = {}
        recommendation['id']                    = row[1]
        recommendation['content']               = row[2]
        recommendation['description']           = row[3]
        recommendation['recommendation_guide']  = row[4]
        recommendations.append(recommendation)
        # 3. Store the recommendations for the current session, only for those module that are not using any kind of external logic. 
        if (module[0]['logic_filename'] == None):
            try:
                conn2    = mysql.connect()
                cursor2  = conn2.cursor()
                cursor2.execute("INSERT INTO Session_Recommendation (sessionID, recommendationID) VALUES (%s, %s)", (ID, recommendation['id']))
                conn2.commit()
            except Exception as e:
                raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
            finally:
                cursor2.close()
                conn2.close()
    cursor.close()
    conn.close()
    # print(result)

    # 4. Create ZIP with recommendations and guides
    # 4.1 Create the temporary directory to be zipped
    temp_dir = 'temp/session'+str(ID)+'/'
    if not os.path.exists(temp_dir):
        os.mkdir(temp_dir)
    # 4.2 Generate the PDF recommendations file    
    modules.utils.build_recommendations_PDF(module_name=module[0]['shortname'], session_id=ID, recommendations=result)
    # 4.3 Add guides to the temporary directory
    for recm in recommendations:
        if recm['recommendation_guide'] is not None:
            shutil.copyfile('external/'+str(recm['recommendation_guide']), temp_dir+str(recm['recommendation_guide']))
    # 4.4 Zip all the files
    zipped = modules.utils.create_recommendations_ZIP(module_name=module[0]['shortname'], session_id=ID)
    # 4.5 Remove all the files created to zip
    if zipped:
        shutil.rmtree(temp_dir)
    return(modules.utils.build_response_json(request.path, 200, result))  


"""
[Summary]: Adds a recommendation to a session, this method is exclusively used after the logic of a module is executed.
[Returns]: 
"""
def add_logic_session_recommendation(session_id, recommendation_id):
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO Session_Recommendation (sessionID, recommendationID) VALUES (%s, %s)", (session_id, recommendation_id))
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # The recommendation is linked to the session.
    return (True)

"""
[Summary]: Counts number of closed sessions by module ID and user ID.
[Returns]: Returns response result.
"""
def count_sessions_of_user_module(module_id, user_id):
    # Let's get existing sessions from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(session_id) FROM View_User_Sessions WHERE moduleID=%s AND user_id=%s AND ended=1 ORDER BY session_id DESC", (module_id, user_id))
        res = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)

    if (res):
        return res[0][0]
    else:
        return 0
