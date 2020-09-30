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
############# JSON Session EXAMPLE #############
{
  "id": 3,
  "user_id": 1,
  "module_id": 6,
  "module_logic": "logic_6.py",
  "ended": 1,
  "createdOn": "2020-08-06 12:26:10",
  "updatedOn": "2020-08-06 12:26:10",
  "questions": [
    {
      "id": 38,
      "content": "Q1Y",
      "answer": {
        "id": -1,
        "content": "2"
      }
    },
    {
      "id": 39,
      "content": "Q2Y",
      "answer": {
        "ID": -1,
        "content": "2"
      }
    }
  ],
  "dependencies": [
    {
      "module": {
        "id": 1,
        "fullname": "Security Requirements Elicitation",
        "displayname": "Security Requirements",
        "shortname": "SRE",
        "last_session": {
          "id": 1,
          "user_id": 1,
          "module_id": 1,
          "module_logic": null,
          "ended": 1,
          "createdOn": "2020-08-06 11:41:50",
          "updatedOn": "2020-08-06 11:41:50",
          "questions": [
            {
              "id": 1,
              "content": "State the domain type for your IoT system",
              "answer": {
                "id": 1,
                "content": "Smart Home"
              }
            },
            {
              "id": 2,
              "content": "Will the system have a user?",
              "answer": {
                "id": 10,
                "content": "Yes"
              }
            }
          ],
          "recommendations": [
            {
              "ID": 1,
              "content": "Confidentiality",
              "description": null,
              "recommendation_guide": "recommendation_1.md"
            }
          ]
        }
      }
    },
    {
      "module": {
        "id": 5,
        "fullname": "Module X",
        "displayname": "Module X",
        "shortname": "MX",
        "last_session": {
          "id": 2,
          "user_id": 1,
          "module_id": 5,
          "module_logic": null,
          "ended": 1,
          "createdOn": "2020-08-06 11:06:16",
          "updatedOn": "2020-08-06 11:06:16",
          "questions": [
            {
              "id": 37,
              "content": "Q3X",
              "answer": {
                "ID": 54,
                "content": "A1X"
              }
            },
            {
              "id": 35,
              "content": "Q1X",
              "answer": {
                "id": -1,
                "content": "2"
              }
            }
            
          ],
          "recommendations": [
            {
              "id": 2,
              "content": "Integrity",
              "description": null,
              "recommendation_guide": null
            }
          ]
        }
      }
    }
  ]
}

############# JSON Recommendations EXAMPLE #############
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
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $recommendations$: Array of Python objects that includes information about the available set of recommendations (see example above).
[Returns]: MUST return an array of recommendation IDs.
"""
def run(session, recommendations):
    DEBUG = False

    # This is the default array that will contain the list of recommendation IDs (integers), the array must be populated after some logic (see below for an example).
    returned_recommendations = []
    if (DEBUG):
        # Print Python Object as a JSON string
        print(json.dumps(session))
        print(json.dumps(recommendations))

    # 1. Do some logic with the answers given by the user to one or more questions for the current parsed module. 
    # If the answer is 16 Recommend to upgrade from a 16bit CPU to a 32bit CPU.
    if (int(session['questions'][0]['answer']['content']) == 16):
        # 1.1. Based on the answers, give an output or recomendation based on the available set of recomendations.
        returned_recommendations.append(recommendations[18]['id'])
    
    # If the answer is 32 Recommend to upgrade from a 32bit CPU to a 64bit CPU.
    if (int(session['questions'][0]['answer']['content']) == 32):
        # 1.1. Based on the answers, give an output or recomendation based on the available set of recomendations.
        returned_recommendations.append(recommendations[19]['id'])

   
    return(returned_recommendations)
