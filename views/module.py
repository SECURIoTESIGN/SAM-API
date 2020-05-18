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
import views.authentication # SAM's views

"""
[Summary]: Get all modules.
[Returns]: Returns a set of modules.
"""
@app.route('/modules', methods=['GET'])
def getModules():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)

    # 2. Let's get the modules from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, shortName, fullname, displayname FROM Module")
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
            data['ID']          = row[0]
            data['shortName']   = row[1]
            data['fullname']    = row[2]
            data['displayName'] = row[3]
            datas.append(data)

        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young padawan'.
        return(modules.utils.build_response_json(request.path, 200, datas))    

"""
[Summary]: Get answers of a question ID
[Arguments]:
    - $ID$: The id of question. 
[Returns]: Returns the answers of a question
"""
@app.route('/module/question/<ID>', methods=['GET'])
def getAnswers(ID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT answer_id, answer FROM view_question_answer WHERE question_id = %s", ID)
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
            data['ID']          = row[0]
            data['answer']    = row[1]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200, datas))    

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
def getAllChilds(initial, c_childs, question, question_js={}):
    childs = []
    # 1. Get childrens of question
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        
        cursor.execute("SELECT child_id, question, questionOrder, ontrigger FROM View_Question_Childs WHERE parent_id=%s", question['ID'])
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 1.2. Check of empty results
    if (len(res) != 0):
        for row in res:
            child = {
                "ID": row[0], 
                "content": row[1],
                "order": row[2],
                "trigger": row[3]
            }
            childs.append(child)
    cursor.close()
    cursor  = conn.cursor()

    # 2. Get, if available, answers of each child found in 1.
    for child in childs:
        try:
            cursor.execute("SELECT answer_id, answer FROM View_Question_Answer WHERE question_id=%s", child['ID'])
            res = cursor.fetchall()
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500)
        
        if (len(res) != 0):
            answers = []
            for row in res:
                answer = { "ID": row[0], "content": row[1] }
                answers.append(answer)    
            child.update({"answers": answers})

    cursor.close()
    conn.close()

    # 3. Check if the current question has children; IF not, return.
    #    This is the illusive break/return condition of this recursive function - 'Elementary, my dear Watson.'
    if (len(childs) == 0): return None
    
    # 4. Recursive calls and python JSON object construction
    for child in childs:
        if (initial == True): 
            question_js = child
            getAllChilds(False, c_childs, child, question_js)
            c_childs.append(question_js)
        else:
            nn = child
            question_js.update({"childs": nn})
            getAllChilds(False, c_childs, child, nn)
            
"""
[Summary]: Get Questions and answers of a given module.
[Arguments]:
    - $ID$: ID of the module.
[Returns]: A set of questions, its children, and its answers.
"""
@app.route('/module/<ID>', methods=['GET'])
def getQuestions(ID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)

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
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        # 2.2.1. The initial set of the information about the module.
        for row in res: 
            data = {"ID": row[0], "name": row[1]}
            break
        # 2.2.2. Map questions of the module to a JSON Python Object (dic).
        questions = []
        for row in res:
            question = {"ID": row[2], "content": row[3], "order": row[4]}
            questions.append(question)
        data.update({"questions":  questions})

        cursor.close()
        conn.close()
    
    # 3. Let's get the answers of each, previously found, question.
    for question in data['questions']:
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT answer_id, answer FROM View_Question_Answer WHERE question_id = %s", question['ID'])
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
                answer = { "ID": row[0], "content": row[1]}
                answers.append(answer)
            question.update({"answers": answers})
        if (conn.open):
            cursor.close()
            conn.close()

    # 4. Recursively get each question child and corresponding data (question, answer, and so on).
    for question in data['questions']: 
        childs = []
        getAllChilds(True, childs, question)
        # 4.1. Update the current question JSON python object (dic) with childs (i.e., sub-questions).
        question.update({"childs": childs})
        
    # 5. 'May the Force be with you'.
    return(modules.utils.build_response_json(request.path, 200, data))
