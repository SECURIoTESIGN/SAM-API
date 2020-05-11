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
[Summary]: Returns info about a session
[Arguments]:
    - $email$: ID of the module.
    - $moduleID$: ID of the module.
[Returns]: Returns an array of JSON Objects containing information about each session. 
"""
@app.route('/session/<email>/<moduleID>', methods=['GET'])
def getSession(email, moduleID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)

    # 2. Let's existing sessions from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, userID, moduleID, ended, createdOn, updatedOn FROM Session WHERE userID=(SELECT ID FROM User WHERE email=%s) AND moduleID=%s", (email, moduleID))
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
            data['userID']      = row[1]
            data['moduleID']    = row[2]
            data['ended']       = row[3]
            data['createdOn']   = row[4]
            data['updatedOn']   = row[5]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you'.
        return(modules.utils.build_response_json(request.path, 200, datas))    


"""
[Summary]: Start a new session to a user.
[Returns]: Response result
"""
@app.route('/session', methods=['POST'])
def startSession():
    if request.method != 'POST': return

    # 1. Check if the user has permissions to access this resource.
    views.authentication.isAuthenticated(request)

    # 2. Let's get our shiny new JSON object
    #    Always start by validating the structure of the json, if not valid send an invalid response.
    try:
        obj = request.json
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 

    # 3. Let's validate the data of our JSON object with a custom function.
    if (not modules.utils.valid_json(obj, {"email", "moduleID"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)

    # 4. Check if there is an identical session opened, if true, return.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, userID, moduleID, ended, createdOn, updatedOn FROM Session WHERE userID=(SELECT ID FROM User WHERE email=%s) AND moduleID=%s", (obj['email'], obj['moduleID']))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    if (len(res) != 0):
        raise modules.error_handlers.BadRequest(request.path, "This session was already created and is still opened.", 409) 
    
    # 5. Connect to the database and add a new session.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO SESSION (userID, moduleID) VALUES ((SELECT ID FROM User WHERE email=%s), %s)", (obj['email'],obj['moduleID']))
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 6. The request was a success, the user 'took the blue pill'.
    return (modules.utils.build_response_json(request.path, 200))
    