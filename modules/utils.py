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
import time, hashlib, uuid, flask, json
from flask import jsonify

# Check if a key is on the json object, and its has values
def valid_json(json_object:None, keys):
    for key in keys:
        if key in json_object:
            # Check if there is a value in the key, if not return false
            if (not json_object[key]):
                return(False)
        else:
            return(False)
    return(True)


"""
[Summary]: Creates a JSON Response built around a set of parsed arguments.
[Arguments]:
       - $name$: is typically the route name.
       - $data$: is a dictionary.
       - $status$: is the HTML status code (e.g, 200).
[References]: https://kite.com/python/docs/flask.jsonify
[Returns]: A JSON response with a HTML code.
"""
def build_response_json(route, status, data={}):
    # If a data object is not provided, data is initialized (i.e. data={}) 
    data['status'] = status 
    return jsonify({route : data})

""" 
[Summary]: Hash a password with some salt
[Arguments]:
       - $password$: The password to hash
[Returns]: Returns the hash of a password + the salt
"""
# TODO: implement a random salt for each user's password
def hash_password(password):
    # uuid is used to generate a random number
    salt = uuid.uuid4().hex
    # The password hash and the salt will be stored in the database
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

""" 
[Summary]: Check if a hashed password is equal to one provided by a user.
[Arguments]:
       - $password$: The password to check.
[Returns]: Returns true if equal, false otherwise.
"""
def check_password(hashed_password, user_password):
    # Let's combine the salt and the password
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
