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
from genericpath import isfile
import os, getpass, configparser;

def create_instance_file():
    print("[SAM] Creating the instance file...")
    config = configparser.ConfigParser()
    try: os.mkdir("./instance")
    except: pass
    config = configparser.ConfigParser()
    config.add_section('default')
    
    db_user = input("[SAM] Input the database username with access to SAM's database: ")
    db_psw = getpass.getpass("[SAM] Input user password: ")
    db_host = input("[SAM] Input the hostname: ")
    db_port = input("[SAM] Input port: ")

    config['default']['MYSQL_DATABASE_USER'] = db_user
    config['default']['MYSQL_DATABASE_PASSWORD'] = db_psw
    config['default']['MYSQL_DATABASE_DB'] = 'sam'
    config['default']['MYSQL_DATABASE_HOST'] = db_host
    config['default']['MYSQL_DATABASE_PORT'] = db_port
    config['default']['JWT_SECRET_TOKEN'] = '3NTJ25Q25=DDPn343L-aX$'
    config['default']['JWT_EXPIRATION_SECONDS'] = '86400'
    config['default']['RECAPTCHA_SECRET'] = input("[SAM] Input the server recaptcha secret: ")

    with open('./instance/config.cfg', 'w') as configfile:
        config.write(configfile)
    
    if (not os.path.isfile(".flaskenv")):
        create_flaskenv_file()

def create_flaskenv_file():
    if (((input("[SAM] Create Flask env configuration file [y/n]: ")).lower().strip())[0] == "n"): return
    print("[SAM] Creating the flask env configuration file...")
    f = open(".flaskenv", "w")
    f.write("FLASK_APP=api.py\n")
    if (((input("[SAM] Set Flask development flag [y/n]: ")).lower().strip())[0] == "y"):
        f.write("FLASK_ENV=development\n")
    
    f.write("FLASK_RUN_HOST=0.0.0.0\n")
    f.write("FLASK_RUN_PORT=8080\n")
    f.close()


if __name__ == "__main__":
    if (not os.path.isfile("./instance/config.cfg")):
        create_instance_file()
    else:
        print("[SAM] Nothing to do, exiting...")