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
import time, hashlib, uuid, flask, json, codecs, os
from flask import jsonify
import modules.error_handlers

"""
[Summary]: Outputs a message to the terminal.
[Arguments]:
       - $function_name$: The name of the function/method/service where the message originated from. 
       - $message$: Message to be displayed.
       - $exception$: Flag the message as an exception.
"""
def console_log(function_name, message, exception=False):
  if (not exception):
    print("[SAM-API] " + function_name + "() => '" + message + "'")
  else:
    print("[SAM-API] " + function_name + "() => Exception error : '" + message + "'")

"""
[Summary]: Builds SQL INSERT or UPDATE instruction with columns that may or may not be defined. None values are also purged from the values inputted.
[Arguments]:
       - $SQL$: Barebones SQL instruction. For example, "INSERT INTO User"
       - $columns$: List of columns that may containg None values, in this case the column is not included in the SQL instruction (e.g., ["username", "password"]).
       - $values$: List of values of the SQL instruction.
[Usage Example]: 
       sql = modules.utils.build_sql_instruction("INSERT INTO Recommendation", ["content", "description", "guideFilename", "createdon", updatedon and "updatedon" or None], values)
[Returns]: The final SQL instruction to be feed into the db_execute_update_insert() function.
"""
def build_sql_instruction(SQL, columns, values, where=None):
    values                      = [i for i in values if i] # If exists, remove None values.
    columns                     = [i for i in columns if i] # If exists, remove None values.
    table_columns, table_values = (str(SQL.lower()).find("update")) == 0 and "SET " or "", ""
    
    if ((str(SQL.lower()).find("insert")) == 0):
        # Proc. columns
        i = 0
        for column in columns:
            table_columns   += (i==0) and ("(" + column) or ((i==(len(columns)-1)) and ("," + column +")") or ("," + column))
            i = i + 1
        i = 0
        # Proc. Values
        for value in values:
            value = "%s"
            table_values    += (i==0) and (" VALUES (" + value) or ((i==len(values)-1) and (","+value+")") or (","+value)) 
            i = i + 1
        SQL = SQL + " " + table_columns + table_values
    if ((str(SQL.lower()).find("update")) == 0):
        # Proc. columns 
        i = 0
        for column in columns:
            table_columns   += (i!=len(columns)-1) and (column +"=%s,") or (column +"=%s")
            i = i + 1
        SQL = SQL + " " + table_columns + table_values + " " + str(where)
    
    return(SQL, values)

"""
[Summary]: Check if an entry exists on the database
[Arguments]:
       - $SQL$: Barebones SQL instruction. For example, "INSERT INTO User"
       - $columns$: List of columns of the table.
       - $values$: List of values of the SQL instruction.
[Returns]: True if exists, false otherwise.
"""
def db_already_exists(mysql, SQL, values, DEGUG=True): 
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        if (DEBUG): console_log("db_already_exists", "SQL=" + SQL + " | values=" + str(values))
        cursor.execute(SQL, values)
        res = cursor.fetchall()
    except Exception as e:
        console_log("db_already_exists", str(e), True)
        return(False)
    
    # Check for empty results. 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(False)    
    else:
        cursor.close()
        conn.close()
        return(True)
    
    retur(False)

"""
[Summary]: Executes a SQL INSERT or UPDATE instruction
[Arguments]:
       - $SQL$: Barebones SQL instruction. For example, "INSERT INTO User"
       - $columns$: List of columns of the table.
       - $values$: List of values of the SQL instruction.
[Returns]: If it is an SQL Insert operation then the return value is the id of the last created entry. 
"""
def db_execute_update_insert(mysql, SQL, values, DEBUG=True):
    n_id = None
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute(SQL, values)
        # Store and return the id of the last created entry in the table.
        if ( (str(SQL.lower()).find("insert")) != -1): n_id = conn.insert_id()
        conn.commit()
    except Exception as e:
        console_log("db_execute_update_insert", str(e), True)
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()
        return(n_id)

"""
obter ap rimary key tendo em conta outros valores
"""
def db_get_primary_key_value(mysql, primary_key, table, where=None, DEBUG=False):
    primary_key_value = None
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        sql     = "SELECT " + primary_key + " FROM " + table + " " + where
        cursor.execute(sql)
        res = cursor.fetchall()
    except Exception as e:
        console_log("db_execute_select", str(e), True)
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results. 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(None)   
    else:
        for row in res:
            primary_key_value = row[0]
    
    cursor.close()
    conn.close()
    return(primary_key_value)
"""
[Summary]: Check if a key/pair value is on a JSON object.
[Arguments]:
       - $json_object$: The JSON object to validate.
       - $keys$: The JSON object must have these keys.
[Returns]: Returns true if valid, false otherwise.
"""
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
    # Check if data is an array/list of dic
    if isinstance(data, list):
        ndata = {}
        ndata['status']     = status
        ndata['content']    = data
        print(ndata)
        return jsonify({route : ndata})
    else:
        data['status'] = status 
        # print(data)
        return jsonify({route : data})
    

""" 
[Summary]: Hash a password with some salt
[Arguments]:
       - $password$: The password to hash
[Returns]: Returns the hash of a password + the salt
TODO: Change to bcrypt if possible
TODO: implement a random salt for each request
"""
def hash_password(password):
    # Static salt: uuid is used to generate a random number.
    # salt = uuid.uuid4().hex 
    # Dynamic sal.
    salt = codecs.encode(os.urandom(16), 'hex').decode()
    # The password hash and the salt will be stored in the database
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

""" 
[Summary]: Check if a hashed password is equal to one provided by a user.
[Arguments]:
       - $password$: The password to check.
[Returns]: Returns true if equal, false otherwise.
TODO: Change to bcrypt if possible
"""
def check_password(hashed_password, user_password):
    # Let's combine the salt and the password
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
