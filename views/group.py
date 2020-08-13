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
import views.user, views.answer # SAM's views

"""
[Summary]: Adds a new question to the database.
[Returns]: Response result.
"""
@app.route('/group', methods=['POST'])
def add_group():
    DEBUG=True
    if request.method != 'POST': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"designation"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)   

    designation = json_data['designation']
    g_modules   = "modules" in json_data and json_data['modules'] or None
    g_users     = "users" in json_data and json_data['users'] or None
    createdon   = "createdon" in json_data and json_data['createdon'] or None
    updatedon   = "updatedon" in json_data and json_data['updatedon'] or None
    
    # Build the SQL instruction using our handy function to build sql instructions.
    values = (designation, createdon, updatedon)
    sql, values = modules.utils.build_sql_instruction("INSERT INTO SAM.Group", ["designation", createdon and "createdon" or None, updatedon and "updatedon" or None], values)
    if (DEBUG): print("[SAM-API]: [POST]/group - " + sql)

    print(g_modules)
    print(g_users)
    
    # Add
    n_id = modules.utils.db_execute_update_insert(mysql, sql, values)
    if (n_id is None):
        return(modules.utils.build_response_json(request.path, 400))  
    else:
        # If any, link the list of provided users or modules to this group
        if (g_users):
            for g_user in g_users:
                values = (g_user['id'], n_id)
                sql, values = modules.utils.build_sql_instruction("INSERT INTO User_Group", ["userID", "groupID"], values)
                modules.utils.db_execute_update_insert(mysql, sql, values)
        if (g_modules):
            for g_module in g_modules:
                values = (g_module['id'], n_id)
                sql, values = modules.utils.build_sql_instruction("INSERT INTO Module_Group", ["moduleID", "groupID"], values)
                modules.utils.db_execute_update_insert(mysql, sql, values)
        
        return(modules.utils.build_response_json(request.path, 200, {"id": n_id}))  

"""
[Summary]: Updates a group.
[Returns]: Response result.
"""
@app.route('/group', methods=['PUT'])
def update_group():
    DEBUG=True
    if request.method != 'PUT': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    json_data = request.get_json()
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"id"})):
        raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    

    group_id    = json_data['id']
    designation = "designation" in json_data and json_data['designation'] or None
    g_modules   = "modules" in json_data and json_data['modules'] or None
    g_users     = "users" in json_data and json_data['users'] or None
    createdon   = "createdon"   in json_data and json_data['createdon'] or None
    updatedon   = "updatedon"   in json_data and json_data['updatedon'] or None

    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): return(modules.utils.build_response_json(request.path, 400)) 

    # Build the SQL instruction using our handy function to build sql instructions.
    values  = (designation, createdon, updatedon)
    columns = [designation and "designation" or None, createdon and "createdon" or None, updatedon and "updatedOn" or None]
    where   = "WHERE id="+str(group_id)
    # Check if there is anything to update (i.e. frontend developer has not sent any values to update).
    if (len(values) == 0): return(modules.utils.build_response_json(request.path, 200))   

    sql, values = modules.utils.build_sql_instruction("UPDATE SAM.Group", columns, values, where)
    if (DEBUG): print("[SAM-API]: [PUT]/group - " + sql + " " + str(values))

    # Update Recommendation
    modules.utils.db_execute_update_insert(mysql, sql, values)
    
    # Check if there are any user flagged to be removed, what is removed is not the user but the mapping of a user to the current group.
    if g_users:
        for g_user in g_users:
            flag_remove = "to_remove" in g_user and g_user['to_remove'] or None
            # Remove the link between the user and the group
            if (flag_remove):
                try:
                    conn    = mysql.connect()
                    cursor  = conn.cursor()
                    cursor.execute("DELETE FROM User_Group WHERE userID=%s", g_user['id'])
                    conn.commit()
                except Exception as e:
                    print("entrou")
                    raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
                finally:
                    cursor.close()
                    conn.close()
            # Add a new user mapping
            else:
                values = (g_user['id'], group_id)
                sql, values = modules.utils.build_sql_instruction("INSERT INTO User_Group", ["userID", "groupID"], values)
                modules.utils.db_execute_update_insert(mysql, sql, values)
    
    # Do as above, but for modules.
    if g_modules:
        for g_module in g_modules:
            flag_remove = "to_remove" in g_module and g_module['to_remove'] or None
            # Remove the link between the user and the group
            if (flag_remove):
                try:
                    conn    = mysql.connect()
                    cursor  = conn.cursor()
                    cursor.execute("DELETE FROM Module_Group WHERE moduleID=%s", g_module['id'])
                    conn.commit()
                except Exception as e:
                    raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
                finally:
                    cursor.close()
                    conn.close()
            # Add a new module mapping
            else:
                values = (g_module['id'], group_id)
                sql, values = modules.utils.build_sql_instruction("INSERT INTO Module_Group", ["moduleID", "groupID"], values)
                modules.utils.db_execute_update_insert(mysql, sql, values)

    return(modules.utils.build_response_json(request.path, 200))   

"""
[Summary]: Get Groups.
[Returns]: Response result.
"""
@app.route('/groups')
def get_groups():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, designation, createdon, updatedon FROM SAM.Group")
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']          = row[0]
            data['designation'] = row[1]
            data['modules']     = find_modules_of_group(row[0])
            data['users']       = find_users_of_group(row[0])
            data['createdon']   = row[2]
            data['updatedon']   = row[3]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200, datas)) 

"""
[Summary]: Finds the list of modules linked to a type.
[Returns]: A list of modules or an empty array if None are found.
"""
def find_modules_of_group(group_id):
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT moduleID FROM Module_Group WHERE groupID=%s", group_id)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return([]) 
    else:
        modules = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            module = views.module.find_module(row[0], True)[0]
            del module['tree']
            del module['dependencies']
            del module['recommendations']
            modules.append(module)
        cursor.close()
        conn.close()
       
        # 'May the Force be with you, young master'.
        return(modules)

def find_users_of_group(group_id):
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT user_email FROM View_User_Group WHERE group_id=%s", group_id)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return([]) 
    else:
        users = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            user = views.user.find_user(row[0], True)
            users.append(user)
        cursor.close()
        conn.close()
       
        # 'May the Force be with you, young master'.
        return(users)

"""
[Summary]: Finds Question.
[Returns]: Response result.
"""
@app.route('/group/<ID>', methods=['GET'])
def find_group(ID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, designation, createdon, updatedon FROM SAM.Group WHERE ID=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(modules.utils.build_response_json(request.path, 404))    
    else:
        datas = [] # Create a new nice empty array of dictionaries to be populated with data from the DB.
        for row in res:
            data = {}
            data['id']          = row[0]
            data['designation'] = row[1]
            data['modules']     = find_modules_of_group(row[0])
            data['users']       = find_users_of_group(row[0])
            data['createdon']   = row[2]
            data['updatedon']   = row[3]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200, datas)) 

"""
[Summary]: Delete a Group.
[Returns]: Returns a success or error response
"""
@app.route('/group/<ID>', methods=["DELETE"])
def delete_group(ID):
    if request.method != 'DELETE': return
    # 1. Check if the user has permissions to access this resource.
    views.user.isAuthenticated(request)

    # 2. Connect to the database and delete the resource.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("DELETE FROM SAM.Group WHERE ID=%s", ID)
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # 3. The Delete request was a success, the user 'took the blue pill'.
    return (modules.utils.build_response_json(request.path, 200))
