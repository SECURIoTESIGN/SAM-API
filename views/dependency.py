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
import views.user, views.module # SAM's views

"""
[Summary]: Adds a new dependency to the database.
[Returns]: Response result.
"""
@app.route('/dependency', methods=['POST'])
def add_dependency(json_internal_data=None, internal_call=False):
    DEBUG=True
    if (not internal_call):
        if request.method != 'POST': return
    
    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    if (not internal_call):
        json_data = request.get_json()
    else:
        json_data = json_internal_data

    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): 
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 400))
        else:
            modules.utils.console_log("[POST]/dependency", "json_data is None")
            return(None)
   
    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"module_id", "depends_on"})):
        if (not internal_call):
            raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    
        else:
            modules.utils.console_log("[POST]/dependency", "Some required key or value is missing from the JSON object")

    module_id   = json_data['module_id']
    depends_on  = json_data['depends_on']
    createdon   = "createdon" in json_data and json_data['createdon'] or None
    updatedon   = "updatedon" in json_data and json_data['updatedon'] or None
    
    # Build the SQL instruction using our handy function to build sql instructions.
    values  = (module_id, depends_on, createdon, updatedon)
    columns = ["moduleID", "dependsOn", createdon and "createdon" or None, updatedon and "updatedon" or None]
    sql, values = modules.utils.build_sql_instruction("INSERT INTO dependency", columns, values)
    if (DEBUG): modules.utils.console_log("[POST]/dependency", sql)

    # Add
    n_id = modules.utils.db_execute_update_insert(mysql, sql, values)

    if (n_id is None):
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 400))
        else:
            return(None)
    else:
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 200, {"id": n_id}))
        else:
            return(n_id)

"""
[Summary]: Updates a dependency.
[Returns]: Response result.
"""
@app.route('/dependency', methods=['PUT'])
def update_dependency(json_internal_data=None, internal_call=False):
    DEBUG=True
    if (not internal_call):
        if request.method != 'PUT': return
    
    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    if (not internal_call):
        json_data = request.get_json()
    else:
        json_data = json_internal_data
    
    # If the mimetype does not indicate JSON (application/json, see is_json()), this returns None.
    if (json_data is None): 
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 400)) 
        else:
            modules.utils.console_log("[PUT]/dependency", "json_data is None")
            return(None)

    dependency_id_available = True
    # Validate if the necessary data is on the provided JSON 
    if (not modules.utils.valid_json(json_data, {"id"})):
        dependency_id_available = False
        if (not modules.utils.valid_json(json_data, {"module_id", "depends_on", "p_depends_on"})):
            raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the JSON object", 400)    
        

    module_id     = "module_id"     in json_data and json_data['module_id'] or None
    depends_on    = "depends_on"    in json_data and json_data['depends_on'] or None     # New dependency
    p_depends_on  = "p_depends_on"  in json_data and json_data['p_depends_on'] or None   # Previous dependency
    createdon     = "createdon"     in json_data and json_data['createdon'] or None
    updatedon     = "updatedon"     in json_data and json_data['updatedon'] or None

    # IF required, get the ID of the dependency taking into account the id of the module and the id of the module that it depends on.
    if (not dependency_id_available):
        json_tmp = find_dependency_of_module_2(module_id, p_depends_on, True)
        if (not json_tmp):
            raise modules.error_handlers.BadRequest(request.path, "Some required key or value is missing from the temporary JSON object", 400)    
        json_data['id'] = json_tmp['id']
    
    # Build the SQL instruction using our handy function to build sql instructions.
    values  = (module_id, depends_on, createdon, updatedon)
    columns = [module_id and "moduleID" or None, depends_on and "dependsOn" or None, createdon and "createdon" or None, updatedon and "updatedOn" or None]
    where   = "WHERE id="+str(json_data['id'])

    # Check if there is anything to update (i.e. frontend developer has not sent any values to update).
    if (len(values) == 0): return(modules.utils.build_response_json(request.path, 200))   

    sql, values = modules.utils.build_sql_instruction("UPDATE dependency", columns, values, where)
    if (DEBUG): modules.utils.console_log("[PUT]/dependency", sql + " " + str(values))

    # Update resource
    modules.utils.db_execute_update_insert(mysql, sql, values)

    if (not internal_call):
        return(modules.utils.build_response_json(request.path, 200))
    else:
        return(True)

"""
[Summary]: Get dependencies.
[Returns]: Response result.
"""
@app.route('/dependencies')
def get_dependency():
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, moduleID, dependsOn, createdOn, UpdatedOn FROM dependency")
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
            data['module_id']   = row[1]
            data['depends_on']  = row[2]
            data['createdon']   = row[3]
            data['updatedon']   = row[4]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200, datas)) 

"""
[Summary]: Finds a dependency.
[Returns]: Response result.
"""
@app.route('/dependency/<ID>', methods=['GET'])
def find_dependency(ID):
    if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT ID, moduleID, dependsOn, createdOn, UpdatedOn FROM dependency WHERE ID=%s", ID)
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
            data['module_id']   = row[1]
            data['depends_on']  = row[2]
            data['createdon']   = row[3]
            data['updatedon']   = row[4]
            datas.append(data)
        cursor.close()
        conn.close()
        # 3. 'May the Force be with you, young master'.
        return(modules.utils.build_response_json(request.path, 200, datas)) 

"""
[Summary]: Finds a dependency of a module
[Returns]: Response result.
"""
@app.route('/dependency/module/<ID>', methods=['GET'])
def find_dependency_of_module(ID, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("SELECT dependency_id, depends_module_id, createdOn, updatedOn FROM View_Module_Dependency WHERE module_ID=%s", ID)
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404)) 
        else:
            return None
    else:
        datas = []
        for row in res:
            data = {}
            data['id']                      = row[0]
            t_module = views.module.find_module(row[1], True)
            module = {}
            module['id']                    = t_module[0]['id']
            module['fullname']              = t_module[0]['fullname']
            module['displaname']            = t_module[0]['displayname']
            module['shortname']             = t_module[0]['shortname']
            data['module']                  = module
            data['createdon']               = row[2]
            data['updatedon']               = row[3]
            datas.append(data)
        cursor.close()
        conn.close()
        
        # 3. 'May the Force be with you, young master'.
        if (not internal_call): 
            return(modules.utils.build_response_json(request.path, 200, datas)) 
        else:
            return(datas)


"""
[Summary]: Finds a dependency of a module, taking as arguments the id of the current module and the id of the module that it depends on.
[Returns]: Response result.
"""
@app.route('/dependency/module/<module_id>/depends/<depends_on_module_id>', methods=['GET'])
def find_dependency_of_module_2(module_id, depends_on_module_id, internal_call=False):
    if (not internal_call):
        if request.method != 'GET': return

    # 1. Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # 2. Let's get the answeers for the question from the database.
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        print("--->" + "SELECT dependency_id, module_id, depends_module_id, createdOn, updatedOn FROM View_Module_Dependency WHERE module_ID=%s AND depends_module_id=%s", (module_id, depends_on_module_id))
        cursor.execute("SELECT dependency_id, module_id, depends_module_id, createdOn, updatedOn FROM View_Module_Dependency WHERE module_ID=%s AND depends_module_id=%s", (module_id, depends_on_module_id))
        res = cursor.fetchall()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500)
    
    # 2.2. Check for empty results 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        if (not internal_call):
            return(modules.utils.build_response_json(request.path, 404)) 
        else:
            return None
    else:
        data = {}
        for row in res:
            data['id']                      = row[0]
            data['module_id']               = row[1]
            data['depends_on_module_id']    = row[2]
            data['createdon']               = row[2]
            data['updatedon']               = row[3]
        cursor.close()
        conn.close()
        
        # 3. 'May the Force be with you, young master'.
        if (not internal_call): 
            return(modules.utils.build_response_json(request.path, 200, data)) 
        else:
            return(data)


"""
[Summary]: Delete a dependency by id.
[Returns]: Returns a success or error response
"""
@app.route('/dependency/<dependency_id>', methods=["DELETE"])
def delete_dependency(dependency_id, internal_call=False):
    if (not internal_call):
        if request.method != 'DELETE': return

    # Check if the user has permissions to access this resource
    if (not internal_call): views.user.isAuthenticated(request)

    # Connect to the database and delete the resource
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        cursor.execute("DELETE FROM dependency WHERE ID=%s", dependency_id)
        conn.commit()
    except Exception as e:
        raise modules.error_handlers.BadRequest(request.path, str(e), 500) 
    finally:
        cursor.close()
        conn.close()

    # The Delete request was a success, the user 'took the blue pill'.
    if (not internal_call):
        return (modules.utils.build_response_json(request.path, 200))
    else:
        return(True)
