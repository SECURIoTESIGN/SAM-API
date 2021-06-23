"""
// ---------------------------------------------------------------------------
//
//	Security Advising sessions (SAM) for Cloud IoT and Mobile Ecosystem
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
import csv

sensitive_domains = ["Smart Healthcare", "Connected Car", "Smart Pet Monitoring", "Smart Environmental Monitoring", "Smart Automotive/Transportation", "Smart Agriculture", "Smart Retail", "Industrial Automation", "Smart Supply Chain", "Smart Banking/Financial applications", "Smart Elderly Monitoring", "Smart Kid Monitoring", "Smart Grid", "Smart City", "Smart Home"]
stream_ciphers = ["Continuous", "Unknown"]

"""
[Summary]: Select the algorithm for each of the provided requirements, if the system already exists.
[Arguments]: 
    - $csv_filename$: CSV filename that provides the conditions to choose an algorithm (string).
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
    - $hardware_type$: Hardware type choosen by the user (string).
    - $flash_memory_size$: Flash memory size introduced by the user (integer).
    - $ram_size$: RAM size introduced by the user (integer).
    - $stream_cipher$: The user wants to use stream cipher (bool).
    - $sensitive_domain$: The system belongs to a sensitive domain (bool).
    - $security_requirements$: Security requirements the user wants to fulfill (array of strings).
[Returns]: An array containing the algorithm for each requirement, orderly.
"""
def select_requirement_algorithm_existing_system(csv_filename, recommendations, hardware_type, flash_memory_size, ram_size, sensitive_domain, stream_cipher, security_requirements):
    p_recommendations = []
    # No algorithm recommendation id
    no_algo_id = 413

    for security_requirement in security_requirements:
        with open(csv_filename, mode='r') as csv_file:
            data = csv.reader(csv_file, delimiter=',', quotechar='"')
            # Skip header
            next(data)
            for row in data:
                security_requirement_req = row[0]
                stream_cipher_req = None if row[1] == ' ' else bool(int(row[1]))
                sensitive_domain_req = bool(int(row[2]))
                flash_memory_size_max = int(row[3])
                flash_memory_size_min = int(row[4])
                ram_size_max = int(row[5])
                ram_size_min = int(row[6])
                hardware_type_req = None if row[1] == ' ' else str(row[7])
                rcmd_name = row[8]
                rcmd_id = get_recommendation_id(recommendations, rcmd_name)

                # Existing system
                if (security_requirement == security_requirement_req) and (stream_cipher_req == None or stream_cipher == stream_cipher_req) and (sensitive_domain == sensitive_domain_req) and (flash_memory_size <= flash_memory_size_max and flash_memory_size >= flash_memory_size_min) and (ram_size <= ram_size_max and ram_size >= ram_size_min) and (hardware_type_req == None or hardware_type == hardware_type_req):             
                    # If the recommendation says there is no algorithm
                    if "no algorithm" in rcmd_name.lower():
                        if len(p_recommendations) == 0 and no_algo_id not in p_recommendations:
                            p_recommendations.append(no_algo_id)
                        break
                    if rcmd_id not in p_recommendations:
                        p_recommendations.append(rcmd_id)
                        if no_algo_id in p_recommendations:
                            p_recommendations.remove(no_algo_id)
                        break

    if len(p_recommendations) == 0:
        p_recommendations.append(no_algo_id)

    return p_recommendations



"""
[Summary]: Select the algorithm for each of the provided requirements, if the system is being planned.
[Arguments]: 
    - $csv_filename$: CSV filename that provides the conditions to choose an algorithm (string).
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
    - $cpu_bits$: cpu architecture bit width choosen by the user (integer).
    - $flash_memory_size$: Flash memory size introduced by the user (integer).
    - $ram_size$: RAM size introduced by the user (integer).
    - $stream_cipher$: The user wants to use stream cipher (bool).
    - $sensitive_domain$: The system belongs to a sensitive domain (bool).
    - $security_requirements$: Security requirements the user wants to fulfill (array of strings).
[Returns]: An array containing the algorithm for each requirement, orderly.
"""
def select_requirement_algorithm_planning(csv_filename, recommendations, cpu_bits, flash_memory_size, ram_size, sensitive_domain, stream_cipher, security_requirements):

    p_recommendations = []
    # No algorithm recommendation id
    no_algo_id = 413

    for security_requirement in security_requirements:
        with open(csv_filename, mode='r') as csv_file:
            data = csv.reader(csv_file, delimiter=',', quotechar='"')
            # Skip header
            next(data)
            for row in data:
                security_requirement_req = row[0]
                stream_cipher_req = None if row[1] == ' ' else bool(int(row[1]))
                sensitive_domain_req = bool(int(row[2]))
                flash_memory_size_max = int(row[3])
                flash_memory_size_min = int(row[4])
                ram_size_max = int(row[5])
                ram_size_min = int(row[6])
                cpu_bits_req = int(row[7])
                rcmd_name = row[8]
                rcmd_id = get_recommendation_id(recommendations, rcmd_name)

                # Planning system
                if (security_requirement == security_requirement_req) and (stream_cipher_req == None or stream_cipher == stream_cipher_req) and (sensitive_domain == sensitive_domain_req) and (flash_memory_size <= flash_memory_size_max and flash_memory_size >= flash_memory_size_min) and (ram_size <= ram_size_max and ram_size >= ram_size_min) and cpu_bits >= cpu_bits_req:
                    # If the recommendation says there is no algorithm
                    if "no algorithm" in rcmd_name.lower():
                        if len(p_recommendations) == 0 and no_algo_id not in p_recommendations:
                            p_recommendations.append(no_algo_id)
                        break
                    if rcmd_id not in p_recommendations:
                        p_recommendations.append(rcmd_id)
                        if no_algo_id in p_recommendations:
                            p_recommendations.remove(no_algo_id)
                        break


    if len(p_recommendations) == 0:
        p_recommendations.append(no_algo_id)
        
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
    global answer_num, _session
    _session = session
    answer_num = 1

    existing_system = get_answer_content()
    hardware_type = get_answer_content()
    cpu_arch = get_answer_content()

    try:
        flash_memory_size = float(get_answer_content())
    except (ValueError, TypeError):
        raise Exception("Flash memory size must be a numeric value.")

    try: 
        ram_size = float(get_answer_content())
    except (ValueError, TypeError):
        raise Exception("RAM size must be a numeric value.")

    try:
        cpu = float(get_answer_content()) if cpu_arch == 'Other' else float(cpu_arch.split(sep="-", maxsplit=1)[0])
    except (ValueError, TypeError):
        raise Exception("CPU bit must be a numeric value.")

    try:
        cpu_clock = float(get_answer_content())
    except (ValueError, TypeError):
        raise Exception("CPU clock must be a numeric value.")

    application_area = get_answer_content()
    payload_size = get_answer_content()


    sre_dependency_recommendations = get_dependency_recommendations(session, 0)
    security_requirements = get_recommendation_content(sre_dependency_recommendations)

    if "Confidentiality" in security_requirements and "Authenticity" in security_requirements:
        security_requirements.remove('Confidentiality')
        security_requirements.remove('Authenticity')
        security_requirements.append('Confidentiality,Authenticity')

    sensitive_domain = belongs_sensitive_domain(application_area)
    stream_cipher = need_stream_cipher(payload_size)

    # If the system already exists
    if existing_system == 'Existing System':
        
        conditions_csv_filename = 'external/conditions_existing_software.csv'
        error_message = [get_recommendation_id(recommendations, 'The system is not capable')]

        # Hardware type SBC
        if hardware_type == 'SBC':
            # If the system is not capable
            if not (cpu >= 32 and flash_memory_size >= 2000000 and ram_size >= 252000 and cpu_clock >= 400):
                return error_message

        # Hardware type AVR
        elif hardware_type == 'AVR':
            if not (cpu >= 8 and flash_memory_size >= 48 and ram_size >= 4 and cpu_clock >= 16):
                return error_message

        # Hardware type MSP
        elif hardware_type == 'MSP':
            if not (cpu >= 16 and flash_memory_size >= 48 and ram_size >= 8 and cpu_clock >= 8):
                return error_message

        # Hardware type ARM
        elif hardware_type == 'ARM':
            if not (cpu >= 32 and flash_memory_size >= 256 and ram_size >= 64 and cpu_clock >= 72):
                return error_message

        # Hardware type PIC
        elif hardware_type == 'PIC':
            if not (cpu >= 8 and flash_memory_size >= 28 and ram_size >= 4 and cpu_clock >= 4):
                return error_message
        # If not hardware type and cpu exists
        else:
            if not (cpu >= 4 and flash_memory_size >= 38 and ram_size >= 4 and cpu_clock >= 10):
                return error_message


        return select_requirement_algorithm_existing_system(conditions_csv_filename, recommendations, hardware_type, flash_memory_size, ram_size, sensitive_domain, stream_cipher, security_requirements)               

    # If the system is being planned   
    else:
        conditions_csv_filename = 'external/conditions_planning_software.csv'

        return select_requirement_algorithm_planning(conditions_csv_filename, recommendations, cpu, flash_memory_size, ram_size, sensitive_domain, stream_cipher, security_requirements)