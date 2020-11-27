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
import json

def recommendations_based_domain(application_domain):
    
    if (application_domain == "Smart Home"):
        # 1.1. Based on the answers, give an output or recomendation based on the available set of recomendations.
        append_secure("Confidentiality")
        append_secure("Privacy")
        append_secure("Integrity")
        append_secure("Accountability")
        append_secure("Authentication")
        append_secure("Authorization")
        append_secure("Availability")
        append_secure("Reliability")
        append_secure("Physical Security")

    elif (application_domain == "Smart Healthcare"):
        append_secure("Confidentiality")
        append_secure("Privacy")
        append_secure("Integrity")
        append_secure("Accountability")
        append_secure("Authentication")
        append_secure("Authorization")
        append_secure("Availability")
        append_secure("Reliability")
        append_secure("Physical Security")
        append_secure("Non-Repudiation")

    elif (application_domain == "Smart Manufacturing"):
        append_secure("Confidentiality")
        append_secure("Integrity")
        append_secure("Accountability")
        append_secure("Authentication")
        append_secure("Authorization")
        append_secure("Availability")
        append_secure("Reliability")
        append_secure("Physical Security")
        append_secure("Non-Repudiation")

    elif (application_domain == "Smart Wearables"):
        append_secure("Confidentiality")
        append_secure("Integrity")
        append_secure("Privacy")
        append_secure("Authentication")
        append_secure("Authorization")
        append_secure("Availability")
        append_secure("Reliability")
        append_secure("Physical Security")

    elif (application_domain == "Smart Toy"):
        append_secure("Confidentiality")
        append_secure("Integrity")
        append_secure("Privacy")
        append_secure("Authentication")
        append_secure("Tamper Detection")
        append_secure("Availability")

    elif (application_domain == "Smart Transportation"):
        append_secure("Confidentiality")
        append_secure("Integrity")
        append_secure("Privacy")
        append_secure("Authentication")
        append_secure("Authorization")
        append_secure("Availability")
        append_secure("Non-Repudiation")
        append_secure("Accountability")
        append_secure("Reliability")
        append_secure("Physical Security")

def recommendations_based_user(user_login, user_information, kind_information, level_information, send_information):
    
    if (user_login == "Yes"):
        append_secure("Authentication")
        append_secure("Non-Repudiation")
    else:
        remove_secure("Authentication")
        remove_secure("Non-Repudiation")

    if (user_information == "Yes"):
        append_secure("Privacy")
        append_secure("Confidentiality")
    else:
        remove_secure("Privacy")
        remove_secure("Confidentiality")

    if (kind_information == "Yes"):
        append_secure("Privacy")
        append_secure("Confidentiality")
    else:
        remove_secure("Privacy")
        remove_secure("Confidentiality")

    if (level_information == "Normal Information"):
        append_secure("Privacy")
        append_secure("Confidentiality")
        append_secure("Physical Security")

    elif (level_information == "Sensitive Information"):
        append_secure("Privacy")
        append_secure("Confidentiality")
        append_secure("Physical Security")
        append_secure("Authorization")
        append_secure("Forgery Resistance")
        append_secure("Authentication")

    elif (level_information == "Critical Information"):
        append_secure("Privacy")
        append_secure("Confidentiality")
        append_secure("Physical Security")
        append_secure("Authorization")
        append_secure("Forgery Resistance")
        append_secure("Authentication")
        append_secure("Non-Repudiation")

    if (send_information == "Yes"):
        append_secure("Authentication")
        append_secure("Non-Repudiation")
        append_secure("Confinement")

def recommendations_based_internet(internet_connection, data_cloud="No"):

    if (internet_connection == "Yes"):
        append_secure("Non-Repudiation")
        append_secure("Accountability")
        append_secure("Reliability")
    
    if (data_cloud == "Yes"):
        append_secure("Integrity")
        append_secure("Availability")
        append_secure("Data Freshness")
        append_secure("Forgery Resistance")
        append_secure("Non-Repudiation")
        append_secure("Authentication")

def recommendations_based_database(database):
    if (database == "Yes"):
        append_secure("Physical Security")
        append_secure("Integrity")
        append_secure("Availability")
        append_secure("Forgery Resistance")
        append_secure("Authentication")
        append_secure("Non-Repudiation")

def recommendations_based_updates(regular_update):
    if (regular_update == "Yes"):
        append_secure("Availability")

def recommendations_based_third_party(third_party_soft):
    if (third_party_soft == "Yes"):
        append_secure("Confinement")
        append_secure("Interoperability")

def recommendations_based_eavesdrop(eavesdrop):
    if (eavesdrop == "Yes"):
        append_secure("Authorization")

def recommendations_based_capture_messages(message_capture_resent):
    if (message_capture_resent == "Yes"):
        append_secure("Data Origin")
        append_secure("Data Freshness")

def recommendations_based_impersonation(impersonate_user):
    if (impersonate_user == "Yes"):
        append_secure("Authentication")

def recommendations_based_access_private(obtain_private_info):
    if (obtain_private_info == "Yes"):
        append_secure("Physical Security")

def recommendations_based_system_mod(modify_system):
    if (modify_system == "Yes"):
        append_secure("Tamper Detection")        


"""
[Summary]: Method to remove from the recommendations list safely (if the ID doesn't exist, it won't be removed).
[Arguments]: 
    - $recommendation_name$: A string that contains the recommendation name.
[Returns]: None.
"""
def remove_secure(recommendation_name):
    global returned_recommendations, security_requirements

    returned_recommendations.remove(security_requirements[recommendation_name]) if security_requirements[recommendation_name] in returned_recommendations else None

"""
[Summary]: Method to append to the recommendations list safely (if the ID already exists, it won't be added).
[Arguments]: 
    - $recommendation_name$: A string that contains the recommendation name.
[Returns]: None.
"""
def append_secure(recommendation_name):
    global returned_recommendations, security_requirements

    returned_recommendations.append(security_requirements[recommendation_name]) if not (security_requirements[recommendation_name] in returned_recommendations) else None

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

"""
[Summary]: Common method to get answer content from session.
[Returns]: Answer content for specified question.
"""
def get_answer_content():
    global answer_num, _session

    answers = _session['questions'][answer_num]['answer']
    if len(answers) == 1:
        answer = answers[0]['content']
    else:
        answer = []
        for ans in answers:
            answer.append(ans['content'])

    answer_num += 1
    return answer

"""
[Summary]: Default SAM's logic main method.
[Arguments]:
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $recommendations$: Array of Python objects that includes information about the available set of recommendations (see example above).
[Returns]: MUST return an array of recommendation IDs.
"""
def run(session, recommendations):
    global returned_recommendations, security_requirements, _session, answer_num
    # This is the default array that will contain the list of recommendation IDs (integers), the array must be populated after some logic (see below for an example).
    _session = session
    returned_recommendations = []
    security_requirements = {}
    answer_num = 0

    # 1. Do some logic with the answers given by the user to one or more questions for the current parsed module. 
    security_requirements = {
        "Authentication": get_recommendation_id(recommendations, "Authentication"),
        "Confidentiality": get_recommendation_id(recommendations, "Confidentiality"),
        "Integrity": get_recommendation_id(recommendations, "Integrity"),
        "Availability": get_recommendation_id(recommendations, "Availability"),
        "Authorization": get_recommendation_id(recommendations, "Authorization"),
        "Non-Repudiation": get_recommendation_id(recommendations, "Non-Repudiation"),
        "Accountability": get_recommendation_id(recommendations, "Accountability"),
        "Reliability": get_recommendation_id(recommendations, "Reliability"),
        "Privacy": get_recommendation_id(recommendations, "Privacy"),
        "Physical Security": get_recommendation_id(recommendations, "Physical Security"),
        "Forgery Resistance": get_recommendation_id(recommendations, "Forgery Resistance"),
        "Tamper Detection": get_recommendation_id(recommendations, "Tamper Detection"),
        "Data Freshness": get_recommendation_id(recommendations, "Data Freshness"),
        "Confinement": get_recommendation_id(recommendations, "Confinement"),
        "Interoperability": get_recommendation_id(recommendations, "Interoperability"),
        "Data Origin": get_recommendation_id(recommendations, "Data Origin"),
    }

    application_domain = get_answer_content()
    recommendations_based_domain(application_domain)

    system_user = get_answer_content()
    if (system_user == "Yes"):
        user_login = get_answer_content()
        user_information = get_answer_content()
        kind_information = get_answer_content()
        level_information = get_answer_content()
        send_information = get_answer_content()
        recommendations_based_user(user_login, user_information, kind_information, level_information, send_information)

    internet_connection = get_answer_content()
    if (internet_connection == "Yes"):
        data_cloud = get_answer_content()
        recommendations_based_internet(internet_connection, data_cloud)
    else:
        recommendations_based_internet(internet_connection)

    database = get_answer_content()
    recommendations_based_database(database)

    regular_update = get_answer_content()
    recommendations_based_updates(regular_update)

    third_party_soft = get_answer_content()
    recommendations_based_third_party(third_party_soft)

    eavesdrop = get_answer_content()
    recommendations_based_eavesdrop(eavesdrop)

    message_capture_resent = get_answer_content()
    recommendations_based_capture_messages(message_capture_resent)

    impersonate_user = get_answer_content()
    recommendations_based_impersonation(impersonate_user)

    obtain_private_info = get_answer_content()
    recommendations_based_access_private(obtain_private_info)

    modify_system = get_answer_content()
    recommendations_based_system_mod(modify_system)

    return(returned_recommendations)