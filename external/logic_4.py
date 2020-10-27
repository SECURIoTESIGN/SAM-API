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
    
    if get_answer_content(session, 0) == 'Android Application':
        confidentiality = 1
        privacy = 1
        integrity = 1
        accountability = 1
        authentication = 1
        authorization = 1

    if get_answer_content(session, 0) == 'iOS Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        integrity = 1
        accountability = 1

    if get_answer_content(session, 0) == 'Hybrid Application':
        authentication = 1
        authorization = 1
        confidentiality = 1
        integrity = 1
        availability = 1
        reliability = 1
        accountability = 1
        
    if get_answer_content(session, 0) == 'Sailfish OS Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    if get_answer_content(session, 0) == 'Tizen Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    if get_answer_content(session, 0) == 'Ubuntu Touch Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    if get_answer_content(session, 0) == 'Web Application':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1

    if get_answer_content(session, 1) == 'Game':
        confidentiality = 1
        availability = 1
        integrity = 1
        
    if get_answer_content(session, 1) == 'm-Commerce':
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

    if get_answer_content(session, 1) == 'm-Health':
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

    if get_answer_content(session, 1) == 'm-Learning':
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

    if get_answer_content(session, 1) == 'm-Payment':
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

    if get_answer_content(session, 1) == 'm-Social Networking':
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

    if get_answer_content(session, 1) == 'm-Tourism':
        confidentiality = 1
        integrity = 1
        availability = 1

    if get_answer_content(session, 1) == 'Multi-user Collaboration':
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

    if get_answer_content(session, 1) == 'Entertainment':
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

    if get_answer_content(session, 1) == 'Smart Agriculture':
        confidentiality = 1
        privacy = 1
        integrity = 1
        accountability = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        physicalSecurity = 1

    if get_answer_content(session, 1) == 'Smart Air Quality':
        authentication = 1
        authorization = 1
        confidentiality = 1
        integrity = 1
        availability = 1
        reliability = 1
        nonRepudiation = 1
        accountability = 1
        physicalSecurity = 1

    if get_answer_content(session, 1) == 'Smart Healthcare':
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

    if get_answer_content(session, 1) == 'Smart Home':
        confidentiality = 1
        privacy = 1
        authentication = 1
        authorization = 1
        availability = 1
        reliability = 1
        integrity = 1
        physicalSecurity = 1

    if get_answer_content(session, 2) == 'No Authentication':
        privacy = 0
        confidentiality = 0

    if get_answer_content(session, 2)== 'Username and Password':
        confidentiality = 0
        integrity = 0
        authentication = 1
        authorization = 0
        privacy = 0

    if get_answer_content(session, 2) == 'Social Networks/Google':
        confidentiality = 0
        integrity = 0
        authentication = 1
        privacy = 0

    if get_answer_content(session, 2) == 'Biometrics':
        confidentiality = 1
        integrity = 1
        authentication = 1
        privacy = 1

    if get_answer_content(session, 2) == 'Two Factor Authentication':
        confidentiality = 1
        integrity = 1
        authentication = 1
        privacy = 1

    if get_answer_content(session, 2) == 'Mult Factor Authentication':
        confidentiality = 1
        integrity = 1
        authentication = 1
        privacy = 1


    if get_answer_content(session, 3) == 'Yes':
        physicalSecurity = 1
        integrity = 1
        availability = 1
        forgeryResistance = 1
        authentication = 1
        nonRepudiation = 1

    if get_answer_content(session, 4) == 'Local Database (Device)':
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

    if get_answer_content(session, 4) == 'Remote Database':
        confidentiality = 1
        integrity = 1
        availability = 1
        authentication = 1
        dataOrigin = 1
        dataFreshness = 1
        physicalSecurity = 1
        authorization = 1

    if get_answer_content(session, 4) == 'Both':
        integrity = 1
        availability = 1
        dataFreshness = 1
        forgeryResistance = 1
        physicalSecurity = 1
        integrity = 1
        authentication = 1
        nonRepudiation = 1
        authorization = 1

    if get_answer_content(session, 5) == 'SQL':
        authentication = 1
        forgeryResistance = 1
        tamperDetection = 1
        authorization = 1

    if get_answer_content(session, 5) == 'NoSQL':
        authentication = 1
        forgeryResistance = 1
        tamperDetection = 1
        authorization = 1

    if get_answer_content(session, 6)== 'Personal Information (Names, Address,...)':
        confidentiality = 1
        privacy = 1
        physicalSecurity = 1
        authentication = 1

    if get_answer_content(session, 6) == 'Confidential Data':
        privacy = 1
        confidentiality = 1
        physicalSecurity = 1
        authorization = 1
        forgeryResistance = 1
        authentication = 1

    if get_answer_content(session, 6) == 'Critical Data':
        privacy = 1
        confidentiality = 1
        physicalSecurity = 1
        authorization = 1
        forgeryResistance = 1
        nonRepudiation = 1
        authentication = 1

    if (get_answer_content(session, 6) == 'All'):
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

    if get_answer_content(session, 7)== 'Yes':
        authentication = 1
        nonRepudiation = 1
    if get_answer_content(session, 8) == 'The users will register themselves':
        authentication = 1
        nonRepudiation = 1
    if get_answer_content(session, 8) == 'Will be an administrator that will register the users':
        authentication = 1
        nonRepudiation = 0
        privacy = 0

    if get_answer_content(session, 9) == 'C#':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authentication = 1
        authorization = 1

    if get_answer_content(session, 9) == 'C/C++' or get_answer_content(session, 9) == 'Objective C':
        confidentiality = 0
        integrity = 0
        privacy = 0
        authentication = 0
        authorization = 0

    if get_answer_content(session, 9) == 'HTML5 + CSS + JavaScript':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authorization = 1
        authorization = 1

    if get_answer_content(session, 9) == 'Java (Android)':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authentication = 1
        authorization = 1

    if get_answer_content(session, 9) == 'Kotlin' or get_answer_content(session, 9) == 'Python':
        confidentiality = 1
        integrity = 1
        privacy = 1
        authentication = 1
        authorization = 1

    if get_answer_content(session, 12) == 'Yes':
        authorization = 1
        confinement = 1
        dataOrigin = 1

    if get_answer_content(session, 13) == 'Yes':
        privacy = 1
        confidentiality = 1
        reliability = 1
        integrity = 1
        authentication = 1
        authorization = 1
        nonRepudiation = 1

    if get_answer_content(session, 14) == 'Yes':
        authentication = 1
        interoperability = 1
        confinement = 1
        tamperDetection = 1

    if get_answer_content(session, 15) == 'Yes':
        confinement = 1
        interoperability = 1

    if get_answer_content(session, 16) == 'Community Cloud (Remote connection)':
        privacy = 1
        integrity = 1
        authorization = 1
        availability = 1
        confidentiality = 1
        nonRepudiation = 1

    if get_answer_content(session, 16) == 'Public Cloud (Remote connection)':
        privacy = 1
        integrity = 1
        authorization = 1
        availability = 1
        confidentiality = 1
        nonRepudiation = 1

    if (get_answer_content(session, 16) == 'Private Cloud (Local connection)'):
        privacy = 1
        integrity = 1
        authorization = 1
        availability = 0
        confidentiality = 1
        nonRepudiation = 1

    if (get_answer_content(session, 16) == 'Hybrid Cloud (Mix Connection)'):
        privacy = 0
        integrity = 1
        authorization = 1
        availability = 0
        confidentiality = 1
        nonRepudiation = 0

    if (get_answer_content(session, 16) == 'Virtual Private Cloud'):
        privacy = 0
        integrity = 0
        authorization = 1
        availability = 1
        confidentiality = 0
        nonRepudiation = 0

    if (get_answer_content(session, 17) == 'Yes'):
        physicalSecurity = 1

    if (get_answer_content(session, 18) == 'Yes'):
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

    print(requirements)
    return requirements


"""
[Summary]: Common method to get answer content from module.
[Arguments]: 
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $question_number$: An integer that declares the question number, array format (0, length-1).
[Returns]: Answer content for specified question.
"""
def get_answer_content(session, question_number):
    return session['questions'][question_number]['answer']['content']

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
    temp_recommendations= get_recommendations(session)
    print(temp_recommendations)
    final_recommendations= []
    for recm in temp_recommendations:
        final_recommendations.append(get_recommendation_id(recommendations, recm))
    print(final_recommendations)

    return final_recommendations

