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

""" [Summary]: Validates recaptcha response from google server.
    [Returns]: Returns True captcha test passed, false otherwise.
    [TODO]: In a production environment the client and server key should be reconfigured.
"""
def is_human(captcha_response):
    # https://www.google.com/recaptcha/
    secret = "6LcLdO8UAAAAAH3CWKWo2WAtFZazstWy2qjcOHOY"
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']

"""
[Summary]: User Registration Service (i.e., add a new user).
[Returns]: Returns a JSON object with the data of the user including a JWT authentication token.
[TODO]: Check inline comments.
"""
@app.route('/user', methods=['POST'])
def addUser():
    if request.method != 'POST': return

    # 1. Let's get our shiny new JSON object and current time.
    # - Always start by validating the structure of the json, if not valid send an invalid response.
    try:
        obj = request.json
        date = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 

    # 2. Let's validate the data of our JSON object with a custom function.
    if (not modules.utils.valid_json(obj, {"email", "psw", "firstName", "lastName", "avatar", "g-recaptcha-response"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)

    # 3. Validate reCAPTCHA
    if not is_human(obj['g-recaptcha-response']):
        raise modules.error_handlers.BadRequest(request.path, "reCAPTCHA failure - Bots are not allowed.", 400)

    # 4. Let's hash the hell of the password.
    hashed_psw = modules.utils.hash_password(obj['psw'])
    obj['psw'] = "" # "paranoic mode".
    
    # 5. Check if the user was not previously registered in the DB (i.e., same email)
    if (views.user.getUser(obj['email']) is not None):
        raise modules.error_handlers.BadRequest(request.path, "The user with that email already exists", 500)

    # 6. Connect to the database and create the new user.
    # TODO: Let's build procedures in the DB to do this. 
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO User (email, psw, firstName, lastName, avatar, createdon, updatedon) VALUES (%s, %s, %s, %s, %s, %s, %s)", (obj['email'], hashed_psw, obj['firstName'], obj['lastName'], obj['avatar'], date, date))
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 7. Authentication success, the user can now choose to 'take the red or blue pill to follow the white rabbit'
    return (modules.utils.build_response_json(request.path, 200))

"""
[Summary]: Find a user by email.
[Returns]: Returns a User object.
"""
# Check if a user exists
@app.route('/user/<email>', methods=['GET'])
def getUser(email):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)
       
    # 2. Let's validate the email, invalid emails from this point are not allowed.
    try:
        valid = validate_email(email)
    except EmailNotValidError as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 
    
    # 3. Let's get the user from the database with the provided [email].
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, email, firstName, lastName, avatar FROM User WHERE email=%s", email)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Empty results ?
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        data = {} # Create a new nice empty dictionary to be populated with data from the DB.
        for row in res:
            data['ID']          = row[0]
            data['email']       = row[1]
            data['firstName']   = row[2]
            data['lastName']    = row[3]
            data['avatar']      = row[4]
        cursor.close()
        conn.close()
        # 4. Return information about the user (except the password) and 'May the Force be with you'.
        return(modules.utils.build_response_json(request.path, 200, data))    

"""
[Summary]: Delete a user
[Returns]: Returns a success or error response
"""
@app.route('/user/<email>', methods=["DELETE"])
def deleteUser(email):
    if request.method != 'DELETE': return
    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)
  
    # 2. Let's validate the email, invalid emails from this point are not allowed.
    try:
        valid = validate_email(email)
    except EmailNotValidError as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 

    # 3. Connect to the database and delete the user
    # TODO: Let's build procedures in the DB to delete Users. 
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("DELETE FROM User WHERE email=%s", email)
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 4. The Delete request was a success, the user 'took the blue pill'.
    return (modules.utils.build_response_json(request.path, 200))

"""
[Summary]: Updates a user
[Returns]: Returns a success or error response
"""
@app.route('/user/<email>', methods=["PUT"])
def updateUser(email):
    updatePsw = False
    # Note: Remember that if an email is being changed, the email argument is the old one; 
    #       The new email content is available on the JSON object parsed in the body of the request.  
    if request.method != 'PUT': return
    # 1. Check if the user has permissions to access this resource
    views.authentication.isAuthenticated(request)

    # 2. Let's validate the email, invalid emails from this point are not allowed.
    try:
        valid = validate_email(email)
    except EmailNotValidError as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 

    # 3. Let's get our shiny new JSON object and current time.
    # - Always start by validating the structure of the json, if not valid send an invalid response.
    try:
        obj = request.json
        date = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 

    # 4. Let's validate the data of our JSON object with a custom function.
    if (not modules.utils.valid_json(obj, {"email", "avatar", "firstName", "lastName"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)

    # 4.1. Let's also validate the new email, invalid emails from this point are not allowed.
    try:
        valid = validate_email(obj['email'])
    except EmailNotValidError as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 

    # 5. Hash the new password and store it (if supplied)
    if (modules.utils.valid_json(obj, {"psw"})):
        updatePsw=True
        hashed_psw = modules.utils.hash_password(obj['psw'])
        obj['psw'] = "" # "paranoic mode".

    # 6. Connect to the database and update the user with the data of the parsed json object
    # TODO: - Let's build procedures in the DB to update Users. 
    #       - Let's not update every single field of the User, instead, let's just updated the one that has changed.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        if (updatePsw):
            cursor.execute("UPDATE User SET email=%s, psw=%s, firstName=%s, lastName=%s, avatar=%s, updatedOn=%s WHERE email=%s",  (obj['email'], hashed_psw, obj['firstName'], obj['lastName'], obj['avatar'],date,email))
        else:
            cursor.execute("UPDATE User SET email=%s, firstName=%s, lastName=%s, avatar=%s, updatedOn=%s WHERE email=%s",  (obj['email'], obj['firstName'], obj['lastName'], obj['avatar'],date,email))    
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 4. The Update request was a success, the user 'is in the rabbit hole'
    return (modules.utils.build_response_json(request.path, 200))

