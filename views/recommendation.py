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
import views.user # SAM's views

"""
[Summary]: Adds a new recommendation to the database.
[Returns]: Response result.
"""
@app.route('/recommendation', methods=['POST'])
def add_recommendation(internal_json=None):
    DEBUG=False
    if (internal_json is None):
        if (request.method != 'POST'): return
    
    # Check if the user has permissions to access this resource
    if (internal_json is None): views.user.isAuthenticated(request)
   
    if (internal_json is None):
        json_data = request.get_json()
    else:
        json_data = internal_json

    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): 
        if (internal_json is None):
            return(modules.utils.build_response_json(request.path, 400)) 
        else:
            return(None)
    
    # Validate if the necessary data is on the provided JSON
    # Check if the recommendation [id] is null. If not null, it means the module was previsoulyed added and we just need to add the question_answers mapping to table [recommendation_question_answer].
    if (json_data['id'] is None):
        if (not modules.utils.valid_json(json_data, {"content", "description"})):
            raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    
        
        content         = json_data['content']
        description     = json_data['description']
        guide           = "guide"     in json_data and json_data['guide']     or None
        createdon       = "createdon" in json_data and json_data['createdon'] or None
        updatedon       = "updatedon" in json_data and json_data['updatedon'] or None
    
        # Build the SQL instruction using our handy function to build sql instructions.
        values = (content, description, guide, createdon, updatedon)
        sql, values = modules.utils.build_sql_instruction("INSERT INTO Recommendation", ["content", "description", guide and "guidefilename" or None, createdon and "createdon" or None, updatedon and "updatedon" or None], values)
        if (DEBUG): print("[SAM-API]: [POST]/recomendation - " + sql + " " + str(values))

        # Add
        recommendation_id = modules.utils.db_execute_update_insert(mysql, sql, values)
        if (recommendation_id is None): 
            if (internal_json is None):
                return(modules.utils.build_response_json(request.path, 400))  
            else:
                return("None")
    else:
        recommendation_id = json_data['id']
 
    # This recommendation is given if a question answer association is defined.
    # question_answer_id is a column in table "Recommendation_Question_Answer"
    questions_answers = "questions_answers" in json_data and json_data['questions_answers'] or None
    if (questions_answers is None): 
        if (internal_json is None):
            return(modules.utils.build_response_json(request.path, 200, {"id": recommendation_id}))   
        else:
            return({"id": recommendation_id})
    
    # Build the SQL instruction using our handy function to build sql instructions.
    for question_answer in questions_answers: 
        question_answer_id = question_answer['id']
        columns = ["recommendationID", "questionAnswerID"] 
        values  = (recommendation_id, question_answer_id)
        sql, values = modules.utils.build_sql_instruction("INSERT INTO Recommendation_Question_Answer", columns, values)
        if (DEBUG): print("[SAM-API]: [POST]/recomendation - " + sql + " " + str(values))
        # Add
        rqa_id = modules.utils.db_execute_update_insert(mysql, sql, values)

    if (rqa_id is None):
        if (internal_json is None):
            return(modules.utils.build_response_json(request.path, 400))
        else:
            return(None)
    else:
        if (internal_json is None):
            return(modules.utils.build_response_json(request.path, 200, {"id": recommendation_id}))   
        else:
            return({"id", recommendation_id})
"""
[Summary]: Updates a recommendation
[Returns]: Response result.
"""
@app.route('/recommendation', methods=['PUT'])
def update_recommendation():
    DEBUG=False
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
    guide       = "guide"       in json_data and json_data['guide']     or None
    createdon   = "createdon"   in json_data and json_data['createdon'] or None
    updatedon   = "updatedon"   in json_data and json_data['updatedon'] or None

    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Build the SQL instruction using our handy function to build sql instructions.
    values  = (content, description, guide, createdon, updatedon)
    columns = [content and "content" or None, description and "description" or None, guide and "guideFileName" or None, createdon and "createdon" or None, updatedon and "updatedOn" or None]
    where   = "WHERE id="+str(json_data['id'])
    # Check if there is anything to update (i.e. frontend developer has not sent any values to update).
    if (len(values) == 0): return(modules.utils.build_response_json(request.path, 200))   

    sql, values = modules.utils.build_sql_instruction("UPDATE Recommendation", columns, values, where)
    if (DEBUG): print("[SAM-API]: [PUT]/recomendation - " + sql + " " + str(values))

    # Update Recommendation
    modules.utils.db_execute_update_insert(mysql, sql, values)

    return(modules.utils.build_response_json(request.path, 200))   

"""
[Summary]: Get recommendations.
[Returns]: Response result.
"""
@app.route('/recommendations', methods=['GET'])
def get_recommendations(internal_call=False):
    if (not internal_call): 
        if request.method != 'GET': return
    # 1. Check if the user has permissions to access this resource
    if (not internal_call): 
        views.user.isAuthenticated(request)

    # 2. Let's get the set of available recommendations
    results = []
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, content, description, guideFileName, createdon, updatedon FROM Recommendation")
        res = cursor.fetchall()
        for row in res:
            result = {}
            result['id']          = row[0]
            result['content']     = row[1]
            result['description'] = row[2]
            result['guide']       = row[3]
            result['createdOn']   = row[4]
            result['updatedOn']   = row[5]
            results.append(result)
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()
        # 3. The request was a success, the user 'is in the rabbit hole'
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, results))
        else:
            return(results)

"""
[Summary]: Finds recommendation by ID.
[Returns]: Response result.
"""
@app.route('/recommendation/<ID>', methods=['GET'])
def find_recommendation(ID, internal_call=False):
    if (not internal_call): 
        if request.method != 'GET': return
    # 1. Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # 2. Let's get the set of available recommendations
    results = []
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, content, description, guideFileName, createdon, updatedon FROM Recommendation WHERE ID=%s", ID)
        res = cursor.fetchall()
        for row in res:
            result = {}
            result['id']          = row[0]
            result['content']     = row[1]
            result['description'] = row[2]
            result['guide']       = row[3]
            result['createdOn']   = row[4]
            result['updatedOn']   = row[5]
            results.append(result)
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()
        
        # 3. The request was a success, the user 'is in the rabbit hole'
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, results)) 
        else:
            return(results)
"""
[Summary]: Finds the recommendations of question, answer association.
[Returns]: Response result.
"""
@app.route('/recommendations/question/<question_id>/answer/<answer_id>', methods=['GET'])
def find_recommendations_of_question_answer(question_id, answer_id, internal_call=False):
    if request.method != 'GET': return
    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)
    
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT recommendation_id as id, content, description, guide, createdon, updatedon FROM View_Question_Answer_Recommendation WHERE question_id = %s AND answer_id = %s", (question_id, answer_id))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 

    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(None)    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']          = row[0]
            data['content']     = row[1]
            data['description'] = row[2]
            data['guide']       = row[3] 
            data['type']        = "recommendation"
            data['children']    = []
            data['createdon']   = row[4]
            data['updatedon']   = row[5]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        if (internal_call):
            return(datas)
        else:
            return(modules.utils.build_response_json(request.path, 200, datas)) 

"""
[Summary]: Finds the recommendations of a module
[Returns]: Response result.
"""
@app.route('/recommendations/module/<module_id>', methods=['GET'])
def find_recommendations_of_module(module_id, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': 
            return
    
    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)
    
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT recommendation_ID, recommendation_content, createdon, updatedon FROM View_Module_Recommendations WHERE module_id=%s", module_id)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 

    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(None)    
    else:
        recommendations = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            recommendation = {}
            recommendation['id']                  = row[0]
            recommendation['content']             = row[1]
            recommendation['createdon']           = row[2]
            recommendation['updatedon']           = row[3]
            recommendations.append(recommendation)
    
    # Find questions and answers associated or mapped to a particular recommendation and module
    for recommendation in recommendations:
        recommendation_id = recommendation['id']
        try:
            cursor  = conn.cursor()
            cursor.execute("SELECT recommendation_question_answer_id, question_id, answer_id, createdon, updatedon FROM View_Module_Recommendations_Questions_Answers WHERE module_id=%s and recommendation_id=%s", (module_id, recommendation_id))
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        if (len(res) != 0):
            questions_answers = []
            for row in res:
                question_answer = {}
                question_answer['id']          = row[0]
                question_answer['question_id'] = row[1]
                question_answer['answer_id']   = row[2]
                question_answer['createdon']   = row[3]
                question_answer['updatedon']   = row[4]
                questions_answers.append(question_answer)
            cursor.close()
            recommendation['questions_answers'] = questions_answers
    
    # 'May the Force be with you, young master'.
    conn.close()
    if (internal_call):
        return(recommendations)
    else:
        return(modules.utils.build_response_json(request.path, 200, recommendations)) 


"""
[Summary]: Removes the mapping between a module and its recommendations.
[Returns]: Returns a reponse object.
"""
@app.route('/recommendations/module/<module_id>', methods=['DELETE'])
def remove_recommendations_of_module(module_id, internal_call=False):
    if not internal_call:
        if request.method != 'DELETE': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)
   
    # 2. Connect to the database and delete the resource
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("DELETE FROM recommendation_question_answer WHERE ID IN (SELECT recommendation_question_answer_ID From View_Module_Recommendations_Questions_Answers where module_id=%s);", module_id)
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()
    
    # The Delete request was a success, the user 'took the blue pill'.
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)


"""
[Summary]: Removes the mapping of a module and a recommendation.
[Returns]: Returns a reponse object.
"""
@app.route('/recommendation/<recommendation_id>/module/<module_id>', methods=['DELETE'])
def remove_recommendation_of_module(recommendation_id, module_id, internal_call=False):
    if not internal_call:
        if request.method != 'DELETE': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)
   
    # 2. Connect to the database and delete the resource
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("DELETE FROM recommendation_question_answer WHERE ID IN (SELECT recommendation_question_answer_ID From View_Module_Recommendations_Questions_Answers where module_id=%s AND recommendation_id=%s);", (module_id, recommendation_id))
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()
    
    # The Delete request was a success, the user 'took the blue pill'.
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)

