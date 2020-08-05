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
"""
############# Python Object Session EXAMPLE #############
{
    "id": 4,
    "user_id": 1,
    "module_id": 6,
    "module_logic": "logic_6.py",
    "ended": 1,
    "createdOn": "2020-08-05 17:55:24",
    "updatedOn": "2020-08-05 17:55:24",
    "questions": [
        {
            "ID": 38,
            "content": "Q1Y",
            "answer": {
                "ID": -1,
                "content": "3"
            }
        },
        {
            "ID": 39,
            "content": "Q2Y",
            "answer": {
                "ID": -1,
                "content": "4"
            }
        }
    ]
}

############# Python Object Recommendations EXAMPLE #############
[
    {
        "id": 1,
        "content": "Confidentiality",
        "description": null,
        "guide": "recommendation_1.md",
        "createdOn": "2020-08-05 16:52:40",
        "updatedOn": "2020-08-05 16:52:40"
    },
    {
        "id": 2,
        "content": "Integrity",
        "description": null,
        "guide": null,
        "createdOn": "2020-08-05 16:52:40",
        "updatedOn": "2020-08-05 16:52:40"
    }
]

[Summary]: Default SAM's logic main method.
[Arguments]:
    - $session$: Python object (from a JSON string) that includes information about a session, including questions and user selected and/or user inputted answers (see example above).
    - $recommendations$: Array of Python objects (from a JSON string) that includes information about the available set of recommendations (see example above).
[Returns]: MUST return an array of recommendation IDs.
"""
def run(session, recommendations):
    DEBUG = False
    
    # This is the default array that will contain the list of recommendation IDs (integers), the array must be populated after some logic (see below for an example).
    returned_recommendations = []
    if (DEBUG):
        print(session)
        print(recommendations)

    # 1. Do some logic with the answers given by the user to one or more questions for the current parsed module. 
    if ( int(session['questions'][0]['answer']['content']) >= 0 and int(session['questions'][1]['answer']['content']) >= 0):
        # 1.1. Based on the answers, give an output or recomendation based on the available set of recomendations.
        returned_recommendations.append(recommendations[0]['id'])
        returned_recommendations.append(recommendations[1]['id'])
   
    return(returned_recommendations)
