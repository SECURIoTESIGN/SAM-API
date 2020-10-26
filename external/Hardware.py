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
##############################################################################
                        SAM - LOGIC EXAMPLE FILE
##############################################################################  
"""
import json
import pandas as pd

sensitive_domains = ["Smart Healthcare", "Connected Car", "Smart Pet Monitoring", "Smart Environmental Monitoring", "Smart Automotive/Transportation", "Smart Agriculture", "Smart Retail", "Industrial Automation", "Smart Supply Chain", "Smart Banking/Financial applications", "Smart Elderly Monitoring", "Smart Kid Monitoring", "Smart Grid", "Smart City", "Smart Home"]
stream_ciphers = ["Continuous", "Unknown"]

def hardware_implementation(csv_filename, recommendations, security_requirements, circuit_area_requirement, throughput_requirement, stream_cipher, sensitive_domain, hardware_type, energy_performance):
    p_recommendations = []

    data = pd.read_csv(csv_filename, na_filter=False, delimiter=',', quotechar='"')
    for security_requirement in security_requirements:
        
        no_rcmd_name = "No algorithm for "+security_requirement.lower()
        no_rcmd_id = get_recommendation_id(recommendations, no_rcmd_name)
        p_recommendations.append(no_rcmd_id)

        for row in data.values:
            security_requirement_req = row[0]
            stream_cipher_req = None if row[1] == ' ' else bool(int(row[1]))
            sensitive_domain_req = bool(int(row[2]))
            circuit_area_min = float(row[3])
            circuit_area_max = float(row[4])
            throughput_min = float(row[5])
            throughput_max = float(row[6])
            hardware_type_req = str(row[7])
            energy_performance_req = str(row[8])
            rcmd_id = get_recommendation_id(recommendations, row[9])

            # We found a match for your system
            if security_requirement == security_requirement_req and (stream_cipher_req == None or stream_cipher == stream_cipher_req) and sensitive_domain == sensitive_domain_req and (circuit_area_requirement <= circuit_area_max and circuit_area_requirement >= circuit_area_min) and (throughput_requirement <= throughput_max and throughput_requirement >= throughput_min) and hardware_type == hardware_type_req and energy_performance == energy_performance_req:
                print('Match')
                p_recommendations.remove(no_rcmd_id)
                p_recommendations.append(rcmd_id)
                break

    return p_recommendations

"""
[Summary]: Evaluates if the user's application needs to use stream cipher or block cipher.
[Arguments]: 
    - $payload_size$: The user answer to the question "Select payload size".
[Returns]: True or False according to whether it need or not a stream cipher.
"""
def need_stream_cipher(payload_size):
    global stream_ciphers

    return payload_size in stream_ciphers

"""
[Summary]: Evaluates if the user's application belongs to a sensitive domain.
[Arguments]: 
    - $application_area$: The user answer to the question "Select application area".
[Returns]: True or False according to whether it belongs or not to a sensitive domain.
"""
def belongs_sensitive_domain(application_area):
    global sensitive_domains

    return application_area in sensitive_domains

"""
[Summary]: Common method to get answer content from session.
[Arguments]: 
    - $session$: A JSON Object that includes information about a session, including questions and user selected and/or user inputted answers.
    - $question_number$: An integer that declares the question number, array format (0, length-1).
[Returns]: Answer content for specified question.
"""
def get_answer_content(session, question_number):
    return session['questions'][question_number]['answer']['content']

"""
[Summary]: Common method to get recommendations from a dependency module.
[Arguments]: 
    - $session$: A JSON Object that includes information about a session, including questions and user selected and/or user inputted answers.
    - $dependency_number$: An integer that declares the dependency number, array format (0, length-1).
[Returns]: A JSON Object that includes information about dependency module's recommendations.
"""
def get_dependency_recommendations(session, dependency_number):
    return session['dependencies'][dependency_number]['module']['last_session']['recommendations']

"""
[Summary]: Common method to get recommendation content from recommendations.
[Arguments]: 
    - $recommendations$: A JSON Object that includes information about recommendations from a different module.
[Returns]: List of recommendations from a module.
"""
def get_recommendation_content(recommendations):
    recmd_content = []
    for recommendation in recommendations:
        recmd_content.append(recommendation['content'])
    return recmd_content

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
    - $session$: A JSON Object that includes information about a session, including questions and user selected and/or user inputted answers.
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: MUST return an array of recommendation IDs.
"""
def run(session, recommendations):
    hardware_type = get_answer_content(session, 1)
    energy_performance = get_answer_content(session, 2)
    circuit_area_requirement = float(get_answer_content(session, 3))
    throughput_requirement = float(get_answer_content(session, 4))
    application_area = get_answer_content(session, 5)
    payload_size = get_answer_content(session, 6)

    sre_dependency_recommendations = get_dependency_recommendations(session, 0)
    security_requirements = get_recommendation_content(sre_dependency_recommendations)

    if "Confidentiality" in security_requirements and "Authenticity" in security_requirements:
        security_requirements.remove('Confidentiality')
        security_requirements.remove('Authenticity')
        security_requirements.append('Confidentiality,Authenticity')

    sensitive_domain = belongs_sensitive_domain(application_area)    
    stream_cipher = need_stream_cipher(payload_size)

    csv_filename = 'external/conditions_hardware.csv'

    return hardware_implementation(csv_filename, recommendations, security_requirements, circuit_area_requirement, throughput_requirement, stream_cipher, sensitive_domain, hardware_type, energy_performance)