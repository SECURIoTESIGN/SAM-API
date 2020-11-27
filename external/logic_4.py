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

def get_recommendations(session):
    requirements=[]

    confidentiality = 0
    integrity = 0
    availability = 0
    authentication = 0
    authorization = 0
    nonRepudiation = 0
    accountability = 0
    reliability = 0
    privacy = 0
    physicalSecurity = 0
    forgeryResistance = 0
    tamperDetection = 0
    dataFreshness = 0
    confinement = 0
    interoperability = 0
    dataOrigin = 0
    
    application_type = get_answer_content()

    if application_type == 'Android Application':
        confidentiality = 1
        privacy = 1
        integrity = 1
        accountability = 1
        authentication = 1
        authorization = 1

    if application_type == 'iOS Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        integrity = 1
        accountability = 1

    if application_type == 'Hybrid Application':
        authentication = 1
        authorization = 1
        confidentiality = 1
        integrity = 1
        availability = 1
        reliability = 1
        accountability = 1
        
    if application_type == 'Sailfish OS Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    if application_type == 'Tizen Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    if application_type == 'Ubuntu Touch Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    if application_type == 'Web Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    application_domain = get_answer_content()

    if application_domain == 'Game':
        confidentiality = 1
        availability = 1
        integrity = 1
        
    if application_domain == 'm-Commerce':
        confidentiality = 1
        integrity = 1
        availability = 1
        privacy = 1
        reliability = 1
        authentication = 1
        nonRepudiation = 1
        accountability = 1
        nonRepudiation = 1
        authorization = 1
        interoperability = 1
        forgeryResistance = 1

    if application_domain == 'm-Health':
        confidentiality = 1
        integrity = 1
        availability = 1
        privacy = 1
        reliability = 1
        authentication = 1
        nonRepudiation = 1
        accountability = 1
        nonRepudiation = 1
        authorization = 1
        interoperability = 1
        forgeryResistance = 1

    if application_domain == 'm-Learning':
        confidentiality =1
        integrity = 1
        availability = 1
        dataFreshness = 1
        forgeryResistance = 1
        nonRepudiation = 1
        authentication = 1
        reliability = 1
        accountability = 1
        authorization = 1
        interoperability = 1
        privacy = 1

    if application_domain == 'm-Payment':
        confidentiality = 1
        integrity = 1
        availability = 1
        dataFreshness = 1
        forgeryResistance = 1
        nonRepudiation = 1
        authentication = 1
        reliability = 1
        accountability = 1
        authorization = 1
        interoperability = 1
        privacy=1

    if application_domain == 'm-Social Networking':
        confidentiality = 1
        integrity = 1
        availability = 1
        dataFreshness = 1
        forgeryResistance = 1
        nonRepudiation = 1
        authentication = 1
        reliability = 1
        accountability = 1
        authorization = 1
        interoperability = 1
        privacy=1

    if application_domain == 'm-Tourism':
        confidentiality = 1
        integrity = 1
        availability = 1

    if application_domain == 'Multi-user Collaboration':
        confidentiality = 1
        integrity = 1
        availability = 1
        dataFreshness = 1
        forgeryResistance = 1
        authentication = 1
        reliability = 1
        accountability = 1
        authorization = 1
        privacy=1

    if application_domain == 'Entertainment':
        confidentiality = 1
        integrity = 1
        availability = 1
        dataFreshness = 1
        forgeryResistance = 1
        nonRepudiation = 1
        authentication = 1
        reliability = 1
        accountability = 1
        authorization = 1
        interoperability = 1
        privacy=1

    if application_domain == 'Smart Agriculture':
        confidentiality = 1
        privacy = 1
        integrity = 1
        accountability = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        physicalSecurity = 1

    if application_domain == 'Smart Air Quality':
        authentication = 1
        authorization = 1
        confidentiality = 1
        integrity = 1
        availability = 1
        reliability = 1
        nonRepudiation = 1
        accountability = 1
        physicalSecurity = 1

    if application_domain == 'Smart Healthcare':
        confidentiality = 1
        integrity = 1
        availability = 1
        authentication = 1
        authorization = 1
        nonRepudiation = 1
        accountability = 1
        reliability = 1
        privacy = 1
        physicalSecurity = 1

    if application_domain == 'Smart Home':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1
        physicalSecurity = 1

    authentication_method = get_answer_content()

    if authentication_method == 'No Authentication':
        privacy = 0
        confidentiality = 0

    if authentication_method == 'Username and Password':
        confidentiality = 0
        integrity = 0
        authentication = 1
        authorization = 0
        privacy = 0

    if authentication_method == 'Social Networks/Google':
        confidentiality = 0
        integrity = 0
        authentication = 1
        privacy = 0

    if authentication_method == 'Biometrics':
        confidentiality = 1
        integrity = 1
        authentication = 1
        privacy = 1

    if authentication_method == 'Two Factor Authentication':
        confidentiality = 1
        integrity = 1
        authentication = 1
        privacy = 1

    if authentication_method == 'Mult Factor Authentication':
        confidentiality = 1
        integrity = 1
        authentication = 1
        privacy = 1

    database_exists = get_answer_content()
    if database_exists == 'Yes':
        physicalSecurity = 1
        integrity = 1
        availability = 1
        forgeryResistance = 1
        authentication = 1
        nonRepudiation = 1

        place_database = get_answer_content()
        if place_database == 'Local Database (Device)':
            confidentiality = 1
            integrity = 1
            availability = 1
            authentication = 1
            authorization = 1
            dataOrigin = 1
            dataFreshness = 1
            privacy = 1
            forgeryResistance = 1
            physicalSecurity = 1

        if place_database == 'Remote Database':
            confidentiality = 1
            integrity = 1
            availability = 1
            authentication = 1
            dataOrigin = 1
            dataFreshness = 1
            physicalSecurity = 1
            authorization = 1

        if place_database == 'Both':
            integrity = 1
            availability = 1
            dataFreshness = 1
            forgeryResistance = 1
            physicalSecurity = 1
            integrity = 1
            authentication = 1
            nonRepudiation = 1
            authorization = 1

        type_database = get_answer_content()
        if type_database == 'SQL':
            authentication = 1
            forgeryResistance = 1
            tamperDetection = 1
            authorization = 1

        if type_database == 'NoSQL':
            authentication = 1
            forgeryResistance = 1
            tamperDetection = 1
            authorization = 1

        type_data_stored = get_answer_content()
        if type_data_stored == 'Personal Information (Names, Address,...)':
            confidentiality = 1
            privacy = 1
            physicalSecurity = 1
            authentication = 1

        if type_data_stored == 'Confidential Data':
            privacy = 1
            confidentiality = 1
            physicalSecurity = 1
            authorization = 1
            forgeryResistance = 1
            authentication = 1

        if type_data_stored == 'Critical Data':
            privacy = 1
            confidentiality = 1
            physicalSecurity = 1
            authorization = 1
            forgeryResistance = 1
            nonRepudiation = 1
            authentication = 1

        if (type_data_stored == 'All'):
            confidentiality = 1
            integrity = 1
            availability = 1
            authentication = 1
            authorization = 1
            nonRepudiation = 1
            accountability = 1
            reliability = 1
            privacy = 1
            physicalSecurity = 1
            forgeryResistance = 1
            tamperDetection = 1
            dataFreshness = 1
            confinement = 1
            interoperability = 1
            dataOrigin = 1

    user_registration = get_answer_content()
    if user_registration == 'Yes':
        authentication = 1
        nonRepudiation = 1

        way_registration = get_answer_content()
        if way_registration == 'The users will register themselves':
            authentication = 1
            nonRepudiation = 1
        if way_registration == 'Will be an administrator that will register the users':
            authentication = 1
            nonRepudiation = 0
            privacy = 0

    system_language = get_answer_content()
    if system_language == 'C#':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authentication = 1
        authorization = 1

    if system_language == 'C/C++' or system_language == 'Objective C':
        confidentiality = 0
        integrity = 0
        privacy = 0
        authentication = 0
        authorization = 0

    if system_language == 'HTML5 + CSS + JavaScript':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authorization = 1
        authorization = 1

    if system_language == 'Java (Android)':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authentication = 1
        authorization = 1

    if system_language == 'Kotlin' or system_language == 'Python':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authentication = 1
        authorization = 1

    server_language = get_answer_content()
    input_forms = get_answer_content()

    upload_files = get_answer_content()
    if upload_files == 'Yes':
        authorization = 1
        confinement = 1
        dataOrigin = 1

    regist_logs = get_answer_content()
    if regist_logs == 'Yes':
        privacy = 1
        confidentiality = 1
        reliability = 1
        integrity = 1
        authentication = 1
        authorization = 1
        nonRepudiation = 1

    regular_updates = get_answer_content()
    if regular_updates == 'Yes':
        authentication = 1
        interoperability = 1
        confinement = 1
        tamperDetection = 1

    third_party_software = get_answer_content()
    if third_party_software == 'Yes':
        confinement = 1
        interoperability = 1

    system_environment = get_answer_content()
    if system_environment == 'Community Cloud (Remote connection)':
        privacy = 1
        integrity = 1
        authorization = 1
        availability = 1
        confidentiality = 1
        nonRepudiation = 1

    if system_environment == 'Public Cloud (Remote connection)':
        privacy = 1
        integrity = 1
        authorization = 1
        availability = 1
        confidentiality = 1
        nonRepudiation = 1

    if (system_environment == 'Private Cloud (Local connection)'):
        privacy = 1
        integrity = 1
        authorization = 1
        availability = 0
        confidentiality = 1
        nonRepudiation = 1

    if (system_environment == 'Hybrid Cloud (Mix Connection)'):
        privacy = 0
        integrity = 1
        authorization = 1
        availability = 0
        confidentiality = 1
        nonRepudiation = 0

    if (system_environment == 'Virtual Private Cloud'):
        privacy = 0
        integrity = 0
        authorization = 1
        availability = 1
        confidentiality = 0
        nonRepudiation = 0

    physical_access = get_answer_content()
    if (physical_access == 'Yes'):
        physicalSecurity = 1

    modify = get_answer_content()
    if (modify == 'Yes'):
        tamperDetection = 1


    if confidentiality == 1 : 
        requirements.append('Confidentiality')
    if integrity == 1 : 
        requirements.append('Integrity')
    if availability == 1 : 
        requirements.append('Availability')
    if authentication == 1 : 
        requirements.append('Authentication')
    if authorization == 1 : 
        requirements.append('Authorization')
    if nonRepudiation == 1 : 
        requirements.append('Non-Repudiation')
    if accountability == 1 : 
        requirements.append('Accountability')
    if reliability == 1 : 
        requirements.append('Reliability')
    if privacy == 1 : 
        requirements.append('Privacy')
    if physicalSecurity == 1 : 
        requirements.append('Physical Security')
    if forgeryResistance == 1 : 
        requirements.append('Forgery Resistance')
    if tamperDetection == 1 : 
        requirements.append('Tamper Detection')
    if dataFreshness == 1 : 
        requirements.append('Data Freshness')
    if confinement == 1 : 
        requirements.append('Confinement')
    if interoperability == 1 : 
        requirements.append('Interoperability')
    if dataOrigin == 1 : 
        requirements.append('Data Origin')

    return requirements


"""
[Summary]: Common method to get answer content from module.
[Arguments]: 
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $question_number$: An integer that declares the question number, array format (0, length-1).
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
[Summary]: Default SAM's logic main method.
[Arguments]:
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: MUST return an array of recommendation IDs.
"""

def run(session, recommendations):
    global answer_num, _session 
    _session = session
    answer_num = 0

    temp_recommendations= get_recommendations(session)

    final_recommendations= []
    for recm in temp_recommendations:
        final_recommendations.append(get_recommendation_id(recommendations, recm))

    return final_recommendations

