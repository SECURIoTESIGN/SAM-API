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
from api import app, mysql, JWT_SECRET_TOKEN, JWT_EXPIRATION_SECONDS
from email_validator import validate_email, EmailNotValidError
from flask import Flask, abort, request, jsonify, render_template, redirect, url_for, request
from datetime import datetime
import requests, json, os
from datetime import timedelta
import modules.error_handlers, modules.utils # SAM's modules

"""
[Summary]: User Authentication Service (i.e., login).
[Returns]: Returns a JSON object with the data of the user including a JWT authentication token.
"""
@app.route('/user/login', methods=['POST'])
def login_user():
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
            cursor.execute("SELECT ID, email, psw, avatar, administrator FROM User WHERE email=%s", email)
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
            data['id']          = row[0]
            data['email']       = row[1]
            # For security reasons lets not store the password in the dic.
            dbpsw               = row[2] 
            data['avatar']      = row[3]
            data['is_admin']    = row[4]
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
    debug=False
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
def logout_user():
    debug = False
    data = {}
    if request.method != "POST": return
    # 1. Check if the token is available on the request header.
    headers = dict(request.headers)
    if (debug): print(str(len(headers)))
    
    # 2. Check if the Authorization header name was parsed.
    if 'Authorization' not in headers: raise modules.error_handlers.BadRequest(request.path, "Authentication failure - You don't have the permission to access this resource. Please, provide an authorization token.", 403) 
    token_parsed = headers['Authorization']
    if (debug): print("Parsed Token:" + token_parsed)
    
    try:
        # 3. From now on the token will be blacklisted because the user has logout and the token may still
        #    exists somewhere because its expiration date is still valid.
        
        # 3.1. Let's clean the house - Remove possible expired tokens from the user of the token
        res_dic  = jwt.decode(token_parsed, JWT_SECRET_TOKEN, algorithms=['HS256'])
       
        userID = int(res_dic['id'])
        if not clear_expired_blacklisted_JWT(userID): # Sanity check
            return (modules.utils.build_response_json(request.path, 500))
        # 3.2. Let's add the token to the blacklist table on the database for the current user
        #      That is, blacklist the current token, that may or may not be alive. 
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("INSERT INTO Auth_Token_Blacklist (userID, token) VALUES (%s, %s)", (userID, token_parsed))
        conn.commit()
        data['message'] = "The authentication token was blacklisted. The user should now be logouted on the client side."
       
    except jwt.exceptions.ExpiredSignatureError as e:
        # We don't need to blacklist this token, the token is already expired (see 'exp' field of the JWT defined in the authenticate function).
        # raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
        data['message'] = "The token has already expired, no need to blacklist it. The user should now be logouted on the client side."
        return (modules.utils.build_response_json(request.path, 200, data))
    except Exception as e :
        # Double token entry ?
        if e.args[0] == 1062:
            data['message'] = "The token was already blacklisted. The user should now be logouted on the client side."
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

@app.route('/user/<email>/admin', methods=['GET'])
def is_admin(email):
    if request.method != 'GET': return
    # 1. Check if the user has permissions to access this resource
    isAuthenticated(request)

    # 2. Let's get the groups associated with the parsed user.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT email, administrator FROM User WHERE email=%s AND administrator=1", email) 
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 

    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404)) 
    else:
        cursor.close()
        conn.close()
        data = {True}
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200))

"""
[Summary]: User Registration Service (i.e., add a new user).
[Returns]: Returns a JSON object with the data of the user including a JWT authentication token.
"""
@app.route('/user', methods=['POST'])
def add_user():
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
[Summary]: Get users.
[Returns]: Returns a User object.
"""
# Check if a user exists
@app.route('/users', methods=['GET'])
def get_users():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    isAuthenticated(request)
    
    # 3. Let's get users from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, email, firstName, lastName, avatar, userStatus, administrator, createdon, updatedon FROM User")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Empty results ?
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] 
        for row in res:
            data = {}
            data['id']          = row[0]
            data['email']       = row[1]
            data['firstName']   = row[2]
            data['lastName']    = row[3]
            data['avatar']      = row[4]
            data['user_status']  = row[5]
            data['administrator'] = row[6]
            data['createdon']   = row[7]
            data['updatedon']   = row[8]
            datas.append(data)
        cursor.close()
        conn.close()
        # 4. Return information about the user (except the password) and 'May the Force be with you'.
        return(modules.utils.build_response_json(request.path, 200, datas))    

"""
[Summary]: Finds a user by email.
[Returns]: Returns a User object.
"""
# Check if a user exists
@app.route('/user/<email>', methods=['GET'])
def find_user(email, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    if (not internal_call):
        isAuthenticated(request)
       
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
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404))
        else:
            return(None)
    else:
        data = {} # Create a new nice empty dictionary to be populated with data from the DB.
        for row in res:
            data['id']          = row[0]
            data['email']       = row[1]
            data['firstName']   = row[2]
            data['lastName']    = row[3]
            data['avatar']      = row[4]
        cursor.close()
        conn.close()

        # 4. Return information about the user (except the password) and 'May the Force be with you'.
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, data))
        else:
            return(data)

"""
[Summary]: Delete a user
[Returns]: Returns a success or error response
"""
@app.route('/user/<email>', methods=["DELETE"])
def delete_user(email):
    if request.method != 'DELETE': return
    # 1. Check if the user has permissions to access this resource
    isAuthenticated(request)
  
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
def update_user(email):
    updatePsw = False
    # Note: Remember that if an email is being changed, the email argument is the old one; 
    #       The new email content is available on the JSON object parsed in the body of the request.  
    if request.method != 'PUT': return
    # 1. Check if the user has permissions to access this resource
    isAuthenticated(request)

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

"""
[Summary]: Finds groups of a user.
[Returns]: Returns a success or error response
"""
@app.route('/user/<email>/groups', methods=["GET"])
def find_user_groups(email):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    isAuthenticated(request)
       
    # 2. Let's validate the email, invalid emails from this point are not allowed.
    try:
        valid = validate_email(email)
    except EmailNotValidError as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 
    
    # 3. Let's get the user from the database with the provided [email].
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT user_id, user_email, user_group FROM View_User_Group WHERE user_email=%s", email)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Empty results ?
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = []
        for row in res:
            data = {} # Create a new nice empty dictionary to be populated with data from the DB.
            data['user_id']     = row[0]
            data['user_email']  = row[1]
            data['user_group']  = row[2]
            datas.append(data)
        cursor.close()
        conn.close()
        # 4. Return information about the user (except the password) and 'May the Force be with you'.
        return(modules.utils.build_response_json(request.path, 200, datas))    

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
    
    # 3. Decode the authorization token to get the User object.
    try:
        # Decode will raise an exception if anything goes wrong within the decoding process (i.e., perform validation of the JWT).
        res_dic  = jwt.decode(parsedToken, JWT_SECRET_TOKEN, algorithms=['HS256'])
        # Get the ID of the user.
        userID = int(res_dic['id'])
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
