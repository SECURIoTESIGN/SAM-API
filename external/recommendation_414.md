# Access Control

Access Control, also known has authorization is the propriety that determines, documents, and manages the subjects (users, devices, or processes) to whom access should be granted, as well as the items to which they should be granted access.


## Owasp ZAP

OWASP ZAP (short for Zed Attack Proxy) is an open-source web application security scanner. ZAP can be defined as a “man-in-the-middle proxy.” It stands between the tester’s browser and the web application so that it can intercept and inspect messages sent between browser and web application, modify the contents if needed, and then forward those packets on to the destination. It can be used as a stand-alone application, and as a daemon process. This scanner claims to test against Path Transversal Vulnerability.

To install and run this scanner the user needs to go to https://www.zaproxy.org/download/ and select the system in which this tool will be installed. This scanner requires Java 8 +.

After installation the application will ask the user if the tester wants to persist the ZAP session. By default, ZAP sessions are always recorded to disk in a HSQLDB database with a default name and location. If you do not persist the session, those files are deleted when you exit ZAP.

To test for access control it is needed to add the access control Add-on and configure a file with the access rules on which is stated what parts of the application each user is supposed to reach. After the correct set up of the add-on ZAP will attack the SUT and try to reach every URL of the web-app from the perspective of every user.