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
import modules.error_handlers, modules.utils # SAM's modules

"""
[Summary]: Find a user by email.
[Returns]: Returns a User object.
"""
# Check if a user exists
@app.route('/user/<email>', methods=['GET'])
def getUser(email):
    # 1. Let's validate the email, invalid emails from this point are not allowed.
    try:
        valid = validate_email(email)
    except EmailNotValidError as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 400) 
    
    # 2. Let's get the user from the database with the provided [email].
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, email, psw, avatar FROM User WHERE email=%s", email)
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
            data['ID']      = row[0]
            data['email']   = row[1]
            data['avatar']  = row[3]
        cursor.close()
        conn.close()
        # 3. Return information about the user (except the password) and 'May the Force be with you'.
        return(modules.utils.build_response_json(request.path, 200, data))    