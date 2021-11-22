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
import os, getpass, configparser;
DB_SCHEMA          = "database-schema.sql"
DB_VIEWS_TRIGGERS  = "database-views-triggers.sql"
DB_DATA	           = "database-data.sql"
# Set to true if the root database user can access the DB with a password, False if unix_socket is enable.
ROOT_WITH_PSW      = True


class Database:
    master  = "root"
    master_psw = ""
    db_user = "sam" # Standard username to be created on the database.
    db_psw = "sam"  # Standard Username password to be created for user 'sam'.
    db_host = "%" # Host
    
    def __init__(self):
        # Create the database schema
        self.__create_schema()  

    def __create_user(self):
        print("[SAM] Creating database user...")
        self.db_user = input("[SAM] Input the username to be created on the database: ")
        self.db_psw = getpass.getpass("[SAM] Input the password for the new user: ")
        #self.db_host = input("[SAM] Input the hostname: ")
        
        ins  = "DROP USER IF EXISTS '"+self.db_user+"'@'"+self.db_host+"';"
        ins += "CREATE USER '"+self.db_user+"'@'"+self.db_host+"' IDENTIFIED BY '"+self.db_psw+"'; "
        ins += "GRANT ALL PRIVILEGES ON `sam`.* TO '"+self.db_user+"'@'"+self.db_host+"'; FLUSH PRIVILEGES;"
        # print(ins)
        f = open("install.tmp", "w")
        f.write(ins)
        f.close()
        if (ROOT_WITH_PSW):
            if (os.system(" mysql -u"+self.master+" -p"+self.master_psw+" < install.tmp") != 0): exit()
        else: 
            if (os.system(" mysql -u"+self.master+" < install.tmp") != 0): exit()
        # Remove tmp file
        os.remove("install.tmp")
        self.__add_data()

    def __create_schema(self):
        print("[SAM] Creating database...")
        self.master_psw = getpass.getpass("[SAM] Input the password of the user that has full permissions (i.e., the root password): ")
        if (ROOT_WITH_PSW):
            # master_psw = getpass.getpass("[SAM] Input the password of the user that has full permissions (e.g., root): ")
            ins = " mysql -u"+self.master+" -p"+self.master_psw+" < " + DB_SCHEMA
            ins += " &&  mysql -u"+self.master+" -p"+self.master_psw+" < " + DB_VIEWS_TRIGGERS
        else:
            ins  = " mysql -u"+self.master+" < " + DB_SCHEMA
            ins += " &&  mysql -u"+self.master+" < " + DB_VIEWS_TRIGGERS

        if (os.system(ins) != 0): exit()
        # Create the database user with permissions to access the new database.
        self.__create_user()
    
    def __add_data(self):
        print("[SAM] Adding content to the database...")
        if (ROOT_WITH_PSW):
            ins = " mysql -u"+self.master+" -p"+self.master_psw+" < " + DB_DATA
        else:
            ins = " mysql -u"+self.master+" < "+DB_DATA

        if (os.system(ins) != 0): exit()


if __name__ == "__main__":
    database = Database()
