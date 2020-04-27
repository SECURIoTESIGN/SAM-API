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
import time, flask, json, modules.utils
from flask import jsonify
blueprint = flask.Blueprint('error_handlers', __name__)

"""
[Summary]: BadRequest class, the name says it all
[Example]: raise error_handlers.BadRequest('The email cannot be empty', 403
"""
class BadRequest(Exception):
    # Custom exception class to be thrown when local error occurs.
    def __init__(self, route, message, status):
        self.route      = route
        self.message    = message
        self.status     = status
        
@blueprint.app_errorhandler(BadRequest)
def handle_bad_request(error):
    # Catch BadRequest exception globally, serialize into JSON, and respond with a [error.status].
    data = {}
    data['route']   = error.route
    data['message'] = error.message
    data['status']  = error.status
    return modules.utils.build_response_json(error.route, error.status, data), error.status