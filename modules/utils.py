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
import hashlib, ast, codecs, os, shutil
from flask import jsonify
from flask.globals import session
import modules.error_handlers
from fpdf import FPDF

"""
[Summary]: Outputs a custom message to the terminal.
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
TODO: This function needs work. 
""" 
def build_sql_instruction(SQL, columns, values, where=None):
    if type(values) is tuple:
        values = [i for i in values if i]  # If exists, remove None values.
    else: 
        values = (str(values)) 
    
    columns  = [i for i in columns if i] 
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
        if (table_columns.rfind(")") == -1): table_columns += ")"
        if (table_values.rfind(")") == -1):  table_values += ")"
        
        SQL = SQL + " " + table_columns + table_values
    
    if ((str(SQL.lower()).find("update")) == 0):
        # Proc. columns 
        i = 0
        for column in columns:
            table_columns   += (i!=len(columns)-1) and (column +"=%s,") or (column +"=%s")
            i = i + 1
        SQL = SQL + " " + table_columns + table_values + " " + str(where)
    print(SQL)
    return(SQL, values)

"""
[Summary]: Check if an entry exists on the database
[Arguments]:
       - $SQL$: Barebones SQL instruction. For example, "Select id FROM User"
       - $columns$: List of columns of the table.
       - $values$: List of values of the SQL instruction.
[Returns]: the id of the entry if exists, -1 otherwise.
"""
def db_already_exists(mysql, SQL, values):
    DEBUG = True
    try:
        conn    = mysql.connect()
        cursor  = conn.cursor()
        if (DEBUG): console_log("db_already_exists", "SQL=" + SQL + " | values=" + str(values))
        cursor.execute(SQL, values)
        res = cursor.fetchall()
    except Exception as e:
        console_log("db_already_exists()", str(e), True)
        return(-1)
    
    # Check for empty results. 
    if (len(res) == 0):
        cursor.close()
        conn.close()
        return(-1)    
    else:
        primary_key_value = -1
        for row in res: 
            primary_key_value = int(row[0])
            break
        cursor.close()
        conn.close()
        return(primary_key_value)
    
    return(-1)

"""
[Summary]: Executes a SQL INSERT or UPDATE instruction
[Arguments]:
       - $SQL$: Barebones SQL instruction. For example, "INSERT INTO User"
       - $columns$: List of columns of the table.
       - $values$: List of values of the SQL instruction.
[Returns]: If it is an SQL Insert operation then the return value is the id of the last created entry. 
"""
def db_execute_update_insert(mysql, SQL, values, DEBUG=False):
    n_id = None
    try:
        if (DEBUG): console_log("db_execute_update_insert", "SQL=" + SQL + " | Values=" + str(values))
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

"""
[Summary]: Orders the questions, answered by user, based on the module tree.
[Returns]: Returns the ordered questions.
"""
def order_questions(tree, session_questions, ordered_questions=[]):
    for obj in tree:
        if obj['type'] == 'question':
            for question in session_questions:
                if question['id'] == obj['id']:
                    ordered_questions.append(question)
                    break

        for children in obj['children']:
            order_questions([children], session_questions, ordered_questions)
    
    return ordered_questions

"""
[Summary]: Class that helps building the PDF for module's recommendations.
"""
class PDF(FPDF):
    def __init__(self, module_name, session_num, image_dir):
        super().__init__()
        self.module_name = module_name
        self.session_num = session_num
        self.image_dir   = image_dir

        self.set_margins(left=35, top=35)
        self.set_auto_page_break(True, margin=30)

    def header(self):
        self.set_font('Helvetica', '', 5)
        self.cell(12, -24, 'Towards the assurance of SECURity by dESIGN of the Internet of Things', 0, 0, 'C')
        # Logo
        self.image(str(self.image_dir)+'project.png', 20, 18, 40)
        self.image(str(self.image_dir)+'logo.png', 160, 5, 30)
        self.ln(1)

    # Page footer
    def footer(self):
        self.image(str(self.image_dir)+'portugal2020.png', 37, 280, w=30)
        self.image(str(self.image_dir)+'fct.png', 77, 280, w=30)
        self.image(str(self.image_dir)+'compete2020.png', 109, 278, w=30)
        self.image(str(self.image_dir)+'feder.png', 144, 280, w=30)

        # Position at 3.7 cm from bottom
        self.set_y(-32)
        self.set_font('Helvetica', '', 6)
        # Project Information
        self.cell(0, 20, 'SAM - Security Advisory Modules © 2021 SECURIoTESIGN', 0, 0, 'C')
        # Page number
        self.cell(0, 20, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'R')

    def write_title(self):
        # Title
        self.set_font('Helvetica', 'B', 18)
        self.multi_cell(w=0, h=10, txt='Recommendations for ' + str(self.module_name), border=0, align='C', fill=False)
        # Session number
        self.set_font('Helvetica', '', 12)
        self.multi_cell(w=0, h=10, txt='Session ' + str(self.session_num), border=0, align='C')
        # Line break
        self.ln(10)

    def write_recommendation(self, recm):
        # Set font for recommendation title
        self.set_font('Helvetica', 'B', 14)
        # Write the recommendation title
        self.multi_cell(0, 8, recm['content'], 0)
        # Write the recommendation description
        if recm['description'] is not None:
            # Set font for recommendation description
            self.set_font('Helvetica', '', 12)
            self.multi_cell(0, 6, recm['description'], 0)
        # Add guide if needed
        if recm['recommendation_guide'] is not None:
            self.set_font('Helvetica', '', 8)
            self.multi_cell(0, 5, 'More information available at: ' + str(recm['recommendation_guide']), 0, 'R')
        # Add some space
        self.ln(5)
"""
[Summary]: Build the PDF for a specific module's session.
[Returns]: Returns True when the PDF is built.
"""
def build_recommendations_PDF(module_name, session_id, recommendations):
    pdf = PDF(module_name=module_name, session_num=session_id, image_dir='static/')
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.write_title()
    for recm in recommendations['recommendations']:
        pdf.write_recommendation(recm)
    pdf.output('temp/session'+str(session_id)+'/session'+str(session_id)+'.pdf', 'F')
    return True

def create_recommendations_ZIP(module_name, session_id):
    shutil.make_archive('temp/'+str(module_name)+'_session_'+str(session_id), 'zip', 'temp/session'+str(session_id))
    return True