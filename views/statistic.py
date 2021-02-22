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
from flask import Flask, request, abort, jsonify, send_from_directory
import os, views.user, modules.utils, views.recommendation, views.module, views.session


"""
[Summary]: Get Global Stats
[Returns]: Response result.
"""
@app.route("/statistics", methods=['GET'])
def get_global_stats():
    stats = {}
    tmp_users = get_stats_user(True)
    tmp_modules = get_stats_modules(True)
    tmp_questions = get_stats_questions(True)
    tmp_answers = get_stats_answers(True)
    tmp_sessions = get_stats_sessions(True)
    tmp_recommendations = get_stats_recommendations(True)

    stats['users']              = tmp_users and tmp_users['size'] or 0
    stats['modules']            = tmp_modules and tmp_modules['size'] or 0
    stats['questions']          = tmp_questions and tmp_questions['size'] or 0
    stats['answers']            = tmp_answers and tmp_answers['size'] or 0
    stats['sessions']           = tmp_sessions and tmp_sessions['size'] or 0
    stats['recommendations']    = tmp_recommendations and tmp_recommendations['size'] or 0

    # 'May the Force be with you.'
    return(modules.utils.build_response_json(request.path, 200, stats)) 

"""
[Summary]: Get the number of users 
[Returns]: Response result.
"""
@app.route("/statistic/users", methods=['GET'])
def get_stats_user(internal_call=False):
    if (not internal_call): 
        if request.method != 'GET': return
    
    # Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticated(request)
    
    # Let's get the info from the databse.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(id) as size FROM User")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)
    else:
        data = {}
        for row in res:
            data['size'] = row[0]
            break
    
    cursor.close()
    conn.close()

    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, data)) 
    else:
        return(data)
"""
[Summary]: Get the number of modules 
[Returns]: Response result.
"""
@app.route("/statistic/modules", methods=['GET'])
def get_stats_modules(internal_call=False):
    if (not internal_call): 
        if request.method != 'GET': return
    
    # Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticated(request)
    
    # Let's get the info from the databse.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        # Top 5 only
        cursor.execute("SELECT moduleID, count(*) as occurrences FROM Session GROUP BY moduleID ORDER BY occurrences DESC LIMIT 5")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)
    else:
        stat = {}
        stat['size'] = get_number_of_modules()
        stat['top'] = []
        for row in res:
            module = views.module.find_module(row[0], True)
            module[0]['occurrences'] = row[1]
            del module[0]["createdon"]
            del module[0]["updatedon"]
            del module[0]["tree"]
            del module[0]["recommendations"]
            del module[0]["logic_filename"]
            del module[0]["description"]
            del module[0]["dependencies"]
            stat['top'].append(module[0])

    cursor.close()
    conn.close()

    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, stat))
    else: 
        return(stat)

def get_number_of_modules():
    size = 0
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(id) as size FROM Module")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(size)    
    else:
        for row in res:
            size = row[0]
            break
    return(size)

"""
[Summary]: Get the number of questions 
[Returns]: Response result.
"""
@app.route("/statistic/questions", methods=['GET'])
def get_stats_questions(internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticated(request)
    
    # Let's get the info from the databse.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(id) as size FROM Question")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None) 
    else:
        data = {}
        for row in res:
            data['size'] = row[0]
            break
    
    cursor.close()
    conn.close()

    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, data))
    else:
        return(data)

"""
[Summary]: Get the number of answers 
[Returns]: Response result.
"""
@app.route("/statistic/answers", methods=['GET'])
def get_stats_answers(internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return
    # Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticated(request)
    
    # Let's get the info from the databse.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(id) as size FROM Answer")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else: 
            return(None)
    else:
        data = {}
        for row in res:
            data['size'] = row[0]
            break
    
    cursor.close()
    conn.close()
    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, data))
    else:
        return(data)

"""
[Summary]: Get the number of recommendations 
[Returns]: Response result.
"""
@app.route("/statistic/recommendations", methods=['GET'])
def get_stats_recommendations(internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return
    # Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticated(request)
    
    # Let's get the info from the databse.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        # Top 5 only
        cursor.execute("SELECT recommendationID, count(*) as occurrences FROM Session_Recommendation GROUP BY recommendationID ORDER BY occurrences DESC LIMIT 5")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)
    else:
        stat = {}
        stat['size'] = get_number_of_recommendations()
        stat['top'] = []
        for row in res:
            recommendation = {}
            recommendation = views.recommendation.find_recommendation(row[0], True)
            del recommendation[0]['description']
            del recommendation[0]['guide']
            del recommendation[0]['createdOn']
            del recommendation[0]['updatedOn']
            recommendation[0]['occurrences'] = row[1]
            stat['top'].append(recommendation[0])

    cursor.close()
    conn.close()
    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, stat))
    else:
        return(stat)

def get_number_of_recommendations():
    size = 0
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(id) as size FROM Recommendation")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(size)    
    else:
        for row in res:
            size = row[0]
            break
    return(size)

"""
[Summary]: Get the number of sessions in the last 7 days.
[Returns]: Response result.
"""
@app.route("/statistic/sessions", methods=['GET'])
def get_stats_sessions(internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return
    # Check if the user has permissions to access this resource
    if (not internal_call):
        views.user.isAuthenticated(request)
    
    # Let's get the info from the databse.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        # Number of session in the Last 7 days sessions
        cursor.execute("SELECT date(createdOn) as day, COUNT(*) as occurrences FROM Session WHERE createdon >= DATE_ADD(CURDATE(), INTERVAL -7 DAY) GROUP BY day")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)   
    else:
        stat = {}
        stat['size'] = get_number_of_sessions()
        stat['top'] = []
        for row in res:
            date = {}
            date['date'] = row[0]
            date['occurrences'] = row[1]
            stat['top'].append(date)

    cursor.close()
    conn.close()

    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, stat))
    else:
        return(stat)

def get_number_of_sessions():
    size = 0
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(id) as size FROM Module")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(size)    
    else:
        for row in res:
            size = row[0]
            break
    return(size)
