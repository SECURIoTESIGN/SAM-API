"""
// ---------------------------------------------------------------------------
//
//	Security Advising Modules (SAM) for Cloud IoT and Mobile Ecosystem
//
//  Copyright (C) 2021 Instituto de Telecomunicações (www.it.pt)
//  Copyright (C) 2021 Universidade da Beira Interior (www.ubi.pt)
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

################################# GLOBAL VARIABLES #################################
vulnerabilities_dict = {
"CWE-20": "Improper Input Validation",
"CWE-22": "Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')",
"CWE-74": "Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')",
"CWE-78": "Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')",
"CWE-79": "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')",
"CWE-89": "Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')",
"CWE-94": "Improper Control of Generation of Code ('Code Injection')",
"CWE-98": "Improper Control of Filename for Include/Require Statement in PHP Program",
"CWE-119": "Improper Restriction of Operations within the Bounds of a Memory Buffer",
"CWE-125": "Out-of-bounds Read",
"CWE-170": "Improper Null Termination",
"CWE-190": "Integer Overflow or Wraparound",
"CWE-200": "Exposure of Sensitive Information to an Unauthorized Actor",
"CWE-248": "Uncaught Exception",
"CWE-252": "Unchecked Return Value",
"CWE-269": "Improper Privilege Management",
"CWE-287": "Improper Authentication",
"CWE-306": "Missing Authentication for Critical Function",
"CWE-327": "Use of a Broken or Risky Cryptographic Algorithm",
"CWE-330": "Use of Insufficiently Random Values",
"CWE-352": "Cross-Site Request Forgery (CSRF)",
"CWE-400": "Uncontrolled Resource Consumption",
"CWE-404": "Improper Resource Shutdown or Release",
"CWE-416": "Use After Free",
"CWE-434": "Unrestricted Upload of File with Dangerous Type",
"CWE-441": "Unintended Proxy or Intermediary ('Confused Deputy')",
"CWE-469": "Use of Pointer Subtraction to Determine Size",
"CWE-476": "NULL Pointer Dereference",
"CWE-477": "Use of Obsolete Function",
"CWE-479": "Signal Handler Use of a Non-reentrant Function",
"CWE-502": "Deserialization of Untrusted Data",
"CWE-515": "Covert Storage Channel",
"CWE-522": "Insufficiently Protected Credentials",
"CWE-544": "Missing Standardized Error Handling Mechanism",
"CWE-573": "Improper Following of Specification by Caller",
"CWE-611": "Improper Restriction of XML External Entity Reference",
"CWE-625": "Permissive Regular Expression",
"CWE-668": "Exposure of Resource to Wrong Sphere",
"CWE-705": "Incorrect Control Flow Scoping",
"CWE-732": "Incorrect Permission Assignment for Critical Resource",
"CWE-758": "Reliance on Undefined, Unspecified, or Implementation-Defined Behavior",
"CWE-778": "Insufficient Logging",
"CWE-787": "Out-of-bounds Write",
"CWE-798": "Use of Hard-coded Credentials",
"CWE-840": "Business Logic Errors",
"CWE-862": "Missing Authorization",
"CWE-913": "Improper Control of Dynamically-Managed Code Resources",
"CWE-1069": "Empty Exception Block",
"CWE-1109": "Use of Same Variable for Multiple Purposes",
"CWE-1209": "Failure to Disable Reserved Bits",
"CWE-1220": "Insufficient Granularity of Access Control",
"CWE-1221": "Incorrect Register Defaults or Module Parameters",
"CWE-1224": "Improper Restriction of Write-Once Bit Fields",
"CWE-1242": "Inclusion of Undocumented Features or Chicken Bits",
"CWE-1244": "Improper Access to Sensitive Information Using Debug and Test Interfaces",
"CWE-1245": "Improper Finite State Machines (FSMs) in Hardware Logic",
"CWE-1247": "Missing or Improperly Implemented Protection Against Voltage and Clock Glitches",
"CWE-1251": "Mirrored Regions with Different Values",
"CWE-1253": "Incorrect Selection of Fuse Values",
"CWE-1255": "Comparison Logic is Vulnerable to Power Side-Channel Attacks",
"CWE-1261": "Improper Handling of Single Event Upsets",
"CWE-1262": "Register Interface Allows Software Access to Sensitive Data or Security Settings",
"CWE-1263": "Improper Physical Access Control",
"CWE-1267": "Policy Uses Obsolete Encoding",
"CWE-1268": "Policy Privileges are not Assigned Consistently Between Control and Data Agents",
"CWE-1271": "Uninitialized Value on Reset for Registers Holding Security Settings",
"CWE-1273": "Device Unlock Credential Sharing",
"CWE-1274": "Insufficient Protections on the Volatile Memory Containing Boot Code",
"CWE-1276": "Hardware Child Block Incorrectly Connected to Parent System",
"CWE-1277": "Firmware Not Updateable",
"CWE-1278": "Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit Imaging Techniques",
"CWE-1279": "Cryptographic Operations are run Before Supporting Units are Ready",
"CWE-1280": "Access Control Check Implemented After Asset is Accessed",
"CWE-1281": "Sequence of Processor Instructions Leads to Unexpected Behavior (Halt and Catch Fire)",
"CWE-1282": "Assumed-Immutable Data is Stored in Writable Memory",
"CWE-1291": "Public Key Re-Use for Signing both Debug and Production Code",
"CWE-1294": "Insecure Security Identifier Mechanism",
"CWE-1295": "Debug Messages Revealing Unnecessary Information",
"CWE-1296": "Incorrect Chaining or Granularity of Debug Components",
"CWE-1297": "Unprotected Confidential Information on Device is Accessible by OSAT Vendors",
"CWE-1298": "Hardware Logic Contains Race Conditions",
"CWE-1299": "Missing Protection Mechanism for Alternate Hardware Interface",
"CWE-1304": "Improperly Preserved Integrity of Hardware Configuration State During a Power Save/Restore Operation",
"CWE-1310": "Missing Ability to Patch ROM Code",
"CWE-1311": "Improper Translation of Security Attributes by Fabric Bridge",
"CWE-1313": "Hardware Allows Activation of Test or Debug Logic at Runtime",
"CWE-1319": "Improper Protection against Electromagnetic Fault Injection (EM-FI)",
"CWE-1326": "Missing Immutable Root of Trust in Hardware",
"CWE-1331": "Improper Isolation of Shared Resources in Network On Chip",
"CWE-1334": "Unauthorized Error Injection Can Degrade Hardware Redundancy",
"CWE-1338": "Improper Protections Against Hardware Overheating",
}

top_n_vulnerabilities = ["CWE-79", "CWE-787", "CWE-20", "CWE-125", "CWE-119", "CWE-89", "CWE-200", "CWE-416", "CWE-352", "CWE-78", "CWE-190", "CWE-22", "CWE-476", "CWE-287", "CWE-434", "CWE-732", "CWE-94", "CWE-522", "CWE-611", "CWE-798", "CWE-502", "CWE-269", "CWE-400", "CWE-306", "CWE-862", "CWE-98", "CWE-170", "CWE-252", "CWE-327", "CWE-330", "CWE-404", "CWE-441", "CWE-479", "CWE-573", "CWE-625", "CWE-705", "CWE-758", "CWE-778", "CWE-1244", "CWE-1247", "CWE-1274", "CWE-1281", "CWE-1295", "CWE-1296", "CWE-1299"]

################################# FUNCTIONS #################################

"""
[Summary]: Common method to get answer content from module, based on the question text.
[Arguments]: 
    - $questions$: A JSON Object that includes the last session questions of a module.
    - $question_text$: An integer that contains the ID (in DB) of the question.
[Returns]: Answer content for specified question.
"""
def get_answer_content(questions, question_id):
    for question in questions:
        if question['id'] == question_id:
            answers = question['answer']
            if len(answers) == 1:
                answer = answers[0]['content']
            else:
                answer=[]
                for ans in answers:
                    answer.append(ans['content'])
            return answer
    
    return []

"""
[Summary]: Common method to get recommendation id by comparing his content with the recommendation name.
[Arguments]: 
    - $recommendations$: A JSON Object that includes information about recommendations.
    - $recommendation_name$: A string that contains a recommendation name (content in JSON).
[Returns]: Recommendation ID.
"""
def get_recommendation_id(recommendations, recommendation_name):
    for recm in recommendations:
        if recm['content'] == recommendation_name:
            return recm['id']

    return None

"""
[Summary]: Common method to get answers from a dependency module.
[Arguments]: 
    - $number_id$: A integer that contains the dependency module ID.
[Returns]: Set of answers.
"""
def get_module_answers(number_id, session):
    modules = session['dependencies']
    for i in range(len(modules)):
        module = modules[i]['module']
        if module['id'] == number_id:
            return module

    return {}

"""
[Summary]: Common method to add recommendation.
[Arguments]: 
    - $recm_list$: A list containing the recommendations ID.
    - $recm$: A string that contains the recommendation abbreviation text.
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: List of recommendations.
"""
def add_recommendation(recm_list, recm_abbv, recommendations):
    recm = vulnerabilities_dict[recm_abbv]
    recm_id = get_recommendation_id(recommendations, recm)
    if recm_id not in recm_list:
        recm_list.append(recm_id)

"""
[Summary]: Common method to order recommendations by their priority.
[Arguments]: 
    - $recm_list$: A list containing the recommendations ID.
[Returns]: List of ordered recommendations.
"""
def order_by_top_n(recm_list):
    top_recm_list = []
    bot_recm_list = []
    for recm in recm_list:
        if recm in top_n_vulnerabilities:
            top_recm_list.append(recm)
        else:
            bot_recm_list.append(recm)

    return (top_recm_list + bot_recm_list)

"""
[Summary]: Method to output recommendations considering user answers.
[Arguments]: 
    - $SRE_answers$: A list containing the answers given to the SRE module.
    - $SBP_answers$: A list containing the answers given to the SBP module.
    - $TMS_answers$: A list containing the answers given to the TMS module.
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: List of ordered recommendations.
"""   
def retrieve_vulnerabilities(SRE_answers, SBP_answers, TMS_answers, recommendations):
    ## Security Requirements Elicitation Answers
    answers = SRE_answers
    domain = get_answer_content(answers, 1)
    user = get_answer_content(answers, 2)
    if user.lower() == "yes":
        login = get_answer_content(answers, 3)
        sent_entity = get_answer_content(answers, 7)
    database = get_answer_content(answers, 10)
    regular_update = get_answer_content(answers, 11)
    third_party = get_answer_content(answers, 12)
    eavesdrop = get_answer_content(answers, 13)
    impersonate = get_answer_content(answers, 15)
    priv_info = get_answer_content(answers, 16)
    modify_hard = get_answer_content(answers, 17)

    ## Security Best Practices Guidelines Answers
    answers = SBP_answers
    db = get_answer_content(answers, 19)
    if db.lower() == "yes":
        type_data = get_answer_content(answers, 20)
    user_regis = get_answer_content(answers, 24)
    prog_lang = get_answer_content(answers, 26)
    input_form = get_answer_content(answers, 27)
    if input_form.lower() == "yes":
        upload_file = get_answer_content(answers, 28)
    logs = get_answer_content(answers, 29)

    ## Threat Modeling Solution Answers
    answers = TMS_answers
    crypto_algo = get_answer_content(answers, 96)
    priv_escal = get_answer_content(answers, 97)
    xml_store = get_answer_content(answers, 98)
    standard_err = get_answer_content(answers, 116)
    HDL = get_answer_content(answers, 104)
    OSAT_ent = get_answer_content(answers, 105)
    documented = get_answer_content(answers, 106)
    add_hard_unit = get_answer_content(answers, 107)
    isolation = get_answer_content(answers, 108)
    vuln_impl = get_answer_content(answers, 109)
    if vuln_impl.lower() == "yes":
        eval_behav = get_answer_content(answers, 110)
        code_review = get_answer_content(answers, 111)
        if code_review.lower() == "no":
            immutable_data = get_answer_content(answers, 112)
        spec_third_party = get_answer_content(answers, 113)
        protect_sens_code = get_answer_content(answers, 114)
        debug_funct = get_answer_content(answers, 115)

    ## Logic
    recms = []
    if domain.lower() == "smart healthcare" or domain.lower() == "smart wearables" or domain.lower() == "smart toys" or domain.lower() == "smart transportation":
        add_recommendation(recms, 'CWE-400', recommendations)
    
    if user.lower() == "yes":
        add_recommendation(recms, 'CWE-287', recommendations)
        add_recommendation(recms, 'CWE-522', recommendations)
        add_recommendation(recms, 'CWE-798', recommendations)

        if login.lower() == "yes":
            add_recommendation(recms, 'CWE-1273', recommendations)

        if sent_entity.lower() == "yes":
            add_recommendation(recms, 'CWE-758', recommendations)
            add_recommendation(recms, 'CWE-515', recommendations)
            add_recommendation(recms, 'CWE-1294', recommendations)

    if database.lower() == "yes":
        add_recommendation(recms, 'CWE-200', recommendations)
        add_recommendation(recms, 'CWE-306', recommendations)
        add_recommendation(recms, 'CWE-862', recommendations)

    if regular_update.lower() == "yes":
        add_recommendation(recms, 'CWE-1277', recommendations)

    if third_party.lower() == "yes":
        add_recommendation(recms, 'CWE-269', recommendations)
        add_recommendation(recms, 'CWE-758', recommendations)
        add_recommendation(recms, 'CWE-1294', recommendations)

    if eavesdrop.lower() == "yes":
        add_recommendation(recms, 'CWE-200', recommendations)
        add_recommendation(recms, 'CWE-327', recommendations)

    if impersonate.lower() == "yes":
        add_recommendation(recms, 'CWE-441', recommendations)

    if priv_info.lower() == "yes":
        add_recommendation(recms, 'CWE-1255', recommendations)

    if modify_hard.lower() == "yes":
        add_recommendation(recms, 'CWE-1278', recommendations)
        add_recommendation(recms, 'CWE-1319', recommendations)
        add_recommendation(recms, 'CWE-1247', recommendations)
        add_recommendation(recms, 'CWE-1263', recommendations)
        add_recommendation(recms, 'CWE-1253', recommendations)
        add_recommendation(recms, 'CWE-1334', recommendations)

    if db.lower() == "yes":
        if type_data.lower() == "sql":
            add_recommendation(recms, 'CWE-89', recommendations)
            add_recommendation(recms, 'CWE-269', recommendations)

    if user_regis.lower() == "yes":
        add_recommendation(recms, 'CWE-287', recommendations)
        add_recommendation(recms, 'CWE-522', recommendations)
        add_recommendation(recms, 'CWE-269', recommendations)

    if "C/C++" in prog_lang:
        add_recommendation(recms, 'CWE-787', recommendations)
        add_recommendation(recms, 'CWE-125', recommendations)
        add_recommendation(recms, 'CWE-119', recommendations)
        add_recommendation(recms, 'CWE-416', recommendations)
        add_recommendation(recms, 'CWE-476', recommendations)
        add_recommendation(recms, 'CWE-469', recommendations)
        add_recommendation(recms, 'CWE-170', recommendations)
        add_recommendation(recms, 'CWE-248', recommendations)
        add_recommendation(recms, 'CWE-479', recommendations)
    
    elif "Java" in prog_lang:
        add_recommendation(recms, 'CWE-476', recommendations)
        add_recommendation(recms, 'CWE-502', recommendations)
        add_recommendation(recms, 'CWE-248', recommendations)
    
    elif "Python" in prog_lang:
        add_recommendation(recms, 'CWE-502', recommendations)

    elif "PHP" in prog_lang:
        add_recommendation(recms, 'CWE-502', recommendations)
        add_recommendation(recms, 'CWE-625', recommendations)
        add_recommendation(recms, 'CWE-98', recommendations)

    elif "Perl" in prog_lang:
        add_recommendation(recms, 'CWE-625', recommendations)

    elif "JavaScript" in prog_lang or "Ruby" in prog_lang:
        add_recommendation(recms, 'CWE-502', recommendations)

    elif "C#" in prog_lang:
        add_recommendation(recms, 'CWE-479', recommendations)
        add_recommendation(recms, 'CWE-248', recommendations)

    if input_form.lower() == "yes":
        add_recommendation(recms, 'CWE-79', recommendations)
        add_recommendation(recms, 'CWE-20', recommendations)
        add_recommendation(recms, 'CWE-352', recommendations)
        add_recommendation(recms, 'CWE-78', recommendations)
        add_recommendation(recms, 'CWE-22', recommendations)
        add_recommendation(recms, 'CWE-94', recommendations)
        add_recommendation(recms, 'CWE-74', recommendations)

        if upload_file.lower() == "yes":
            add_recommendation(recms, 'CWE-434', recommendations)

    if logs.lower() == "yes":
        add_recommendation(recms, 'CWE-778', recommendations)

    if crypto_algo.lower() == "yes":
        add_recommendation(recms, 'CWE-330', recommendations)
        add_recommendation(recms, 'CWE-327', recommendations)


    if priv_escal.lower() == "yes":
        add_recommendation(recms, 'CWE-269', recommendations)
        add_recommendation(recms, 'CWE-732', recommendations)
        add_recommendation(recms, 'CWE-306', recommendations)
        add_recommendation(recms, 'CWE-862', recommendations)
        add_recommendation(recms, 'CWE-1268', recommendations)


    if xml_store.lower() == "yes":
        add_recommendation(recms, 'CWE-611', recommendations)


    if standard_err.lower() == "no":
        add_recommendation(recms, 'CWE-544', recommendations)


    if HDL.lower() == "yes":
        add_recommendation(recms, 'CWE-1224', recommendations)
        add_recommendation(recms, 'CWE-1221', recommendations)
        add_recommendation(recms, 'CWE-1298', recommendations)
        add_recommendation(recms, 'CWE-1251', recommendations)
        add_recommendation(recms, 'CWE-1311', recommendations)
        add_recommendation(recms, 'CWE-1279', recommendations)
        add_recommendation(recms, 'CWE-1296', recommendations)
        add_recommendation(recms, 'CWE-1297', recommendations)
        add_recommendation(recms, 'CWE-1280', recommendations)
    

    if OSAT_ent.lower() == "yes":
        add_recommendation(recms, 'CWE-1297', recommendations)


    if documented.lower() == "no":
        add_recommendation(recms, 'CWE-1242', recommendations)


    if add_hard_unit.lower() == "yes":
        add_recommendation(recms, 'CWE-1279', recommendations)
        add_recommendation(recms, 'CWE-1338', recommendations)


    if isolation.lower() == "no":
        add_recommendation(recms, 'CWE-1331', recommendations)
        add_recommendation(recms, 'CWE-1261', recommendations)


    if vuln_impl.lower() == "yes":
        if eval_behav.lower() == "no":
            add_recommendation(recms, 'CWE-190', recommendations)
            add_recommendation(recms, 'CWE-705', recommendations)
            add_recommendation(recms, 'CWE-668', recommendations)
            add_recommendation(recms, 'CWE-913', recommendations)
            add_recommendation(recms, 'CWE-840', recommendations)
            add_recommendation(recms, 'CWE-1109', recommendations)
            add_recommendation(recms, 'CWE-252', recommendations)
            add_recommendation(recms, 'CWE-1069', recommendations)
            add_recommendation(recms, 'CWE-404', recommendations)
            add_recommendation(recms, 'CWE-1280', recommendations)
            add_recommendation(recms, 'CWE-1271', recommendations)
            add_recommendation(recms, 'CWE-1281', recommendations)
            add_recommendation(recms, 'CWE-1245', recommendations)
            add_recommendation(recms, 'CWE-1276', recommendations)

        if code_review.lower() == "no":
            add_recommendation(recms, 'CWE-477', recommendations)
            
            if immutable_data.lower() == "no":
                add_recommendation(recms, 'CWE-1282', recommendations)
                add_recommendation(recms, 'CWE-1304', recommendations)

        if spec_third_party.lower() == "no":
            add_recommendation(recms, 'CWE-573', recommendations)

        if protect_sens_code.lower() == "yes":
            add_recommendation(recms, 'CWE-1267', recommendations)
        else:
            add_recommendation(recms, 'CWE-1274', recommendations)
            add_recommendation(recms, 'CWE-1310', recommendations)
            add_recommendation(recms, 'CWE-1326', recommendations)
            add_recommendation(recms, 'CWE-1220', recommendations)
            add_recommendation(recms, 'CWE-1299', recommendations)
            add_recommendation(recms, 'CWE-1262', recommendations)
        
        if debug_funct.lower() == "no":
            add_recommendation(recms, 'CWE-1244', recommendations)
            add_recommendation(recms, 'CWE-1291', recommendations)
            add_recommendation(recms, 'CWE-1295', recommendations)
            add_recommendation(recms, 'CWE-1296', recommendations)
            add_recommendation(recms, 'CWE-1313', recommendations)

    return order_by_top_n(recms)

"""
[Summary]: Default SAM's logic main method.
[Arguments]:
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: MUST return an array of recommendation IDs.
"""
def run(session, recommendations):
    SRE_answers = get_module_answers(1, session)['last_session']['questions']
    SBP_answers = get_module_answers(2, session)['last_session']['questions']
    TMS_answers = session['questions']

    final_recommendations = retrieve_vulnerabilities(SRE_answers, SBP_answers, TMS_answers, recommendations)
    return final_recommendations

