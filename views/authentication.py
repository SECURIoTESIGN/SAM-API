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
import time, json, jwt, os, urllib
import modules.error_handlers, modules.utils # SAM's modules
from api import app, mysql, JWT_SECRET_TOKEN
from datetime import datetime
from configparser import SafeConfigParser
from flask import Flask, abort, request, jsonify, render_template, redirect, url_for, request
from flaskext.mysql import MySQL
from flasgger import Swagger
from flasgger.utils import swag_from
from jsonschema import validate
import views.user #SAM's views

"""
[Summary]: Check if the user has the necessary permissions to access a service.
[Returns]: True if access is granted to access the resource, false otherwise.
"""
def isAuthenticated(request):
    # 1. Check if the token is available on the request header.
    headers = dict(request.headers)
    # Debug only: print(str(len(headers)))
    
    # 2. Check if the Authorization header name was parsed.
    if 'Authorization' not in headers: raise modules.error_handlers.BadRequest(request.path, "Authentication failure - You don't have the permission to access this resource. Please, provide an authorization token.", 403) 
    parsedToken = headers['Authorization']
    # print("Parsed Token:" + parsedToken)

    # 3. Decode the authorization token to get the User object.
    try:
        res_dic  = jwt.decode(parsedToken, JWT_SECRET_TOKEN, algorithms=['HS256'])
        # debug only: print(str(json.dumps(res_dic)))
        # Get the ID of the user.
        userID = int(res_dic['ID'])
        # Check if this user id exists.
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID FROM User WHERE id=%s", userID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 403) 

    if (len(res) == 1): 
        cursor.close()
        conn.close()    
        return True # The user is legit, we can let him access the target resource 
    else:
        cursor.close()
        conn.close()    
        raise modules.error_handlers.BadRequest(request.path, "Authentication failure - You don't have the necessary permissions to access this resource. Please, provide an authorization token.", 403) 

"""
[Summary]: User Authentication Service (i.e., login).
[Returns]: Returns a JSON object with the data of the user including a JWT authentication token.
"""
@app.route('/user/login', methods=['POST'])
def authenticate():
    if request.method == "POST":
        # 1. Validate and parse POST data.
        if not request.form.get('email'):
            raise modules.error_handlers.BadRequest(request.path, 'The email cannot be empty', 400) 
        if not request.form.get('psw'):
            raise modules.error_handlers.BadRequest(request.path, 'The password cannot be empty', 400) 
        
        email   = request.form['email']
        psw     = request.form['psw']
        
        # 2. Connect to the DB and get the user info.
        try:
            conn    = mysql.connect()
            cursor  = conn.cursor()
            cursor.execute("SELECT ID, email, psw, avatar FROM User WHERE email=%s", email)
        except Exception as e:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
        # 2.1. Check if the user exists.
        if (cursor.rowcount == 0): 
            raise modules.error_handlers.BadRequest(request.path, "A user with the specified email was not found", 404) 
        
        # 2.2. Process the DB results.
        records = cursor.fetchall()
        dbpsw = ""
        data = {} # Create a new nice empty dictionary to be populated with data from the DB.
        for row in records:
            data['ID']      = row[0]
            data['email']   = row[1]
            # For security reasons lets not store the password in the dic.
            dbpsw           = row[2] 
            data['avatar']  = row[3]

        cursor.close()
        conn.close()    
        
        # Check if the hashed password of the database is the same as the one provided by the user.
        if modules.utils.check_password(dbpsw, psw):
            # First, build the authentication token and added it to the dictionary.
            # Second, let's create a JSON response with the data of the dictionary.
            data['token'] = (jwt.encode(data, JWT_SECRET_TOKEN, algorithm='HS256')).decode('UTF-8')
            
            # Authentication success, the user 'can follow the white rabbit'.
            return (modules.utils.build_response_json(request.path, 200, data))
        else:
            raise modules.error_handlers.BadRequest(request.path, "Authentication failure", 401)