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
from flask import request
from datetime import datetime
import os
import modules.error_handlers, modules.utils # SAM's modules
import views.user, views.recommendation, views.question, views.dependency # SAM's views

"""
[Summary]: Adds a new Module.
[Returns]: Response result.
"""
@app.route('/api/module', methods=['POST'])
def add_module():
    DEBUG=False
    if request.method != 'POST': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticatedAdmin(request)

    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON
    if (not modules.utils.valid_json(json_data, {"shortname", "fullname", "displayname"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    
    
    shortname       = json_data['shortname']
    fullname        = json_data['fullname']
    displayname     = json_data['displayname']

    # Check if module's short name and display name are unique
    shortnames, displaynames = get_modules_short_displaynames()
    if shortname in shortnames:
        raise modules.error_handlers.BadRequest(request.path, str("'Abbreviation' already in use."), 500) 
    if displayname in displaynames:
        raise modules.error_handlers.BadRequest(request.path, str("'Display Name' already in use."), 500) 

    tree            = None
    if ('tree' in json_data): 
        tree = json_data['tree']
    recommendations = "recommendations" in json_data and json_data['recommendations'] or None
    dependencies    = "dependencies" in json_data and json_data['dependencies'] or None
    avatar      = "avatar" in json_data and json_data['avatar'] or None
    description = "description" in json_data and json_data['description'] or None
    type_id     = "type_id" in json_data and json_data['type_id'] or None
    logic       = "logic_filename" in json_data and json_data['logic_filename'] or None
    createdon   = "createdon" in json_data and json_data['createdon'] or None
    updatedon   = "updatedon" in json_data and json_data['updatedon'] or None
    
    # Build the SQL instruction using our handy function to build sql instructions.
    columns = ["shortname", "fullname", "displayname", type_id and "typeID" or None, avatar and "avatar" or None, description and "description" or None, createdon and "createdon" or None, updatedon and "updatedon" or None]
    values  = (shortname, fullname, displayname, type_id, avatar, description, createdon, updatedon)
    
    sql, values = modules.utils.build_sql_instruction("INSERT INTO module", columns, values)
    if (DEBUG): print("[SAM-API]: [POST]/api/module - " + sql + " => " + str(values))

    # Add Module and iterate the tree of the module in order to create the questions and answers mapped to the current module.
    module_id = modules.utils.db_execute_update_insert(mysql, sql, values)
    if ('tree' in json_data):
        for node in tree: 
            iterate_tree_nodes(recommendations, "INSERT", module_id, node)
    
    # Store the mapping of question_answer and recommendations (DB table Recommendation_Question_Answer)
    # Get the question_answer id primary key value, through [question_id] and [answer_id]
    if recommendations:
        for recommendation in recommendations:
            for question_answer in recommendation['questions_answers']:
                qa_res = views.question.find_question_answers_2(question_answer['question_id'], question_answer['answer_id'], True)
                if (qa_res is None): return(modules.utils.build_response_json(request.path, 400)) 
                qa_res = qa_res[0]
                if (DEBUG): print("[SAM-API] [POST]/api/module - question_id = " + str(question_answer['question_id']) + ", answer_id=" + str(question_answer['answer_id']) + " => Question_Answer_id =" + str(qa_res['question_answer_id']))
                question_answer['id'] = qa_res['question_answer_id']
    
        # Add the recommendation with the link between questions and answers
        for recommendation in recommendations:
            views.recommendation.add_recommendation(recommendation)
    
    # Add dependencies, only if the current module depends on another module.
    if (module_id and dependencies):
        for dependency in dependencies:
                views.dependency.add_dependency({"module_id": module_id, "depends_on": dependency['module']['id']}, True)

    # If availabe, set the logic filename after knowing the database id of the module
    if logic and module_id:
        final_logic_filename = "logic_" + str(module_id) + ".py"
        sql, values = modules.utils.build_sql_instruction("UPDATE module", ["logicFilename"], final_logic_filename, "WHERE id="+str(module_id))
        modules.utils.db_execute_update_insert(mysql, sql, values, True)

    # 'Do, or do not, there is no try.'
    return(modules.utils.build_response_json(request.path, 200, {"id": module_id, "tree": tree}))  

"""
[Summary]: Delete logic file linked to a module.
[Returns]: Returns a success or error response
"""
@app.route('/api/module/<ID>/logic', methods=["DELETE"])
def delete_module_logic(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'DELETE': return
    
    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticatedAdmin(request)

    # Get information about module and remove logic file
    module = find_module(ID, True)

    if (module[0]['logic_filename']):
        try:
            os.remove(os.getcwd() + "/external/" + module[0]['logic_filename'])
        except OSError as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)

    # The Delete request was a success, the user 'took the blue pill'.
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)


"""
[Summary]: Delete questions linked to a module.
[Returns]: Returns a success or error response
"""
@app.route('/api/module/<ID>/questions', methods=["DELETE"])
def delete_module_questions(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'DELETE': return
    
    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticatedAdmin(request)

    # Get the set of questions linked to this module.
    questions = find_module_questions(ID, True)
    if (questions):
        for question in questions:
            views.question.delete_question(question['id'], True)
    
    # Delete the module itself and all the sessions linked to him.
    # delete_module(ID, True)

    # The Delete request was a success, the user 'took the blue pill'.
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)

"""
[Summary]: Delete answers linked to a module.
[Returns]: Returns a success or error response
"""
@app.route('/api/module/<ID>/answers', methods=["DELETE"])
def delete_module_answers(ID, internal_call=False):
    if (not internal_call): 
        if request.method != 'DELETE': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticatedAdmin(request)

    # Get the set of answers linked to this module.
        # Get the set of questions linked to this module.
    answers = find_module_answers(ID, True)
    if (answers):
        for answer in answers:
            views.answer.delete_answer(answer['id'], True)
    
    # Delete the module itself and all the sessions linked to him.
    # delete_module(ID, True)
    
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)


"""
[Summary]: Delete a module (partial delete - Linked questions and answers are not deleted)
[Returns]: Returns a success or error response
"""
@app.route('/api/module/<ID>', methods=["DELETE"])
def delete_module_partial(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'DELETE': return
    
    # 1. Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticatedAdmin(request)

    # 2. Delete logic file associated
    delete_module_logic(ID, True)

    # 3. Connect to the database and delete the resource
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("DELETE FROM module WHERE ID=%s", ID)
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 4. The Delete request was a success, the user 'took the blue pill'.
    if (not internal_call): 
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)

"""
[Summary]: Fully delete a module (including sessions, linked questions and answers)
[Returns]: Returns a success or error response
"""
@app.route('/api/module/<ID>/full', methods=["DELETE"])
def delete_module_full(ID, internal_call=False):
    if (not internal_call): 
        if request.method != 'DELETE': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticatedAdmin(request)

    # Get and delete the set of answers and questions linked to this module.
    delete_module_answers(ID, True)
    delete_module_questions(ID, True)
    
    # Delete the module itself and all the sessions linked to him.
    delete_module_partial(ID, True)
    
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)

"""
[Summary]: Updates a Module.
[Returns]: returns 200 if the operation was a success, 500 otherwise.
"""
@app.route('/api/module', methods=['PUT'])
def update_module():
    DEBUG=False
    # Check if the user has permissions to access this resource
    views.user.isAuthenticatedAdmin(request)
    # Delete the module but not to forget to preserve the session related to this module that  is being delete just for the sake of being easier to update is info based on the tree parsed
    if request.method != 'PUT': return
    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"id"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    

    module_id       = json_data['id']
    tree            = None
    # If there is a tree to update
    if ('tree' in json_data):
        modules.utils.console_log("[PUT]/api/module", "Tree exists")
        tree        = json_data['tree']
    # If the user has choosen to erase all questions
    if (tree is None):
        modules.utils.console_log("[PUT]/api/module", "No tree exists")
        sql     = "DELETE FROM module_question WHERE moduleID=%s"
        values  = module_id
        modules.utils.db_execute_update_insert(mysql, sql, values)

    #
    dependencies    = "dependencies" in json_data and json_data['dependencies'] or None
    recommendations = "recommendations" in json_data and json_data['recommendations'] or None
    shortname       = "shortname" in json_data and json_data['shortname'] or None
    fullname        = "fullname" in json_data and json_data['fullname'] or None
    displayname     = "displayname" in json_data and json_data['displayname'] or None
    avatar          = "avatar" in json_data and json_data['avatar'] or None
    description     = "description" in json_data and json_data['description'] or None
    type_id         = "type_id" in json_data and json_data['type_id'] or None
    logic           = "logic_filename" in json_data and "logic_"+str(module_id)+".py" or None
    createdon       = None
    updatedon       = datetime.now()
    
    # Build the SQL instruction using our handy function to build sql instructions.
    columns = [shortname and "shortname" or None, fullname and "fullname" or None, displayname and "displayname" or None, type_id and "typeID" or None, logic and "logicFilename" or None, avatar and "avatar" or None, description and "description" or None, createdon and "createdon" or None, updatedon and "updatedon" or None]
    values  = (shortname, fullname, displayname, type_id, logic, avatar, description, createdon, updatedon)
    where   = "WHERE id="+str(module_id)

    sql, values = modules.utils.build_sql_instruction("UPDATE module", columns, values, where)
    if (DEBUG): modules.utils.console_log("[PUT]/api/module", str(sql + " => " + str(values) + " " + where))

    # Update 
    modules.utils.db_execute_update_insert(mysql, sql, values)
    
    # Iterate the tree of module in order to update questions an answers of the module
    if ('tree' in json_data):
        for node in tree:   
            iterate_tree_nodes(recommendations, "UPDATE", module_id, node)

    # Update the dependency
    if (dependencies):
        for dependency in dependencies:
            flag_remove = "to_remove" in dependency and dependency['to_remove'] or None
            # Remove the dependency
            if (flag_remove):
                views.dependency.delete_dependency(dependency['id'], True)
            else:
                views.dependency.add_dependency({"module_id": module_id, "depends_on": dependency['module']['id']}, True)

    if (recommendations):
        # Check if there are any recommendation flagged to be removed, what is removed is not the recommentation but the mapping of a recommendation to the current module
        for recommendation in recommendations:
            flag_remove = "to_remove" in recommendation and recommendation['to_remove'] or None
            # Remove the recommendation
            if (flag_remove):
                views.recommendation.remove_recommendation_of_module(recommendation['id'], module_id, True)
            # Add a new recommendation
            else:
                # Store the mapping of question_answer and recommendations (DB table Recommendation_Question_Answer)
                # Get the question_answer id primary key value, through [question_id] and [answer_id]    
                for question_answer in recommendation['questions_answers']:
                    qa_res = views.question.find_question_answers_2(question_answer['question_id'], question_answer['answer_id'], True)
                    if (qa_res is None): return(modules.utils.build_response_json(request.path, 400)) 
                    qa_res = qa_res[0]
                    if (DEBUG): print("[SAM-API] [POST]/api/module - question_id = " + str(question_answer['question_id']) + ", answer_id=" + str(question_answer['answer_id']) + " => Question_Answer_id =" + str(qa_res['question_answer_id']))
                    question_answer['id'] = qa_res['question_answer_id']
                    print("!---->" + str(question_answer['id']))
                
                # Add the recommendation with the link between questions and answers
                views.recommendation.add_recommendation(recommendation)
    
    return(modules.utils.build_response_json(request.path, 200, {"id": module_id}))  

"""
[Summary]: Get modules.
[Returns]: Returns a set of modules.
"""
@app.route('/api/modules', methods=['GET'])
def get_modules():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the modules from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, typeID, shortname, fullname, displayname, logicfilename, description, avatar, createdon, updatedon FROM module WHERE disable = 0")
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
            data['id']              = row[0]
            data['type_id']         = row[1]
            data['shortname']       = row[2]
            data['fullname']        = row[3]
            data['displayname']     = row[4]
            data['logic_filename']  = row[5]
            data['plugin']          = check_plugin(row[0], True)
            data['description']     = row[6]
            data['avatar']          = row[7]
            data['createdon']       = row[8]
            data['updatedon']       = row[9]
            datas.append(data)

        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young padawan'.
        return(modules.utils.build_response_json(request.path, 200, datas))    

"""
[Summary]: Get questions of each module.
[Returns]: Returns a set of modules.
"""
@app.route('/api/modules/questions', methods=['GET'])
def get_modules_questions():
    if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # Let's get the resource from the DB
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT DISTINCT module_id FROM view_module_questions_answers")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results. 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = []
        # Module IDs first
        for row in res:
            module = {}
            module['id']            = row[0]
            module['questions']     = find_module_questions(module['id'], True)
            datas.append(module)
    cursor.close()
    conn.close()
    
    # 'May the Force be with you, young padawan'.
    return(modules.utils.build_response_json(request.path, 200, datas))    

"""
[Summary]: Get answers of each module.
[Returns]: Returns a set of modules.
"""
@app.route('/api/modules/answers', methods=['GET'])
def get_modules_answers():
    if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # Let's get the resource from the DB
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT DISTINCT module_id FROM view_module_questions_answers")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results. 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = []
        # Module IDs first
        for row in res:
            module = {}
            module['id']            = row[0]
            module['answers']     = find_module_answers(module['id'], True)
            datas.append(module)
    cursor.close()
    conn.close()
    
    # 'May the Force be with you, young padawan'.
    return(modules.utils.build_response_json(request.path, 200, datas))    

"""
[Summary]: Get shortName and displayName of each module.
[Returns]: Returns a set of modules.
"""
def get_modules_short_displaynames():
    # Let's get the resource from the DB
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT shortname, displayName FROM module")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    short_names   = []
    display_names = []
    # Module IDs first
    for row in res:
        short_names.append(row[0])
        display_names.append(row[1])
    cursor.close()
    conn.close()
    
    return short_names, display_names   


"""
[Summary]: Finds a module.
[Returns]: Returns a module.
"""
@app.route('/api/module/<ID>', methods=['GET'])
def find_module(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    if (not internal_call): 
        views.user.isAuthenticated(request)
    
    # Get the tree of the module and other relevant information.
    tree            = (get_module_tree(str(ID), True))
    recommendations = (views.recommendation.find_recommendations_of_module(ID, True))
    dependencies    = (views.dependency.find_dependency_of_module(ID, True))
    
    if (not dependencies): dependencies = []
    if (not recommendations): recommendations = []

    # Let's get the modules from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, typeID, shortname, fullname, displayname, logicfilename, description, avatar, createdon, updatedon FROM module WHERE ID=%s", ID)
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
            data['id']              = row[0]
            data['type_id']         = row[1]
            data['shortname']       = row[2]
            data['fullname']        = row[3]
            data['displayname']     = row[4]
            data['logic_filename']  = row[5]
            data['description']     = row[6]
            data['avatar']          = row[7]
            data['createdon']       = row[8]
            data['updatedon']       = row[9]
            data['tree']            = tree
            data['recommendations'] = recommendations and recommendations or []
            data['dependencies']    = dependencies
            datas.append(data)
        cursor.close()
        conn.close()

        # 'May the Force be with you, young padawan'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))
        else:
            return(datas)

"""
[Summary]: Finds questions linked to a module.
[Returns]: Returns a module.
"""
@app.route('/api/module/<ID>/questions', methods=['GET'])
def find_module_questions(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)


    # Let's get the questions of the module
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT DISTINCT question_id, question, createdon, updatedon FROM view_module_question WHERE module_id=%s", ID)
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
        datas = [] # Create a new nice empty array to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']              = row[0]
            data['content']         = row[1]
            data['createdon']       = row[2]
            data['updatedon']       = row[3]
            datas.append(data)
        cursor.close()
        conn.close()

        # 'May the Force be with you, young padawan'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))
        else:
            return(datas)

"""
[Summary]: Finds answers linked to a module.
[Returns]: Returns a module.
"""
@app.route('/api/module/<ID>/answers', methods=['GET'])
def find_module_answers(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # Let's get the answers linked to the current module.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT DISTINCT answer_id, answer, createdon, updatedon FROM view_module_answers WHERE module_id=%s", ID)
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
        datas = [] # Create a new nice empty array to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']              = row[0]
            data['content']         = row[1]
            data['createdon']       = row[2]
            data['updatedon']       = row[3]
            datas.append(data)
        cursor.close()
        conn.close()

        # 'May the Force be with you, young padawan'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))
        else:
            return(datas)

"""
[Summary]: Get the tree of the module. This tree contains all the questions and answers.
[Returns]: A set of questions, its children, and its answers.
"""
@app.route('/api/module/<pID>/tree', methods=['GET'])
def get_module_tree(pID, internal_call=False):
    # Do you want to add recommendations to the tree? For example, if an answer is X than the recommendation is Y, and so on. This feature is still experimental.
    add_recommendations_to_tree = False
    IDS = []
    if (not internal_call):
        if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # 1.1. Check if the user needs information about all modules available on the database.
    if (pID.lower() == "all"):
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT ID FROM Module ORDER BY ID ASC")
            res = cursor.fetchall()
            if (len(res) != 0):
                for row in res:
                    IDS.append(int(row[0]))
            cursor.close()
            conn.close()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    else:
        IDS.append(pID)

    datas = []
    for ID in IDS:
        # print(" Processing Data of Module " + str(ID))
        # 2. Let's get the main questions of the module.
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT module_id, module_displayname, question_id, question, questionorder, multipleAnswers FROM view_module_question WHERE module_id = %s", ID)
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
        # 2.2. Check for empty results - 'Fasten your seatbelts. It's going to be a bumpy night'.
        if (len(res) == 0):
            cursor.close()
            conn.close()
            if (len(IDS) == 1):
                if (not internal_call):
                    return(modules.utils.build_response_json(request.path, 404))
                else:
                    return None
            else:
                continue
        else:
            # 2.2.1. The initial set of the information about the module.
            for row in res: 
                data = {"id": row[0], "name": row[1]}
                break
            # 2.2.2. Map questions of the module to a JSON Python Object (dic).
            questions = []
            for row in res:
                question = {"id": row[2], "type": "question", "name": row[3], "multipleAnswers" : row[5], "order": row[4], "children": []}
                questions.append(question)
            data.update({"tree":  questions})

            cursor.close()
            conn.close()
        
        # 3. Recursively get each question child and corresponding data (question, answer, and so on).
        for question in data['tree']: 
            get_children(True, question, add_recommendations_to_tree)
             

        if (len(IDS) == 1):    
            # 4. 'May the Force be with you'.
            if (not internal_call):
                return(modules.utils.build_response_json(request.path, 200, data))
            else:
                #del data[request.path]
                return(data['tree'])
        else:
            datas.append(data)
    
    # 4. 'May the Force be with you'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, datas))
    else:
        del datas[request.path]
        # print("### = " + str(datas['tree']))
        return(datas['tree'])


"""
[Summary]: Auxiliary function to check if a subquestion is no longer linked to parent one. 
[Arguments]:
    - $parent$: Parent id.
    - $values$: Child id.
    - $trigger$; Answer id. 
"""
def subquestion_parent_changed(parent, child, trigger):
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        print("SELECT ID FROM question_has_child WHERE parent=%s AND child=%s AND ontrigger=%s", (parent, child, trigger))
        cursor.execute("SELECT ID FROM question_has_child WHERE parent=%s AND child=%s AND ontrigger=%s", (parent, child, trigger))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)

    # 2.1. Check for empty results. 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(True)    
    else:
        cursor.close()
        conn.close()
        return(False)

"""
[Summary]: Auxiliary functions to check if an answer or question is no longer is parent or child.
[Arguments]:
    - $question_id$: Parent id.
    - $answer_id$: Child id.
"""
def parent_changed(question_id, answer_id):
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        print("SELECT ID FROM question_answer WHERE questionID=%s AND answerID=%s", (question_id, answer_id))
        cursor.execute("SELECT ID FROM question_answer WHERE questionID=%s AND answerID=%s", (question_id, answer_id))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)

    # 2.1. Check for empty results. 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(True)    
    else:
        cursor.close()
        conn.close()
        return(False)

"""
[Summary]: When a new question or answer is added on the client side an ID is generated for each one. After that, the user is required to add recommendations. 
           These recommendations will be given taking into account if the user has selected a set of answers to a set of questions. The mapping of questions and 
           answers temporarily uses the previous generated ID. After the process of adding each question and answer to the database, that temporary ID needs to be 
           updated to the new one (i.e., the ID that identifies each question and answer on the database). 
[Arguments]:
    - $client_id$: The id temporary assigned (on the client side) to a question or answer.
    - $database_id$: The 'real' id of the question or answer that is used to update a recommendation.
    - $recommendations$: The list of recommendations.
    - $is_question$: Flag to ascertain if the mapping operation of client_id => database_id is to be performed on a question or an answer.
"""
def update_questions_answers_ids(client_id, database_id, recommendations, is_question):
    DEBUG = False
    if (DEBUG):
        if (is_question):
            print("[SAM-API] update_questions_answers_ids() => Trying to find client_question_id = " + str(client_id) + " in recommendations list.")
        else:
            print("[SAM-API] update_questions_answers_ids() => Trying to find client_question_id = " + str(client_id) + " in recommendations list.")
    
    if (recommendations):
        for recommendation in recommendations:
            # if ("questions_answers" not in recommendation): continue
            for question_answer in recommendation['questions_answers']:
                # Update the questions to the real ID
                if (is_question):
                    if ("client_question_id" in question_answer):
                        if (question_answer['client_question_id'] == client_id):
                            del question_answer['client_question_id']
                            question_answer['question_id'] = database_id
                            if (DEBUG): print("[SAM-API] update_questions_answers_ids() => Found it, updating node = " + str(question_answer))
                else:
                    if ("client_answer_id" in question_answer):
                        if (question_answer['client_answer_id'] == client_id):
                            del question_answer['client_answer_id']
                            question_answer['answer_id'] = database_id
                            if (DEBUG): print("[SAM-API] update_questions_answers_ids() => Found it, updating node = " + str(question_answer))

"""
[Summary]: Iterates the module tree that contains the mapping of questions and answers. This is an auxiliary function of add_module() and update_module().
[Arguments]:
    - $module_id$: Id of the newly created module.
    - $node$:  current node of the tree being processed. 
    - $p_node$: Previous node or parent node.
    - $p_p_node$: Parent of the parent node.
"""
def iterate_tree_nodes(recommendations, operation, module_id, c_node, p_node=None, p_p_node=None):
    debug=False
    # print("[SAM-API] Processing current node = '"+ str(c_node['name'])+"'")
    operation = operation.upper()

    # In the case of an UPDATE operation, we need to check if this question is available on the database; if not, 
    # this means that the user has added a new question/answer and the values are in need of being processed with an INSERT operation.
    # ---> We need to change the operation from UPDATE TO INSERT after encountering this situation. 
    # ---> We can check if a question/answer is NOT available on the database if c_node['id'] == null
    if (operation == "UPDATE" and (not c_node['id'])): 
        operation = "INSERT"

    # 1. Check if the current node is a question or an answer.
    if (c_node["type"] == "question"): 
        
        # 1.1. Add or update question - Table [Question].
        if (operation == "INSERT"):
            sql     = "INSERT INTO question (content, multipleAnswers) VALUES (%s, %s)"
            values  =  (c_node['name'], c_node['multipleAnswers'])
            exists_flag = False
            # Check if the question already exists (i.e. if c_node['id'] == null)
            if (not c_node['id']):
                c_node.update({"id": modules.utils.db_execute_update_insert(mysql, sql, values)})
                # By knowing the client_id update recommendations questions and answers to the database id (c_node['id']).
                update_questions_answers_ids(c_node['client_id'], c_node['id'], recommendations, True)

            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
        if (operation == "UPDATE"):
            sql     = "UPDATE question SET content=%s, multipleAnswers=%s WHERE ID=%s"
            values  = (c_node['name'], c_node['multipleAnswers'], c_node['id'])
            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
            modules.utils.db_execute_update_insert(mysql, sql, values)

        
        # 1.2. Add link to table [Module_Question] - Link question and the module together.
        # Be aware, that child questions are not added to this table. That is, only questions are mapped to modules.
        if (p_node is None):
            if (operation == "INSERT"):
                sql     = "INSERT INTO module_question (moduleID, questionID, questionOrder) VALUES (%s, %s, %s)"
                values  = (module_id,c_node['id'], 0)
                modules.utils.db_execute_update_insert(mysql, sql, values)
                if (debug): print("  -> [?] = '" + sql + ", " + str(values))

        # 1.3. Add Sub question to table [Question_has_Child] - Link question and subquestions by a trigger (i.e., answer).
        # Knowing that the current node is a parent, this is accomplish by checking if the parent was an answer. 
        if (p_node != None):
            if (p_node['type'] == "answer"): 

                if (operation == "INSERT"):
                    sql     = "INSERT INTO question_has_child (parent, child, ontrigger, questionOrder) VALUES (%s, %s, %s, %s)"
                    values  = (p_p_node['id'], c_node['id'], p_node['id'], 0)
                    modules.utils.db_execute_update_insert(mysql, sql, values)
                    if (debug): print("  -> [?] = '" + sql + ", " + str(values))
                
                if (operation == "UPDATE"):
                    if (subquestion_parent_changed(p_p_node['id'], c_node['id'], p_node['id'])):
                        if (debug): print("  -> [?] New Link detected")
                        # Remove the previous link
                        sql     = "DELETE FROM question_has_child WHERE child=%s"
                        values  = c_node['id']
                        if (debug): print("     -> '" + sql + ", " + str(values))
                        modules.utils.db_execute_update_insert(mysql, sql, values)
                        # Add the new link
                        sql     = "INSERT INTO question_has_child (parent, child, ontrigger, questionOrder) VALUES (%s, %s, %s, %s)"
                        values  = (p_p_node['id'], c_node['id'], p_node['id'], 0)
                        if (debug): print("     -> '" + sql + ", " + str(values))
                        modules.utils.db_execute_update_insert(mysql, sql, values)
    else: 
        # 1.1. Add or update answer - Table [Answer].
        if (operation == "INSERT"):
            sql     = "INSERT INTO answer (content) VALUES (%s)"
            values  = c_node['name']
            exists_flag = False
            # Check if the answer already exists (i.e. if c_node['id'] == null)
            if (not c_node['id']):
                # Check if the answer is similar or equal to one already available on the database, if so, use the id of the one that is equal
                # This is performed by checking the contents of an answer. No need to create a new answer on the database if one similar is already available.
                node_id = (modules.utils.db_already_exists(mysql, "SELECT id, content FROM answer WHERE content LIKE %s", c_node['name']))
                print(node_id)
                if (node_id == -1):
                    c_node.update({"id": modules.utils.db_execute_update_insert(mysql, sql, values)}) # Store the ID of the newly created answer.
                else:
                    c_node.update({"id": node_id}) # Store the ID of an answer that was previsouly inserted on the database. 

                # By knowing the client_id update recommendations questions and answers to the database id (c_node['id']).
                update_questions_answers_ids(c_node['client_id'], c_node['id'], recommendations, False)

            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
        
        if (operation == "UPDATE"):
            sql     = "UPDATE answer SET content=%s WHERE ID=%s"
            values  = (c_node['name'], c_node['id'])
            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
            modules.utils.db_execute_update_insert(mysql, sql, values)
        
        if (operation == "INSERT"):
            # 1.2. Add link to table [Question_Answer] - Link question and answer together.
            sql     = "INSERT INTO question_answer (questionID, answerID) VALUES (%s, %s)"
            values  = (p_node['id'], c_node['id'])
            modules.utils.db_execute_update_insert(mysql, sql, values)
            if (debug): print("  -> [?] = '" + sql + ", " + str(values))
        
        if (operation == "UPDATE"):
            # Check if the link between the current answer node and a question was changed (i.e., parent change).
            # If true remove the previous link and assigned the new one
            if (parent_changed(p_node['id'], c_node['id'])):
                # Remove the previous one
                if (debug): print("  -> [?] New Link detected")
                sql     = "DELETE FROM question_answer WHERE answerID=%s AND questionID IN (SELECT questionID From question_answer WHRE answerID=%s)"
                values  = (c_node['id'], c_node['id'])
                if (debug): print("    -> [?] = '" + sql + ", " + str(values))
                modules.utils.db_execute_update_insert(mysql, sql, values)
                # Add new updated link
                sql     = "INSERT INTO question_answer (questionID, answerID) VALUES (%s, %s)"
                values  = (p_node['id'], c_node['id'])
                modules.utils.db_execute_update_insert(mysql, sql, values)
                if (debug): print("    -> [?] = '" + sql + ", " + str(values))

    if (debug): print("\n")
    try:
        # Recursively iterate 
        for child in c_node['children']:
            iterate_tree_nodes(recommendations, operation, module_id, child, c_node, p_node)
    except:
        pass
    return

"""
[Summary]: Auxiliary function to get the sub-questions of a set of questions, and the sub-questions of 
           those, and so on. This is accomplished through our 'friendly neighbor' - recursivity. 
[Arguments]:
    - $initial$:  This flag must be set to true if it is the initial call of the recursive function.
    - $c_childs$: Array that contains the childs of a question ($question_js$ Python object), this must be initially empty.
    - $question$: Current question being analysed (has childs ?).
    - $question_js$: The JSON Python object being populate with data (question information, answers, and so on.)
[Returns]: Returns a JSON object with the mapping of all childs of a set of questions.
"""
def get_children(initial, question, add_recommendations_to_tree):
    children = question['children']
    debug = False
    if (debug): print("# Parsing question [%s] - %s" % (question['id'], question['name']))
    # 1. Get answers of the parent question.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT answer_id, answer FROM view_question_answer WHERE question_id=%s", question['id'])
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 1.2. Store, if available, answers of the parent question - An answer is a child of a parent question.
    if (len(res) != 0):
        for row in res:
            answer = { "id": row[0], "type": "answer", "name": row[1], "children" : []}
            children.append(answer)     
    cursor.close() # Clean the house nice & tidy.

    # 2. Check if the current question has children; IF not, return.
    #    This is the illusive break/return condition of this recursive function - 'Elementary, my dear Watson.'
    if (len(children) == 0): return None

    # Get recommendation(s) for the current answer and question.
    for child in children:
        if (child['type'] == 'question'): continue


    # 3. Get sub-questions triggered by an answer 
    for child in children:
        try:
            cursor  = conn.cursor()
            cursor.execute("SELECT child_id, question, questionOrder, ontrigger, multipleAnswers FROM view_question_childs WHERE parent_id=%s AND ontrigger=%s", (question['id'], child['id']))
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
        # 3.1. Store it!
        if (len(res) != 0):
            for row in res:
                s_question = {"id": row[0], "name": row[1], "multipleAnswers": row[4], "type": "question","order": row[2],"trigger": row[3], "children": []}
                child['children'].append(s_question)
        
        # 3.2. If requested, and a sub-question is no where to be found for the current child, the list of recommendations will be added as children to the current answer.
        else:
            if (add_recommendations_to_tree):
                recommendations = (views.recommendation.find_recommendations_of_question_answer(question['id'], child['id'], True)).json
                # print(str(recommendations))
                if (recommendations != None): child['children'] = recommendations
            
            
    cursor.close()
    conn.close()

    # Debug
    if (debug):
        print("<!> Question [%s] ('%s') has the following answers:" % (question['id'], question['name']))
        for answer in children:
            if (answer['type'] == "answer"):
                print("  -> Answer ID[%d] - %s" % (answer['id'], answer['name']))
                for s_question in answer['children']:
                    print("     -> Question ID[%d] - %s" % (s_question['id'], s_question['name']))

    # 4. Recursive calls and python JSON object construction
    if (len(question['children']) != 0): question.update({"expanded": False})
    for answer in children:
        t_answer = answer
        # We need to go deeper in order to find the questions to be parsed to this recursive function.
        for question in answer['children']:
            t_answer.update({"expanded": False})
            if (question['type'] != 'recommendation'):
                get_children(False, question, add_recommendations_to_tree)
 
"""
[Summary]: Checks if a module is a plugin.
[Returns]: Returns a Boolean.
"""
@app.route('/api/module/<ID>/type', methods=['GET'])
def check_plugin (ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    tree = get_module_tree(str(ID), True)

    if (tree == None):
        plugin = True
    else:
        plugin = False

    if (not internal_call):
        return modules.utils.build_response_json(request.path, plugin)
    else:
        return plugin
