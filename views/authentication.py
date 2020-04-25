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
from api import app, mysql, JWT_SECRET_TOKEN
import time, json, jwt, os, urllib
import modules.error_handlers, modules.utils # Import our new and shiny custom SAM's modules
from datetime import datetime
from configparser import SafeConfigParser
from flask import Flask, abort, request, jsonify, render_template, redirect, url_for, request
from flaskext.mysql import MySQL
from flasgger import Swagger
from flasgger.utils import swag_from
from jsonschema import validate
# Import our SAM's views at predefined routes
import views.user

"""
[Summary]: Check if the user has the necessary permissions (e.g., authenticated) to access SAM's services
[Returns]: True if access to a resource is approved, false otherwise.
"""
def isAuthenticated(request):
    # Get the token from the parse request headers
    headers = dict(request.headers)
    print(str(len(headers)))
    # Check if the Authorization header name was parsed to the service
    if 'Authorization' not in headers: raise modules.error_handlers.BadRequest(request.path, "Authentication failure - You don't have the permission to access the requested resource", 403) 
    parsedToken = headers['Authorization']

    # Decode the parsed Token
    try:
        res_dic  = jwt.decode(parsedToken, JWT_SECRET_TOKEN, algorithms=['HS256'])
        # Get the ID of the user embedded on the token 
        userID = int(res_dic['User']['ID'])
        # Check if the user id exists on the database
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID FROM User WHERE id=%s", userID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 403) 

    if (len(res) == 1): 
        return True # The user is legit, we can let him access the target resource 
    else:
        raise modules.error_handlers.BadRequest(request.path, "Authentication failure - You don't have the permission to access the requested resource", 403) 

"""
[Summary]: User Authentication Service for login proposes.
[Returns]: Returns a JSON object with the data of the user including a JWT token.
"""
@app.route('/user/login', methods=['POST'])
def authenticate():
    if request.method == "POST":
        # Validate and parse POST data
        if not request.form.get('email'):
            raise modules.error_handlers.BadRequest(request.path, 'The email cannot be empty', 400) 
        if not request.form.get('psw'):
            raise modules.error_handlers.BadRequest(request.path, 'The password cannot be empty', 400) 
        #
        email   = request.form['email']
        psw     = request.form['psw']
        # Connecting to the DB 
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT ID, email, psw, avatar FROM User WHERE email=%s", email)
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
        # Evalute DB and if != none parse results
        if (cursor.rowcount == 0): 
            raise modules.error_handlers.BadRequest(request.path, "A user with the specified email was not found", 404) 
        # Lets get the amazing results returned by the DB
        records = cursor.fetchall()
        dbpsw = ""
        data = {} # Create a new nice empty dictionary to be populated with data from the DB
        for row in records:
            data['ID']      = row[0]
            data['email']   = row[1]
            dbpsw           = row[2] # For security reasons lets not store this in the dic
            data['avatar']  = row[3]

        if modules.utils.check_password(dbpsw, psw):
            # IF the hash password of the database is the same as the one provided by the user
            # Build the authentication token and added to newly created dic
            data['token'] = str(jwt.encode(data, JWT_SECRET_TOKEN, algorithm='HS256'))
            # Creates a JSON response with the data of the dictionary 
            return (modules.utils.build_response_json(request.path, 200, data))
        else:
            raise modules.error_handlers.BadRequest(request.path, "Authentication failure", 401) 

@app.route('/user', methods=['POST'])
def register():
    # 1. Lets get our shiny new JSON object and current time
    # Always start by validating the structure of the json, if not valid send an invalid response
    try:
        obj = request.json
        date = (datetime.now()).strftime('%Y-%m-%d %H:%M:%S')
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 

    # 2. Lets validate the data of our JSON object with a custom function
    if (not modules.utils.valid_json(obj, {"email", "psw"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)

    # 3. Lets hash the hell of the password
    hashed_psw = modules.utils.hash_password(obj['psw'])
    obj['psw'] = "" # clearing the user's plain text password parsed through https
    
    # 4. Check if the user is not already registered
    if (views.user.getUser(obj['email']) is not None):
        raise modules.error_handlers.BadRequest(request.path, "The user with that email already exists", 500)

    # 4. Connect to the database and create the new user
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO User (email, psw, avatar, createdon, updatedon) VALUES (%s, %s, %s, %s, %s)", (obj['email'], hashed_psw, obj['avatar'], date, date))
        #conn.commit()
    except Exception as e:
        print(str(e))
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    return (modules.utils.build_response_json(request.path, 200))