""""""
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
"""
__version__ = "0.9.0"
import time, pathlib
import modules.error_handlers, modules.utils # SAM's modules
from configparser import SafeConfigParser
from flask import Flask, request, render_template
from flaskext.mysql import MySQL

""" Initialization """
app = Flask(__name__)
app.register_blueprint(modules.error_handlers.blueprint)
# Load data from the configuration file 
# <!> Please, do not store your configuration file in the github repository.
parser = SafeConfigParser()
# parser.read(str(pathlib.Path(__file__).parent.resolve()) +'/instance/config.cfg')
parser.read('./instance/config.cfg');
# JWT related stuff
JWT_SECRET_TOKEN = parser.get('default', 'JWT_SECRET_TOKEN')
JWT_EXPIRATION_SECONDS = parser.get('default', 'JWT_EXPIRATION_SECONDS')
# reCAPTCHA related stuff
RECAPTCHA_SECRET = parser.get('default', 'RECAPTCHA_SECRET')

# MySQL/MariaDB related stuff
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = parser.get('default', 'MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = parser.get('default', 'MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = parser.get('default', 'MYSQL_DATABASE_DB')
app.config['MYSQL_DATABASE_HOST'] = parser.get('default', 'MYSQL_DATABASE_HOST')
mysql.init_app(app)
import views.user, views.module, views.session, views.recommendation, views.question, views.answer, views.group, views.type, views.dependency, views.file, views.statistic # SAM's views
import modules.utils

""" Main route where all the magic happens."""
@app.route('/')
def home():
    return render_template('home.html', version=__version__)
