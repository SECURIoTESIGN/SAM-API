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

import modules.utils
import external.Software
import external.Hardware

"""
[Summary]: Common method to get answer content from module.
[Arguments]: 
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $question_number$: An integer that declares the question number, array format (0, length-1).
[Returns]: Answer content for specified question.
"""
def get_answer_content(session, question_number):
    answers = session['questions'][question_number]['answer']
    if len(answers) == 1:
        answer = answers[0]['content']
    else:
        answer = []
        for ans in answers:
            answer.append(ans['content'])

    return answer


"""
[Summary]: Default SAM's logic main method.
[Arguments]:
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: MUST return an array of recommendation IDs.
"""
def run(session, recommendations):
    DEBUG = False
    request_type = get_answer_content(session, 0)

    if(DEBUG): 
        modules.utils.console_log("logic_3", str(session))
        modules.utils.console_log("logic_3", str(recommendations))
    
    if request_type == "Software":
        return external.Software.run(session, recommendations)
    else:
        return external.Hardware.run(session, recommendations)
