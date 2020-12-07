
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
	practices = []

	practices.append("Authentication")

	arq_type = get_answer_content()  # 0
	domain_type = get_answer_content()  # 1
	auth = get_answer_content()  # 2
	db = get_answer_content()  # 3

	# check if embebbed systems are chosen
	if 'Embedded System' in arq_type:
		practices.append("IoT Security")

	# check if database is choosed

	if db == 'Yes':
		db_type = get_answer_content()  # 4
		type_data = get_answer_content()  # 7
		if db_type == "SQL":
			wich_db_SQL = get_answer_content()  # 5
			practices.append("SQL Injection")
			if "Hybrid Application" in arq_type or "Web Application" in arq_type and db_type == "MySQL" or db_type == "PostgreSQL":
				practices.append("SSL/TLS")

			elif db_type == "MySQL" or db_type == "PostgreSQL":
				practices.append("Access Control")

		elif db_type == "NoSQL":
			wich_db_noSQL = get_answer_content()  # 6
	
	user_reg = get_answer_content()  # 8

	if user_reg == "Yes":
		way_of_reg = get_answer_content()  # 9
	
	
	prog_leng = get_answer_content()  # 10
	print(prog_leng)
	# check if language program are chosen
	if 'Android App' in arq_type and "C#" in prog_leng or "Java" in prog_leng:
		practices.append("Secure Java and C # Deployment")



	input_forms = get_answer_content()  # 11
	upload_files = get_answer_content()  # 12
	logs = get_answer_content()  # 13
	reg_updates = get_answer_content()  # 14
	third_party_soft = get_answer_content()  # 15
	cloud = get_answer_content()  # 16
	hardware = get_answer_content()  # 17

	if hardware == "Yes":
		hardware_auth = get_answer_content()  # 18
		hardware_comm = get_answer_content()  # 19

	# check if input forms is used
	if input_forms == "Yes":
		practices.append("Input Validation")

	if "Hybrid Application" in arq_type or "Web Application" in arq_type:
		practices.append("Session Management")
		practices.append("Cross Site Scripting")
		practices.append("HTML Secure Fashion")

    # write Buffer Overflows guide
	if "C/C++/Objective C" in prog_leng:
		practices.append("Buffer Overflows")

	# write Cryptography guide
	practices.append("Cryptography")

	# write SSL/TLS guide

	if upload_files == "Yes":
		practices.append("File Upload")

	# logging info
	if logs == "Yes":
		practices.append("Logging")

	# Update info
	if reg_updates == "Yes":
		practices.append("Application Regular Updates")

	# Third-party info
	if third_party_soft == "Yes":
		practices.append("Third-Party Applications")
	print(cloud)
	# Database use and community and private cloud environment
	if db == "Yes" and cloud == "Community Cloud (Remote connection)" or cloud == "Private Cloud (Local connection)":
		practices.append("Security Risk Analysis 1")

	# Database use and public cloud environment
	if db == "Yes" and cloud == "Public Cloud (Remote connection)":
		practices.append("Security Risk Analysis 2")

	# Database use and Hybrid cloud environment
	if db == "Yes" and cloud == "Hybrid Cloud (Mix Connection)":
		practices.append("Security Risk Analysis 3")


	# Database use and VPC environment
	if db == "Yes" and cloud == "Virtual Private Cloud":
		practices.append("Security Risk Analysis 4")

	return (practices)


"""
[Summary]: Common method to get answer content from module.
[Arguments]:
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $question_number$: An integer that declares the question number, array format (0, length-1).
[Returns]: Answer content for specified question.
"""
def get_answer_content():
    global answer_num, _session

    answers=_session['questions'][answer_num]['answer']
    if len(answers) == 1:
        answer=answers[0]['content']
    else:
        answer=[]
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
	_session=session
	answer_num=0

	temp_recommendations=get_recommendations(session)
	final_recommendations=[]
	for recm in temp_recommendations:
		final_recommendations.append(get_recommendation_id(recommendations, recm))

	return final_recommendations
