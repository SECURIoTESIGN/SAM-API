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


def get_recommendations(session, threats, ciphers):

    #37 
    # https://owasp.org/www-project-web-security-testing-guide/assets/archive/OWASP_Testing_Guide_v4.pdf

    SymmetricCiphers=["Clefia128/128","Clefia128/192","Enocoro_v2-128","Grain_v1-128", "Trivium-80", "MICKEY_2.0-80", "TWINE64/80","TWINE64/128", "Midori128/128", "SIMON64/128", "Piccolo64/80", "Piccolo64/128", "Midori64/128", "SIMON64/96", "Grain_v1-80", "ChaCha20-128","ChaCha20-256", "SPECK64/128", "AES_CTR128/128", "LED64/80", "SPECK64/96", "PRESENT64/80", "PRINCE64/128", "AES_CBC128/128", "Enocoro-80", "Clefia128/256", "PRESENT64/128", "SPECK96/144", "SPECK48/72"]
    HashFunction=["PHOTON-80/20/16", "Keccak-f[100]", "SPONGENT-128/128/8","PHOTON-256/32/32", "SPONGENT-88/80/8", "U-QUARK", "PHOTON-128/16/16", "SPONGENT-160/160/16", "PHOTON-160/36/36", "S-QUARK", "PHOTON-224/32/32"]
    Mac=["AES-GCM","ACORN", "SILC-PRESENT", "SILC-AES", "Deoxys", "AES-OTR", "Ascon", "CLOC-AES", "JAMBU-AES", "CLOC-TWINE", "Ketje-SR"]
    hMAC=["SipHash-128"]

    recommendations=[]

    
    recommendations.append("Testing for Malicious Apps")

    if "Out-of-bounds Write" in threats: #787
        recommendations.append("Testing Buffer Overflow")
        recommendations.append("Testing Forced Browsing")


    if "Improper Restriction of Operations within the Bounds of a Memory Buffer" in threats: #119
        recommendations.append("Testing Buffer Overflow")
        recommendations.append("Testing Format String")
        recommendations.append("Testing SQL Injection")
        recommendations.append("Testing Reflected XSS"),
        recommendations.append("Testing Stored XSS")


    if "Improper Neutralization of Special Elements in Output Used by a Downstream Component ('Injection')" in threats: #74
        recommendations.append("Testing Code Injection")
        recommendations.append("Testing SQL Injection")
        recommendations.append("Testing Format String")
        recommendations.append("Testing Command Injection")
        recommendations.append("Testing Log Injection")
        recommendations.append("Testing Reflected XSS"),
        recommendations.append("Testing Stored XSS")
        recommendations.append("Testing CSV Injection")


    if "Improper Input Validation" in threats: #20
        recommendations.append("Testing SQL Injection")
        recommendations.append("Testing Reflected XSS"),
        recommendations.append("Testing Stored XSS")
        recommendations.append("Testing for XXE Injection")


    
    if "Out-of-bounds Read" in threats: #125
        recommendations.append("Testing SQL Injection")
        recommendations.append("Testing Reflected XSS"),
        recommendations.append("Testing Stored XSS")
        recommendations.append("Testing Heartbleed Bug")

    if "Improper Following of Specification by Caller" in threats: #573 --> Buffer from child 253; Code from 304 
        recommendations.append("Testing Buffer Overflow")
        recommendations.append("Testing Code Injection")

    if "Exposure of Sensitive Information to an Unauthorized Actor" in threats: #200
        recommendations.append("Testing Path Traversal")    
        recommendations.append("Testing SSL")   

    if "Exposure of Resource to Wrong Sphere" in threats: #668 Path Traversal(Son 22),  Format String(Son 134), DDoS (son 642, 1327), Command (son 583), CSRF (son 732)
        recommendations.append("Testing DoS")
        recommendations.append("Testing Command Injection")
        recommendations.append("Testing Path Traversal")
        recommendations.append("Testing Format String") 
        recommendations.append("Testing CSRF")

    if "Use After Free" in threats: #416
        recommendations.append("Testing DoS")
        recommendations.append("Testing Code Injection")

    if "Use of Insufficiently Random Values" in threats: #330
        recommendations.append("Testing Random and Pseudorandom Number Generators for Cryptographic Applications")
        recommendations.append("Testing Replay Attack")

    if "NULL Pointer Dereference" in threats:#476
        recommendations.append("Testing Command Injection")
        recommendations.append("Testing Code Injection")
        recommendations.append("Testing DoS")

    if "Improper Resource Shutdown or Release" or "Incorrect Control Flow Scoping" in threats: #404, 705(from Sons)
        recommendations.append("Testing DoS")

    if "Improper Authentication" in threats: #287
        recommendations.append("Testing Brute Force")
        recommendations.append("Testing Expired Domain")
        recommendations.append("Testing Man in The Middle")
        

    if "Improper Control of Dynamically-Managed Code Resources" in threats: #913
        recommendations.append("Testing Code Injection")
        recommendations.append("Testing Path Traversal")
        recommendations.append("Testing DoS")

    if "Unrestricted Upload of File with Dangerous Type" in threats: #434
        recommendations.append("Testing Path Traversal")
        recommendations.append("Testing Command Injection")
        recommendations.append("Testing Code Injection")

    if "Covert Storage Channel" or "Insufficiently Protected Credentials" in threats: #515, 522
        recommendations.append("Testing Man in The Middle")

    if "Use of Pointer Subtraction to Determine Size" or "Signal Handler Use of a Non-reentrant Function" in threats: #469, 479
        recommendations.append("Testing Code Injection")

    if "Missing Standardized Error Handling Mechanism" in threats: #544
        recommendations.append("Testing Error Handling")

    if "Improper Restriction of XML External Entity Reference" in threats: #611
        recommendations.append("Testing for XXE Injection")
        recommendations.append("Testing SQL Injection")

    if "Permissive Regular Expression" in threats: #625
        recommendations.append("Testing Reflected XSS"),
        recommendations.append("Testing Stored XSS")
        recommendations.append("Testing SQL Injection")
        recommendations.append("Testing DoS")


    if "Improper Control of Filename for Include/Require Statement in PHP Program" in threats: #98
        recommendations.append("Testing Remote File Inclusion")

    if "Deserialization of Untrusted Data" in threats: #502
        recommendations.append("Testing DoS")
        recommendations.append("Testing Code Injection")

    if "Improper Privilege Management" in threats: #269
        recommendations.append("Testing CSRF")
        recommendations.append("Testing Access Control")

    if "Improper Null Termination" in threats: #170
        recommendations.append("Testing Buffer Overflow")
        recommendations.append("Testing DoS")

    if "Use of a Broken or Risky Cryptographic Algorithm" in threats: #327
        recommendations.append("Testing Assessment of Cryptographic protocols")
        if any(item in ciphers  for item in SymmetricCiphers):
            recommendations.append("ProVerif Testing Symmetrical Cyphers")
        if any(item in ciphers  for item in HashFunction):
            recommendations.append("ProVerif Testing Hash Functions")
        if any(item in ciphers  for item in Mac):
            recommendations.append("ProVerif Testing MAC Functions")
        if any(item in ciphers  for item in hMAC):
            recommendations.append("ProVerif Testing HMAC Functions")
    
    
    if "Unchecked Return Value" or "Uncaught Exception" or "Uncontrolled Resource Consumption" in threats: #[252, 248] (former 391) and 400
        recommendations.append("Testing DoS")


    if "Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')" in threats: #22
        recommendations.append("Testing Path Traversal")  
        recommendations.append("Testing DoS") 
        recommendations.append("Testing Command Injection")
        recommendations.append("Testing Code Injection")

    if "Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')" in threats: #78
        recommendations.append("Testing Command Injection")

    if "Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')" in threats: #79
        recommendations.append("Testing Reflected XSS"),
        recommendations.append("Testing Stored XSS")   

    if "Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection')" in threats: #89
        recommendations.append("Testing SQL Injection")

    if "Improper Control of Generation of Code ('Code Injection')" in threats: #94
        recommendations.append("Testing Code Injection")

    if "Missing Authentication for Critical Function" in threats: #306
        recommendations.append("Testing Access Control")
        recommendations.append("Testing CSRF")  
    
    if "Cross-Site Request Forgery (CSRF)" in threats: #352
        recommendations.append("Testing CSRF")     

    if "Unintended Proxy or Intermediary ('Confused Deputy')" in threats: #441
        recommendations.append("Testing DNS Poisoning")

    if "Incorrect Permission Assignment for Critical Resource" in threats: #732
        recommendations.append("Testing CSRF")
        recommendations.append("Testing Replay Attack")
        recommendations.append("Testing Forced Browsing")

    if "Insufficient Granularity of Access Control" or "Improper Restriction of Write-Once Bit Fields" in threats: #1220, 1224
        recommendations.append("Testing Brute Force")
        recommendations.append("Testing Access Control")

    if "Inclusion of Undocumented Features or Chicken Bits" in threats: #1242 ---> attack patern to Functionality Misuse (Ataques retirados de OWASP Test Guide)
        
        recommendations.append("Testing Forced Browsing")
        recommendations.append("Testing SQL Injection")
        recommendations.append("Testing Reflected XSS"),
        recommendations.append("Testing Stored XSS") 
        recommendations.append("Testing Access Control") 

    if "Improper Access to Sensitive Information Using Debug and Test Interfaces" in threats: #1244 attacks from attack paterns
        recommendations.append("Testing Brute Force")
        recommendations.append("Testing Access Control") 

    if "Missing Authorization" in threats: #862
        recommendations.append("Testing for Insecure Direct Object References")

    if "Integer Overflow or Wraparound" in threats: #190
        recommendations.append("Testing Buffer Overflow")


    if "Incorrect Selection of Fuse Values" in threats: #1253
        recommendations.append("Avoid Incorrect Selection of Fuse Values")


    if "Improper Handling of Single Event Upsets" in threats: #1261
        recommendations.append("Testing for SEU sensitivity")

    if "Register Interface Allows Software Access to Sensitive Data or Security Settings" or "Policy Uses Obsolete Encoding" or "Policy Privileges are not Assigned Consistently Between Control and Data Agents" or "Access Control Check Implemented After Asset is Accessed" or "Improper Translation of Security Attributes by Fabric Bridge" or "Hardware Allows Activation of Test or Debug Logic at Runtime" in threats: #1262 #1267 #1268 #1280 #1311
        recommendations.append("Testing Access Control")


    if "Device Unlock Credential Sharing" in threats: #1273
        recommendations.append("Testing Brute Force")

    if "Missing Protection Against Hardware Reverse Engineering Using Integrated Circuit Imaging Techniques" in threats: #1278
        recommendations.append("Testing Firmware Cracking")

    ############################################

    if "Assumed-Immutable Data is Stored in Writable Memory" in threats: #1282
        recommendations.append("Testing if Assumed-Immutable Data is Stored in Writable Memory")

   # if "Unprotected Confidential Information on Device is Accessible by OSAT Vendors" in threats: #1297
   #     recommendations.append("Post Silicon Validation")

    if "Signal Handler Use of a Non-reentrant Function" or "Hardware Logic Contains Race Conditions" in threats: #479 #1298
        recommendations.append("Testing for Race Conditions")

    if "Improper Protection against Electromagnetic Fault Injection (EM-FI)" in threats: #1319
        recommendations.append("Testing for Hardware Fault Injections")

    if "Missing Immutable Root of Trust in Hardware" in threats: #1326
        recommendations.append("Testing Access Control")
        recommendations.append("Testing Code Signing")

    if "Improper Isolation of Shared Resources in Network On Chip" in threats: #1331
        recommendations.append("Testing for Shared Resource Manipulation")

    if "Improper Protections Against Hardware Overheating" in threats: #1338
        recommendations.append("Testing Overheating")


    final_recm=[]
    for recm in recommendations:
        if recm not in final_recm:
            final_recm.append(recm)
    return final_recm

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

"""ins
[Summary]: Default SAM's logic main method.
[Arguments]:
    - $session$: Python object that includes information about a session - Questions and user selected and/or user inputted answers (see example above).
    - $recommendations$: An array of JSON Objects that includes information about the available set of recommendations.
[Returns]: MUST return an array of recommendation IDs.
"""

def run(session, recommendations):
    global answer_num, _session 
    _session = session

    TMS_dependency_recommendations=get_dependency_recommendations(session, 1)
    LWCAR_dependency_ciphers= get_dependency_recommendations(session,0)
    vulnerabilities=get_recommendation_content(TMS_dependency_recommendations)
    ciphers = get_recommendation_content(LWCAR_dependency_ciphers)

    tests= get_recommendations(session, vulnerabilities, ciphers)
    final_recommendations= []
    print("\n \n \n \n")
    print(tests)
    print("\n \n \n \n")
    for test in tests:
        final_recommendations.append(get_recommendation_id(recommendations, test))
    
    print(final_recommendations)
    return final_recommendations


