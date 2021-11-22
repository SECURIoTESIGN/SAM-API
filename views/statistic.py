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
import views.user, modules.utils, views.recommendation, views.module, views.session


"""
[Summary]: Get Global Stats
[Returns]: Response result.
"""
@app.route("/api/statistics", methods=['GET'])
def get_global_stats():
    if request.method != 'GET': return
    
    views.user.isAuthenticated(request)

    stats = {}
    tmp_users = get_number_of_table('user')
    tmp_modules = get_number_of_table('module')
    tmp_questions = get_number_of_table('question')
    tmp_answers = get_number_of_table('answer')
    tmp_sessions = get_number_of_table('session')
    tmp_recommendations = get_number_of_table('recommendation')

    stats['users']              = tmp_users or 0
    stats['modules']            = tmp_modules or 0
    stats['questions']          = tmp_questions or 0
    stats['answers']            = tmp_answers or 0
    stats['sessions']           = tmp_sessions or 0
    stats['recommendations']    = tmp_recommendations or 0

    # 'May the Force be with you.'
    return(modules.utils.build_response_json(request.path, 200, stats)) 

"""
[Summary]: Get the number of users 
[Returns]: Response result.
"""
@app.route("/api/statistic/users", methods=['GET'])
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
        cursor.execute("SELECT COUNT(id) as size FROM user")
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
@app.route("/api/statistic/modules", methods=['GET'])
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
        cursor.execute("SELECT shortname, displayname, occurrences FROM module, (SELECT moduleID as mID, count(*) as occurrences FROM session GROUP BY moduleID ORDER BY occurrences DESC LIMIT 5) as Top5 WHERE ID = mID")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, {"size":0}))
        else:
            return(None)
    else:
        tot_mod = 0
        stat = {}
        stat['top'] = []
        for row in res:
            module = {}
            module['shortname'] = row[0]
            module['displayname'] = row[1]
            module['occurrences'] = row[2]
            tot_mod += row[2]
            stat['top'].append(module)
        
        stat['size'] = tot_mod

    cursor.close() 
    conn.close()

    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, stat))
    else: 
        print("--->" + stat)
        return(stat)

"""
[Summary]: Get the number of questions 
[Returns]: Response result.
"""
@app.route("/api/statistic/questions", methods=['GET'])
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
        cursor.execute("SELECT COUNT(id) as size FROM question")
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
@app.route("/api/statistic/answers", methods=['GET'])
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
        cursor.execute("SELECT COUNT(id) as size FROM answer")
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
@app.route("/api/statistic/recommendations", methods=['GET'])
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
        cursor.execute("SELECT content, occurrences FROM recommendation, (SELECT recommendationID as rID, count(*) as occurrences FROM session_recommendation GROUP BY recommendationID ORDER BY occurrences DESC LIMIT 5) as Top5 WHERE ID = rID;")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, {"size":0}))
        else:
            return(None)
    else:
        tot_recm = 0
        stat = {}
        stat['top'] = []
        for row in res:
            recommendation = {}
            recommendation['occurrences'] = row[1]
            recommendation['content'] = row[0]
            tot_recm += row[1]
            stat['top'].append(recommendation)
        
        stat['size'] = tot_recm

    cursor.close()
    conn.close()
    # 'May the Force be with you, young master'.
    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200, stat))
    else:
        return(stat)


"""
[Summary]: Get the number of sessions in the last 7 days.
[Returns]: Response result.
"""
@app.route("/api/statistic/sessions", methods=['GET'])
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
        cursor.execute("SELECT date(createdOn) as day, COUNT(*) as occurrences FROM session WHERE createdon >= DATE_ADD(CURDATE(), INTERVAL -7 DAY) GROUP BY day")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, {"size": 0}))
        else:
            return(None)   
    else:
        stat = {}
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


"""
[Summary]: Get the amount of elements in a table. 
[Returns]: Integer.
"""
def get_number_of_table(table_name):
    size = 0
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT COUNT(id) as size FROM "+str(table_name))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    if len(res) != 0:
            size = res[0][0]

    return(size)