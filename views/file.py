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
from flask import Flask, request, abort, jsonify, send_from_directory
import os, views.user, modules.utils
from werkzeug.utils import secure_filename

UPLOAD_DIRECTORY="./external/"

@app.route("/file/<path:path>", methods=['GET'])
def get_file(path):
    if request.method != 'GET': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)
    
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

@app.route("/files", methods=['GET'])
def list_files():
    if request.method != 'GET': return
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

@app.route("/file/<filename>", methods=["POST"])
def post_file(filename):
    if request.method != 'POST': return
    file = request.files['file']
    # Check if the user has permissions to access this resource
    views.user.isAuthenticated(request)

    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories directories allowed")

    if file:
        filename = secure_filename(filename)
        file.save(UPLOAD_DIRECTORY + filename)

    # Return 201 CREATED
    return(modules.utils.build_response_json(request.path, 201))    