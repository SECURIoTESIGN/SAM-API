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
//
List of third-party Python3 modules:
# Pyjwt             -> https://pyjwt.readthedocs.io/en/latest/
# Flask-mysql       -> https://flask-mysql.readthedocs.io/en/latest/#
# flasgger          -> https://github.com/flasgger/flasgger
# email_validator   -> https://github.com/JoshData/python-email-validator
"""
VERSION = 0.1
import time, json, jwt, os, urllib
import modules.error_handlers, modules.utils # SAM's modules
from datetime import datetime
from configparser import SafeConfigParser
from flask import Flask, abort, request, jsonify, render_template, redirect, url_for, request
from flaskext.mysql import MySQL
from flasgger import Swagger
from flasgger.utils import swag_from
from jsonschema import validate

""" Initialization """
app = Flask(__name__)
app.config['SWAGGER'] = {'title': 'SAM','uiversion': 3}
Swagger(app, template_file='api.yaml')
app.register_blueprint(modules.error_handlers.blueprint)
# Load data from the configuration file 
# <!> Please, do not store your configuration file in the github repository.
parser = SafeConfigParser()
parser.read('instance/config.cfg')
#print(parser.get('DEFAULT', 'color'))
# JWT related stuff
JWT_SECRET_TOKEN = parser.get('DEFAULT', 'JWT_SECRET_TOKEN')
# MySQL related stuff
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = parser.get('DEFAULT', 'MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = parser.get('DEFAULT', 'MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = parser.get('DEFAULT', 'MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = parser.get('DEFAULT', 'MYSQL_DATABASE_HOST')
mysql.init_app(app)
import views.authentication, views.user # SAM's views

""" Main route where all the magic starts."""
@app.route('/')
def home():
    return render_template('home.html', version=VERSION)

"""
[Summary]: Just a test service to demonstrate that only authenticated users can access this resource.
[Returns]: Returns the current time.
"""
@app.route('/time')
def get_current_time():
    views.isAuthenticated(request)
    return {'time': time.time()}
