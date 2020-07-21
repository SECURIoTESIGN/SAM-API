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
DEBUG = False
"""
[Summary]: Default SAM's logic main method.
[Arguments]:
    - $module$: A JSON Object that includes information about a module, including questions and user selected and/or user inputted answers.
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: MUST return an array of recommendation IDs.
"""
def run(module, recommendations):
    # This is the default array that will contain the list of recommendation IDs, the array must be populated after some logic (see below for an example).
    p_recommendations = []
    if (DEBUG):
        print(str(module))
        print(str(recommendations))
    
    # 1. Do some logic with the answers given by the user to one or more questions for the current parsed module. 
    if (module['Module']['questions'][0]['answer']['content'] >= 0 and module['Module']['questions'][1]['answer']['content'] >= 0):
        # 1.1. Based on the answers, give an output or recomendation based on the available set of recomendations.
        p_recommendations.append(recommendations[0])
        p_recommendations.append(recommendations[1])
   
    return(p_recommendations)
