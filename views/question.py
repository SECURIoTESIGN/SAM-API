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
import modules.error_handlers, modules.utils # SAM's modules
import views.user, views.answer, views.module # SAM's views

"""
[Summary]: Adds a new question to the database.
[Returns]: Response result.
"""
@app.route('/api/question', methods=['POST'])
def add_question():
    DEBUG=True
    if request.method != 'POST': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"content", "description"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    

    content     = json_data['content']
    description = json_data['description']
    createdon   = "createdon" in json_data and json_data['createdon'] or None
    updatedon   = "updatedon" in json_data and json_data['updatedon'] or None
    
    # Build the SQL instruction using our handy function to build sql instructions.
    values = (content, description, createdon, updatedon)
    sql, values = modules.utils.build_sql_instruction("INSERT INTO Question", ["content", "description", createdon and "createdon" or None, updatedon and "updatedon" or None], values)
    if (DEBUG): print("[SAM-API]: [POST]/api/question - " + sql)

    # Add
    n_id = modules.utils.db_execute_update_insert(mysql, sql, values)
    if (n_id is None):
        return(modules.utils.build_response_json(request.path, 400))  
    else:
        return(modules.utils.build_response_json(request.path, 200, {"id": n_id}))  


"""
[Summary]: Delete a question
[Returns]: Returns a success or error response
"""
@app.route('/api/question/<ID>', methods=["DELETE"])
def delete_question(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'DELETE': return
    
    # 1. Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # 2. Connect to the database and delete the resource
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("DELETE FROM Question WHERE ID=%s", ID)
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 3. The Delete request was a success, the user 'took the blue pill'.
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)

"""
[Summary]: Updates a question.
[Returns]: Response result.
"""
@app.route('/api/question', methods=['PUT'])
def update_question():
    DEBUG=True
    if request.method != 'PUT': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"id"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    

    content     = "content"     in json_data and json_data['content'] or None
    description = "description" in json_data and json_data['description'] or None
    createdon   = "createdon"   in json_data and json_data['createdon'] or None
    updatedon   = "updatedon"   in json_data and json_data['updatedon'] or None

    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Build the SQL instruction using our handy function to build sql instructions.
    values  = (content, description, createdon, updatedon)
    columns = [content and "content" or None, description and "description" or None, createdon and "createdon" or None, updatedon and "updatedOn" or None]
    where   = "WHERE id="+str(json_data['id'])
    # Check if there is anything to update (i.e. frontend developer has not sent any values to update).
    if (len(values) == 0): return(modules.utils.build_response_json(request.path, 200))   

    sql, values = modules.utils.build_sql_instruction("UPDATE Question", columns, values, where)
    if (DEBUG): print("[SAM-API]: [PUT]/api/question - " + sql + " " + str(values))

    # Update Recommendation
    modules.utils.db_execute_update_insert(mysql, sql, values)

    return(modules.utils.build_response_json(request.path, 200))   

"""
[Summary]: Get Questions.
[Returns]: Response result.
"""
@app.route('/api/questions')
def get_questions():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT id, content, description, createdOn, updatedOn FROM Question")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']      = row[0]
            data['content'] = row[1]
            data['description'] = row[2]
            data['type']    = 'question'
            data['modules'] = find_modules_of_question(data['id'])
            data['createdon']   = row[3]
            data['updatedon']   = row[4]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200, datas)) 

"""
[Summary]: Finds the list of modules linked to a question
[Returns]: A list of modules or an empty array if None are found.
"""
def find_modules_of_question(question_id):
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT module_id FROM View_Module_Question WHERE question_id=%s", question_id)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        # Check if this question is a child of another question, triggered by an answer, were the parent belongs to a module.
        # We need to do this because sub-questions, triggered by an answer, are not directly linked to a module. 
        # In order to find the module that the sub-question belongs, we need to find its parent.
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT parent FROM Question_has_Child WHERE child=%s", question_id)
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
        if (len(res) == 0):
            cursor.close()
            conn.close()
            return([]) 
        else:
            l_modules = []
            for row in res:
                modules = find_modules_of_question(row[0])
                l_modules.append(modules)
            #
            f_list_modules = []
            for modules in l_modules:
                for module in modules:
                    if module not in f_list_modules:
                        f_list_modules.append(module)
            return(f_list_modules)
            cursor.close()
            conn.close()
    else:
        modules = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            module = views.module.find_module(row[0], True)[0]
            del module['tree']
            del module['dependencies']
            del module['recommendations']
            modules.append(module)
        cursor.close()
        conn.close()
       
        # 'May the Force be with you, young master'.
        return(modules)

"""
[Summary]: Finds Question.
[Returns]: Response result.
"""
@app.route('/api/question/<ID>', methods=['GET'])
def find_question(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID as question_id, content, description, createdOn, updatedOn FROM Question WHERE ID=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']      = row[0]
            data['content'] = row[1]
            data['type']    = 'question'
            datas.append(data)
        cursor.close()
        conn.close()
        
        # 3. 'May the Force be with you, young master'.
        if (not internal_call): 
            return(modules.utils.build_response_json(request.path, 200, datas)) 
        else:
            return(datas)

"""
[Summary]: Finds Answers of a Question by question ID ans answerID- [Question_Answer] Table.
[Returns]: Response result.
"""
@app.route('/api/question/<question_id>/answer/<answer_id>', methods=['GET'])
def find_question_answers_2(question_id, answer_id, internal_call=False):
    if (request.method != 'GET' and not internal_call): return

    
    # 1. Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT question_answer_id, question_id, question, answer_id, answer FROM View_Question_Answer where question_id=%s and answer_id=%s", (question_id, answer_id))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
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
            data['question_answer_id']  = row[0]
            data['question_id']         = row[1]
            data['question_content']    = row[2]
            data['answer_id']           = row[3]
            data['answer_content']      = row[4]
            datas.append(data)
        cursor.close()
        conn.close()
        
        # 3. 'May the Force be with you, young master'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, datas))
        else:
            return(datas)

"""
[Summary]: Finds Answers of a Question - [Question_Answer] Table.
[Returns]: Response result.
"""
@app.route('/api/question/<ID>/answers', methods=['GET'])
def find_question_answers(ID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT question_answer_id, question_id, question, answer_id, answer FROM View_Question_Answer where question_id=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['question_answer_id']  = row[0]
            data['question_id']         = row[1]
            data['question_content']    = row[2]
            data['answer_id']           = row[3]
            data['answer_content']      = row[4]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200, datas))    


"""
[Summary]: Gets Answers of a Questions - [Question_Answer] Table.
[Returns]: Response result.
"""
@app.route('/api/questions/answers', methods=['GET'])
def get_questions_answers():
   
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the questions from the database 
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT question_answer_id, question_id, question, answer_id, answer FROM View_Question_Answer")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['question_answer_id']  = row[0]
            data['question_id']         = row[1]
            data['question_content']    = row[2]
            data['answer_id']           = row[3]
            data['answer_content']      = row[4]
            datas.append(data)
    
    cursor.close()
    conn.close()
    # 3. 'May the Force be with you, young master'.
    return(modules.utils.build_response_json(request.path, 200, datas))    
