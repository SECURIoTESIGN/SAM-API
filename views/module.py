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
import requests, json, os, copy
import modules.error_handlers, modules.utils # SAM's modules
import views.user, views.recommendation, views.question # SAM's views

"""
[Summary]: Adds a new Module.
[Returns]: Response result.
"""
@app.route('/module', methods=['POST'])
def add_module():
    DEBUG=True
    if request.method != 'POST': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON
    if (not modules.utils.valid_json(json_data, {"shortname", "fullname", "displayname", "tree"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    
    
    shortname       = json_data['shortname']
    fullname        = json_data['fullname']
    displayname     = json_data['displayname']
    tree            = json_data['tree']
    recommendations = "recommendations" in json_data and json_data['recommendations'] or None
    avatar      = "avatar" in json_data and json_data['avatar'] or None
    description = "description" in json_data and json_data['description'] or None
    type_id     = "type_id" in json_data and json_data['type_id'] or None
    logic       = "logic_filename" in json_data and json_data['logic_filename'] or None
    createdon   = "createdon" in json_data and json_data['createdon'] or None
    updatedon   = "updatedon" in json_data and json_data['updatedon'] or None
    
    # Build the SQL instruction using our handy function to build sql instructions.
    columns = ["shortname", "fullname", "displayname", type_id and "typeID" or None, logic and "logicFilename" or None, avatar and "avatar" or None, description and "description" or None, createdon and "createdon" or None, updatedon and "updatedon" or None]
    values  = (shortname, fullname, displayname, type_id, logic, avatar, description, createdon, updatedon)
    
    sql, values = modules.utils.build_sql_instruction("INSERT INTO Module", columns, values)
    if (DEBUG): print("[SAM-API]: [POST]/module - " + sql + " => " + str(values))

    # Add Module and iterate the tree of the module in order to create the questions and answers mapped to the current module.
    module_id = modules.utils.db_execute_update_insert(mysql, sql, values)
    for node in tree: 
        iterate_tree_nodes(recommendations, "INSERT", module_id, node)
    
    # Store the mapping of question_answer and recommendations (DB table Recommendation_Question_Answer)
    # 1. Get the question_answer id primary key value, through [question_id] and [answer_id]    
    for recommendation in recommendations:
        for question_answer in recommendation['questions_answers']:
            qa_res = views.question.find_question_answers_2(question_answer['question_id'], question_answer['answer_id'], True)
            if (qa_res is None): return(modules.utils.build_response_json(request.path, 400)) 
            qa_res = qa_res[0]
            if (DEBUG): print("[SAM-API] [POST]/module - question_id = " + str(question_answer['question_id']) + ", answer_id=" + str(question_answer['answer_id']) + " => Question_Answer_id =" + str(qa_res['question_answer_id']))
            question_answer['id'] = qa_res['question_answer_id']
    

    # 2. Add the recommendation with the link between questions and answers
    for recommendation in recommendations:
        views.recommendation.add_recommendation(recommendation)
    

    return(modules.utils.build_response_json(request.path, 200, {"id": module_id, "tree": tree}))  

"""
[Summary]: Updates a Module.
[Returns]: returns 200 if the operation was a success, 500 otherwise.
"""
@app.route('/module', methods=['PUT'])
def update_module():
    DEBUG=True
    # Delete the module but not to forget to preserve the session related to this module that  is being delete just for the sake of being easier to update is info based on the tree parsed
    if request.method != 'PUT': return
    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"id", "tree"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    
    
    module_id   = json_data['id']
    tree        = json_data['tree']
    #
    shortname   = "shortname" in json_data and json_data['shortname'] or None
    fullname    = "fullname" in json_data and json_data['fullname'] or None
    displayname = "displayname" in json_data and json_data['displayname'] or None
    avatar      = "avatar" in json_data and json_data['avatar'] or None
    description = "description" in json_data and json_data['description'] or None
    type_id     = "type_id" in json_data and json_data['type_id'] or None
    logic       = "logic_filename" in json_data and json_data['logic_filename'] or None
    createdon   = "createdon" in json_data and json_data['createdon'] or None
    updatedon   = "updatedon" in json_data and json_data['updatedon'] or None
    
    # Build the SQL instruction using our handy function to build sql instructions.
    columns = [shortname and "shortname" or None, fullname and "fullname" or None, displayname and "displayname" or None, type_id and "typeID" or None, logic and "logicFilename" or None, avatar and "avatar" or None, description and "description" or None, createdon and "createdon" or None, updatedon and "updatedon" or None]
    values  = (shortname, fullname, displayname, type_id, logic, avatar, description, createdon, updatedon)
    where   = "WHERE id="+str(module_id)
    
    sql, values = modules.utils.build_sql_instruction("UPDATE Module", columns, values, where)
    if (DEBUG): print("[SAM-API]: [PUT]/module - " + sql + " => " + str(values))
    
    # Update 
    modules.utils.db_execute_update_insert(mysql, sql, values)
    
    # Iterate the tree of module in order to update questions an answers of the module
    for node in tree:   
        iterate_tree_nodes(recommendations, "UPDATE", module_id, node)

    return(modules.utils.build_response_json(request.path, 200))  

"""
[Summary]: Get modules.
[Returns]: Returns a set of modules.
"""
@app.route('/modules', methods=['GET'])
def get_modules():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the modules from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, typeID, shortname, fullname, displayname, logicfilename, description, avatar, createdon, updatedon FROM Module")
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
[Summary]: Finds a module.
[Returns]: Returns a module.
"""
@app.route('/module/<ID>', methods=['GET'])
def find_module(ID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)
    
    # 2 Get the tree of the module
    tree = (get_module_tree(ID, True)).json

    # 3. Let's get the modules from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, typeID, shortname, fullname, displayname, logicfilename, description, avatar, createdon, updatedon FROM Module WHERE ID=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 3.1. Check for empty results. 
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
            data['description']     = row[6]
            data['avatar']          = row[7]
            data['createdon']       = row[8]
            data['updatedon']       = row[9]
            data['tree']            = tree
            datas.append(data)
        cursor.close()
        conn.close()

        # 4. 'May the Force be with you, young padawan'.
        return(modules.utils.build_response_json(request.path, 200, datas))    

"""
[Summary]: Get the tree of the module. This tree contains all the questions and answers.
[Returns]: A set of questions, its children, and its answers.
"""
@app.route('/module/<pID>/tree', methods=['GET'])
def get_module_tree(pID, internal_call=False):
    # Do you want to add recommendations to the tree? For example, if an answer is X than the recommendation is Y, and so on. This feature is still experimental.
    add_recommendations_to_tree = False
    IDS = []
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
        print(" Processing Data of Module " + str(ID))
        # 2. Let's get the main questions of the module.
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT module_id, module_displayname, question_id, question, questionorder FROM View_Module_Question WHERE module_id = %s", ID)
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
        # 2.2. Check for empty results - 'Fasten your seatbelts. It's going to be a bumpy night'.
        if (len(res) == 0):
            cursor.close()
            conn.close()
            if (len(IDS) == 1):
                return(modules.utils.build_response_json(request.path, 404)) 
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
                question = {"id": row[2], "type": "question", "name": row[3], "order": row[4], "children": []}
                questions.append(question)
            data.update({"tree":  questions})

            cursor.close()
            conn.close()
        
        # 3. Recursively get each question child and corresponding data (question, answer, and so on).
        for question in data['tree']: 
            get_children(True, question, add_recommendations_to_tree)
             

        if (len(IDS) == 1):    
            # 5. 'May the Force be with you'.
            return(modules.utils.build_response_json(request.path, 200, data))
        else:
            datas.append(data)
    

    return(modules.utils.build_response_json(request.path, 200, datas))


    IDS = []
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

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
        print(" Processing Data of Module " + str(ID))
        # 2. Let's get info about the selected module.
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT module_id, module_displayname, question_id, question, questionorder FROM View_Module_Question WHERE module_id = %s", ID)
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
        # 2.2. Check for empty results - 'Fasten your seatbelts. It's going to be a bumpy night'.
        if (len(res) == 0):
            cursor.close()
            conn.close()
            if (len(IDS) == 1):
                return(modules.utils.build_response_json(request.path, 404)) 
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
                question = {"id": row[2], "name": row[3], "order": row[4]}
                questions.append(question)
            data.update({"questions":  questions})

            cursor.close()
            conn.close()
        
        # 3. Let's get the answers of each, previously found, question.
        for question in data['questions']:
            try:
                conn    = mysql.connect()
                cursor  = conn.cursor()
                cursor.execute("SELECT answer_id, answer FROM View_Question_Answer WHERE question_id = %s", question['id'])
                res = cursor.fetchall()
            except Exception as e:
                raise modules.error_handlers.BadRequest(request.path, str(e), 500)
            # 3.1. 'déjà vu'.
            if (len(res) == 0):
                if (conn.open):
                    cursor.close()
                    conn.close()
                # return(modules.utils.build_response_json(request.path, 404))    
            else:
                answers = []
                for row in res:
                    answer = { "id": row[0], "name": row[1]}
                    answers.append(answer)
                question.update({"answers": answers})
            if (conn.open):
                cursor.close()
                conn.close()

        # 4. Recursively get each question child and corresponding data (question, answer, and so on).
        for question in data['questions']: 
            childs = []
            get_children(True, childs, question)
            # 4.1. Update the current question JSON python object (dic) with childs (i.e., sub-questions).
            question.update({"childs": childs})

        if (len(IDS) == 1):    
            # 5. 'May the Force be with you'.
            return(modules.utils.build_response_json(request.path, 200, data))
        else:
            datas.append(data)
    
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))
        else:
            return(datas)

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
        print("SELECT ID FROM Question_has_Child WHERE parent=%s AND child=%s AND ontrigger=%s", (parent, child, trigger))
        cursor.execute("SELECT ID FROM Question_has_Child WHERE parent=%s AND child=%s AND ontrigger=%s", (parent, child, trigger))
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
        print("SELECT ID FROM Question_Answer WHERE questionID=%s AND answerID=%s", (question_id, answer_id))
        cursor.execute("SELECT ID FROM Question_Answer WHERE questionID=%s AND answerID=%s", (question_id, answer_id))
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
    DEBUG = True
    if (DEBUG):
        if (is_question):
            print("[SAM-API] update_questions_answers_ids() => Trying to find client_question_id = " + str(client_id) + " in recommendations list.")
        else:
            print("[SAM-API] update_questions_answers_ids() => Trying to find client_question_id = " + str(client_id) + " in recommendations list.")
            
    for recommendation in recommendations:
        for question_answer in recommendation['questions_answers']:
            # Update the questions to the real ID
            if (is_question):
                if ("client_question_id" in question_answer):
                    if (question_answer['client_question_id'] == client_id):
                        del question_answer['client_question_id']
                        question_answer['question_id'] = database_id
                        print("[SAM-API] update_questions_answers_ids() => Found it, updating node = " + str(question_answer))
            else:
                if ("client_answer_id" in question_answer):
                    if (question_answer['client_answer_id'] == client_id):
                        del question_answer['client_answer_id']
                        question_answer['answer_id'] = database_id
                        print("[SAM-API] update_questions_answers_ids() => Found it, updating node = " + str(question_answer))

"""
[Summary]: Iterates the module tree that contains the mapping of questions and answers. This is an auxiliary function of add_module().
[Arguments]:
    - $module_id$: Id of the newly created module.
    - $node$:  current node of the tree being processed. 
    - $p_node$: Previous node or parent node.
    - $p_p_node$: Parent of the parent node.
"""
def iterate_tree_nodes(recommendations, operation, module_id, c_node, p_node=None, p_p_node=None):
    debug=True
    print("[SAM-API] Processing current node = '"+ str(c_node['name'])+"'")
    operation = operation.upper()

    # 1. Check if the current node is a question or an answer.
    if (c_node["type"] == "question"): 
        # 1.1. Add or update question - Table [Question].
        if (operation == "INSERT"):
            sql     = "INSERT INTO Question (content) VALUES (%s)"
            values  = c_node['name']
            exists_flag = False
            try: exists_flag = modules.utils.db_already_exists(mysql, "SELECT id FROM Question WHERE id=%s", c_node['id'])
            except: pass
            if (not exists_flag):
                c_node.update({"id": modules.utils.db_execute_update_insert(mysql, sql, values)})
                # By knowing the client_id update recommendations questions and answers to the database id (c_node['id']).
                update_questions_answers_ids(c_node['client_id'], c_node['id'], recommendations, True)

            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
        if (operation == "UPDATE"):
            sql     = "UPDATE Question SET content=%s WHERE ID=%s"
            values  = (c_node['name'], c_node['id'])
            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
            modules.utils.db_execute_update_insert(mysql, sql, values)

        
        # 1.2. Add link to table [Module_Question] - Link question and the module together.
        # Be aware, that child questions are not added to this table. That is, questions that are triggered by an answer.
        if (p_node is None):
            if (operation == "INSERT"):
                sql     = "INSERT INTO Module_Question (moduleID, questionID, questionOrder) VALUES (%s, %s, %s)"
                values  = (module_id,c_node['id'], 0)
                modules.utils.db_execute_update_insert(mysql, sql, values)
                if (debug): print("  -> [?] = '" + sql + ", " + str(values))

        # 1.3. Add Sub question to table [Question_has_Child] - Link question and subquestions by a trigger (i.e., answer).
        # Knowing that the current node is a parent, this is accomplish by checking if the parent was an answer. 
        if (p_node != None):
            if (p_node['type'] == "answer"): 
                if (operation == "INSERT"):
                    sql     = "INSERT INTO Question_has_Child (parent, child, ontrigger, questionOrder) VALUES (%s, %s, %s, %s)"
                    values  = (p_p_node['id'], c_node['id'], p_node['id'], 0)
                    modules.utils.db_execute_update_insert(mysql, sql, values)
                    if (debug): print("  -> [?] = '" + sql + ", " + str(values))
                if (operation == "UPDATE"):
                    if (subquestion_parent_changed(p_p_node['id'], c_node['id'], p_node['id'])):
                        if (debug): print("  -> [?] New Link detected")
                        # Remove the previous link
                        sql     = "DELETE FROM Question_has_Child WHERE child=%s"
                        values  = c_node['id']
                        if (debug): print("     -> '" + sql + ", " + str(values))
                        modules.utils.db_execute_update_insert(mysql, sql, values)
                        # Add the new link
                        sql     = "INSERT INTO Question_has_Child (parent, child, ontrigger, questionOrder) VALUES (%s, %s, %s, %s)"
                        values  = (p_p_node['id'], c_node['id'], p_node['id'], 0)
                        if (debug): print("     -> '" + sql + ", " + str(values))
                        modules.utils.db_execute_update_insert(mysql, sql, values)
    else: 
        # 1.1. Add or update answer - Table [Answer].
        if (operation == "INSERT"):
            sql     = "INSERT INTO Answer (content) VALUES (%s)"
            values  = c_node['name']
            exists_flag = False
            try: exists_flag = modules.utils.db_already_exists(mysql, "SELECT id FROM Answer WHERE id=%s", c_node['id'])
            except: pass
            if (not exists_flag):
                c_node.update({"id": modules.utils.db_execute_update_insert(mysql, sql, values)}) # Store the ID of the newly created answer.
                # By knowing the client_id update recommendations questions and answers to the database id (c_node['id']).
                update_questions_answers_ids(c_node['client_id'], c_node['id'], recommendations, False)

            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
        if (operation == "UPDATE"):
            sql     = "UPDATE Answer SET content=%s WHERE ID=%s"
            values  = (c_node['name'], c_node['id'])
            if (debug): print("  -> [" + str(c_node["id"]) + "] = '" + sql + ", " + str(values))
            modules.utils.db_execute_update_insert(mysql, sql, values)
        
        if (operation == "INSERT"):
            # 1.2. Add link to table [Question_Answer] - Link question and answer together.
            sql     = "INSERT INTO Question_Answer (questionID, answerID) VALUES (%s, %s)"
            values  = (p_node['id'], c_node['id'])
            modules.utils.db_execute_update_insert(mysql, sql, values)
            if (debug): print("  -> [?] = '" + sql + ", " + str(values))
        if (operation == "UPDATE"):
            # Check if the link between the current answer node and a question was changed (i.e., parent change).
            # If true remove the previous link and assigned the new one
            if (parent_changed(p_node['id'], c_node['id'])):
                # Remove the previous one
                if (debug): print("  -> [?] New Link detected")
                sql     = "DELETE FROM Question_Answer WHERE answerID=%s AND questionID IN (SELECT questionID From Question_Answer WHRE answerID=%s)"
                values  = (c_node['id'], c_node['id'])
                if (debug): print("    -> [?] = '" + sql + ", " + str(values))
                modules.utils.db_execute_update_insert(mysql, sql, values)
                # Add new updated link
                sql     = "INSERT INTO Question_Answer (questionID, answerID) VALUES (%s, %s)"
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
        cursor.execute("SELECT answer_id, answer FROM View_Question_Answer WHERE question_id=%s", question['id'])
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
            cursor.execute("SELECT child_id, question, questionOrder, ontrigger FROM View_Question_Childs WHERE parent_id=%s AND ontrigger=%s", (question['id'], child['id']))
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
        # 3.1. Store it!
        if (len(res) != 0):
            for row in res:
                s_question = {"id": row[0], "name": row[1],"type": "question","order": row[2],"trigger": row[3], "children": []}
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
 
