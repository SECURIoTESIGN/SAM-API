# Stored XXS

When a web application collects potentially malicious information from a user and stores it in a data store for later use, this is known as stored XSS. The processed input hasn't been properly filtered. As a result, the malicious data will appear to be part of the website and will run in the user's browser with the web application's privileges.

## Owasp ZAP

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

If the system is vulnerable to Reflected XSS it will appear on the Alerts tab with the name "Cross Site Scripting (Stored)". The tester can click on this alert an it will show the variables vulnerable within the code.

## Burp SUite

Burp Suite is software developed in Java by PortSwigger, to perform security tests on web applications.The Burp Suite is divided into several components such has: Burp Proxy, Burp Spider, Burp Scanner, Burp Intruder, Burp Repeater. etc.
To download this tool the user needs to access https://portswigger.net/burp/communitydownload and download the program to their respective system.


To begin the testing with this tool the tester needs to config their browser's proxy configuration to "localhost" in port 8080.


To test the SUT the tester needs:

* Open the burp suite, go to the "Proxy" tab, click on "Intercept" and press the button "Intercept is off";
* Go to the browser and open the web page to be tested;
* Return to Burp and, in the Proxy "Intercept" tab, ensure "Intercept is on";
* Submit a request by refreshing the web application in your browser. The request will be captured by Burp. You can view the HTTP request in the Proxy "Intercept" tab;
* Right click anywhere on the request to bring up the context menu and then click "Send to Repeater";
* Go to the "Repeater" tab;
* It is possible to test various inputs by editing the "Value" of the appropriate parameter in the "Raw" or "Params" tabs;
* An example of a command to preform this type of attack can be by inserting in the Value the follwing:
``` HTML
    <script>alert(document.domain)</script>
```
* Click "Go";
* Return to the browser and refresh the page, thereby sending a second request to the application. This time simulating the user/victim. If the payload fires, then the SUT is vulnerable.