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
from api import app, mysql, JWT_SECRET_TOKEN, JWT_EXPIRATION_SECONDS
from datetime import datetime
from configparser import SafeConfigParser
from flask import Flask, abort, request, jsonify, render_template, redirect, url_for, request
from flaskext.mysql import MySQL
from flasgger import Swagger
from flasgger.utils import swag_from
from jsonschema import validate
from datetime import timedelta

import views.user #SAM's views


"""
[Summary]: Check if the user has the necessary permissions to access a service.
[Returns]: True if access is granted to access the resource, false otherwise.
[ref]: CHECK THIS: https://medium.com/devgorilla/how-to-log-out-when-using-jwt-a8c7823e8a6
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
        # Decode will raise an exception if anything goes wrong within the decoding process (i.e., perform validation of the JWT).
        res_dic  = jwt.decode(parsedToken, JWT_SECRET_TOKEN, algorithms=['HS256'])
        # Get the ID of the user.
        userID = int(res_dic['ID'])
        # Debug only: print(str(json.dumps(res_dic)))
       
        conn    = mysql.connect()
        cursor  = conn.cursor()
        # 3.1. Check if the token is not blacklisted, that is if a user was previously logged out from the platform but the token is still 'alive'.
        cursor.execute("SELECT ID FROM Auth_Token_Blacklist WHERE userID=%s AND token=%s", (userID, parsedToken))
        res = cursor.fetchall()
        if (len(res) == 1):
            raise modules.error_handlers.BadRequest(request.path, "Authentication failure - You don't have the necessary permissions to access this resource. Please, provide an authorization token.", 403) 
        cursor.close()
        cursor  = conn.cursor()

        # 3.2. Get info of the user
        # Check if this user id exists.
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
            # Set the expiration time of the token, the JWT auth token will not be valid after x seconds
            # Default is a 15 minute session
            data['exp']     = datetime.utcnow() + timedelta(seconds=int(JWT_EXPIRATION_SECONDS))

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


"""
[Summary]: Clear the list of expired blacklisted JSON Web Tokens of a user.
[Arguments]:
       - $userID$: Target user.
[Returns]: Returns false, if an error occurs, true otherwise. 
"""
def clear_expired_blacklisted_JWT(userID):
    debug=True
    if (debug): print("Checking blacklisted tokens for user id ="+str(userID))
    try:
        # Check if this user id exists.
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT token FROM Auth_Token_BlackList WHERE userID=%s", userID)
        res = cursor.fetchall()
    except Exception as e:
        if (debug): print(str(e))
        return (False) # 'Houston, we have a problem.'
    # Empty results ?
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return (True)
    else:
        i=0
        for row in res: 
            token = row[0]
            if (debug): print ("# Checking token[" + str(i) + "]" + "= " + token)
            i = i + 1
            try:
                # Let's see if the token is expired
                res_dic  = jwt.verify(token)
                if (debug): print(" - The token is still 'alive'. Nothing to do here.")
            except:
                if (debug): print(" - The token is expired, removing it from the database for user with id " + str(userID))
                # The token is expired, remove it from the DB
                try:
                    cursor.execute("DELETE FROM Auth_Token_Blacklist WHERE token=%s AND userID=%s", (token,userID))
                    conn.commit()
                except Exception as e:
                    if (debug): print(str(e))
                    return (False) # 'Houston, we have a problem.'
    return(True)

"""
[Summary]: Performs a logout using an JWT authentication token.
[Returns]: 200 response if the user was successfully logged out.
[ref]: Based on https://medium.com/devgorilla/how-to-log-out-when-using-jwt-a8c7823e8a6
"""
@app.route('/user/logout', methods=['POST'])
def logout():
    data = {}
    if request.method != "POST": return
    # 1. Check if the token is available on the request header.
    headers = dict(request.headers)
    # Debug only: print(str(len(headers)))
    
    # 2. Check if the Authorization header name was parsed.
    if 'Authorization' not in headers: raise modules.error_handlers.BadRequest(request.path, "Authentication failure - You don't have the permission to access this resource. Please, provide an authorization token.", 403) 
    parsedToken = headers['Authorization']
    print("Parsed Token:" + parsedToken)
    
    try:
        # 3. From now on the token will be blacklisted because the user has logout and the token may still
        #    exists somewhere because its expiration date is still valid.
        
        # 3.1. Let's clean the house - Remove possible expired tokens from the user of the token
        res_dic  = jwt.decode(parsedToken, JWT_SECRET_TOKEN, algorithms=['HS256'])
       
        userID = int(res_dic['ID'])
        if not clear_expired_blacklisted_JWT(userID): # Sanity check
            return (modules.utils.build_response_json(request.path, 500))
        # 3.2. Let's add the token to the blacklist table on the database for the current user
        #      That is, blacklist the current token, that may or may not be alive. 
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO Auth_Token_Blacklist (userID, token) VALUES (%s, %s)", (userID, parsedToken))
        conn.commit()
        data['message'] = "The authentication token was blacklisted."
       
    except jwt.exceptions.ExpiredSignatureError as e:
        # We don't need to blacklist this token, the token is already expired (see 'exp' field of the JWT defined in the authenticate function).
        # raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
        data['message'] = "The token has already expired, no need to blacklist it."
        return (modules.utils.build_response_json(request.path, 200, data))
    except Exception as e :
        # Double token entry ?
        if e.args[0] == 1062:
            data['message'] = "The token was already blacklisted."
        else:
            raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass # cursor or conn may not be defined, I don't care, 'Just keep swimming'.
    #
    return (modules.utils.build_response_json(request.path, 200, data))
