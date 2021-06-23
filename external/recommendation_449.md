# Shared Resource Manipulation


## OWASP ZAP

OWASP ZAP (short for Zed Attack Proxy) is an open-source web application security scanner. ZAP can be defined as a “man-in-the-middle proxy.” It stands between the tester’s browser and the web application so that it can intercept and inspect messages sent between browser and web application, modify the contents if needed, and then forward those packets on to the destination. It can be used as a stand-alone application, and as a daemon process. This scanner claims to test against Path Transversal Vulnerability.

To install and run this scanner the user needs to go to https://www.zaproxy.org/download/ and select the system in which this tool will be installed. This scanner requires Java 8 +.

After installation the application will ask the user if the tester wants to persist the ZAP session. By default, ZAP sessions are always recorded to disk in a HSQLDB database with a default name and location. If you do not persist the session, those files are deleted when you exit ZAP.

To automatically test against Reflected XSS only needed to do the following:
* Click in the Quick Start Tab;
* Click on New Scan;
* In "Starting Point" click in the "Select" Button and choose a POST request to start on;
* Go to "Input Vectors" and check all boxes;
* Click on Start Scan;
* When the load bar is at 100% click on the "Alerts" tab.

If the system is vulnerable to Reflected Shared Resource Manipulation it will appear on the Alerts tab with the name "Sub Resource Integrity Attribute Missing". The tester can click on this alert an it will show the variables vulnerable within the code.