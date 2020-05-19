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
[Summary]: Gets the set of available recommendations.
[Returns]: Response result.
"""
@app.route('/recommendations', methods=['GET'])
def getRecommendations():
    if request.method != 'GET': return
    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)

    # 2. Let's get the set of available recommendations
    results = []
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, content, description, guideFileName, createdon, updatedon FROM Recommendation")
        res = cursor.fetchall()
        for row in res:
            result = {}
            result['ID']          = row[0]
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
        return(modules.utils.build_response_json(request.path, 200, results))   

"""
[Summary]: Adds a recommendation to a session based on one or more answers given. 
[Returns]: Response result.
"""
@app.route('/recommendation/<ID_r>/session/<ID_s>', methods=['GET'])
def addRecomendation(ID_r, ID_s):
    if request.method != 'GET': return
    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO Session_Recommendation (sessionID, recommendationID) VALUES (%s, %s)", (ID_s, ID_r))
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 5. The Update request was a success, the user 'is in the rabbit hole'
    return (modules.utils.build_response_json(request.path, 200))

