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
from api import app, mysql
from email_validator import validate_email, EmailNotValidError
from flask import Flask, abort, request, jsonify, render_template, redirect, url_for, request
from datetime import datetime
import requests, json, os
import modules.error_handlers, modules.utils # SAM's modules
import views.user, views.module # SAM's views

"""
[Summary]: Adds a new session to a user.
[Returns]: Response result.
"""
@app.route('/session', methods=['POST'])
def add_session():
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

    # 4. Check if there is an identical session closed, 
    #    if true, notify the user on the return response object that a new session will be created; otherwise, 
    #    delete all that of the previously opened session.
    destroySessionID = -1
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, ended updatedOn FROM Session WHERE userID=(SELECT ID FROM User WHERE email=%s) AND moduleID=%s", (obj['email'], obj['module_id']))
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

    
    # 5. Connect to the database and add a new session.
    try:
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO SESSION (userID, moduleID) VALUES ((SELECT ID FROM User WHERE email=%s), %s)", (obj['email'],obj['module_id']))
        data['id'] = conn.insert_id()
        conn.commit()

    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    data['module'] = views.module.find_module(obj['module_id'], True)

    # 6. The request was a success, the user 'took the blue pill'.
    return (modules.utils.build_response_json(request.path, 200, data))

"""
[Summary]: Updates the session with the set of answers given and the corresponding questions.
[Returns]: Response result.
"""
@app.route('/session/<ID>', methods=['PUT'])
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
    
    print(obj)
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
[Summary]: Ends a user's session.
[Returns]: Response result.
"""
@app.route('/session/<ID>/end', methods=['PUT'])
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
@app.route('/session/<ID>/closed', methods=['GET'])
def find_session_closed(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return
    
    # 0. Check if the user has permissions to access this resource.
    if (not internal_call): views.user.isAuthenticated(request)

    # 1. Let's get the data of the session that has ended.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT session_ID, session_userID, session_moduleID, session_ended, session_createdOn, session_updatedOn, question_ID, question, answer_input, module_logic, answer_id, answer FROM View_Session_Answers WHERE session_ID=%s AND session_ended=1", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2. Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (internal_call):
            return(None)
        else:
            return(modules.utils.build_response_json(request.path, 400))
    else:
        # datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        data = {}
        # 3. Let's get the info about the session.
        for row in res:
            data['ID']           = row[0]
            data['userID']       = row[1]
            data['moduleID']     = row[2]
            data['module_logic'] = row[9]
            data['ended']        = row[3]
            data['createdOn']    = row[4]
            data['updatedOn']    = row[5]
            break
        # 4. Let's get the questions and inputted answers.
        questions = []
        for row in res:
            question = {}
            question['ID']           = row[6]
            question['content']      = row[7]
            # Let's check if the answer was user inputted, or selected from the database.
            if (row[8] != None):
                question['answer'] = row[8]
                question.update({"answer": { "ID": -1, "content": row[8]}}) 
            else:
                question.update({"answer": { "ID": row[10], "content": row[11]}})
            questions.append(question)
        data.update({"questions":  questions})
    cursor.close()
        
    # 5. Let's now get the recommendations, if any, stored for this session
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
            recommendation['ID']                  = row[0]
            recommendation['content']             = row[1]
            recommendation['description']         = row[2]
            recommendation['recommendation_guide'] = row[3]
            recommendations.append(recommendation)
        data.update({"recommendations": recommendations})
    conn.close()
    cursor.close()

    # 6. 'May the Force be with you'.
    if (internal_call): 
        return(data) 
    else: 
        return(modules.utils.build_response_json(request.path, 200, data))


"""
[Summary]: Finds a session by ID (opened or closed)
[Returns]: Returns response result.
"""
@app.route('/session/<ID>', methods=['GET'])
def find_session(ID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

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
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        # 2.2. Check if the session requested was ended.
        if (res[0][3] == 1):
            cursor.close()
            conn.close()
            datas = find_session_closed(ID, True)
            if (datas == None):
                return(modules.utils.build_response_json(request.path, 404))
            else:
                return(modules.utils.build_response_json(request.path, 200, datas))  
        
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['ID']          = row[0]
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
    
    if (session['module_logic'] != None):
        try:
            # 2.1. Get information related to the current session. This includes the information about the module, the set of related questions, and the answers given by the user to those questions.
            r = requests.get(request.url_root+"session/"+str(ID), headers={'content-type': 'application/json', 'Authorization': dict(request.headers)['Authorization']})
            r.raise_for_status()
            json_module = json.loads(r.text)
            json_module["Module"] = json_module.pop("/session/"+str(ID))

            # 2.2. Get the set of available recommendations.
            r = requests.get(request.url_root+"recommendations", headers={'content-type': 'application/json', 'Authorization': dict(request.headers)['Authorization']})
            r.raise_for_status()
            json_recommendations = json.loads(r.text)
            json_recommendations["Recommendations"] = json_recommendations.pop("/recommendations")
            
            # 2.2. Dynamically load the logic element for the current session.
            name = "external.elements." + session['module_logic'] + "." + session['module_logic']
            mod = __import__(name, fromlist=[''])
            provided_recommendations = mod.run(json_module, json_recommendations)

            # 2.3. Make the recommendations taking into account the results of the logic element.
            if (len(provided_recommendations) != 0):
                for rec in provided_recommendations:
                    s_name = request.url_root+'recommendation/'+str(rec)+'/session/' + str(ID)
                    print("-->"+s_name)
                    r = requests.get(s_name, headers={'content-type': 'application/json', 'Authorization': dict(request.headers)['Authorization']})
                    r.raise_for_status()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        return(modules.utils.build_response_json(request.path, 200))


         #   raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2. Get the list of recommendations to be stored in the session.
    #    -> Some redundancy is expected to exist on the database, however, it avoids further 
    #       processing when checking the history of sessions.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT session_id, recommendation_id, recommendation, recommendation_description, guideFileName FROM View_Recommendation WHERE session_id=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
    # 2.1 Check for empty results.
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))

    results = []
    for row in res:
        result = {}
        result['session_id']                 = row[0]
        result['recommendation_id']          = row[1]
        result['recommendation']             = row[2]
        result['recommendation_description'] = row[3]
        result['guide_filename']             = row[4]
        
        results.append(result)
        # 3. Store the recommendations for the current session.
        try:
            conn2    = mysql.connect()
            cursor2  = conn2.cursor()
            cursor2.execute("INSERT INTO Session_Recommendation (sessionID, recommendationID) VALUES (%s, %s)", (ID, result['recommendation_id']))
            conn2.commit()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
        finally:
            cursor2.close()
            conn2.close()
    cursor.close()
    conn.close()

    # 4. 'May the Force be with you'.
    return(modules.utils.build_response_json(request.path, 200, results))  
