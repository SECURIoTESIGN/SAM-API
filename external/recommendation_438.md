# Path/Directory Traversal File 
The aim of a path traversal attack (also known as directory traversal) is to gain access to files and directories stored outside of the web root folder. It may be possible to access arbitrary files and directories stored on the file system, like program source code configuration and critical system files, by modifying variables that reference files with “dot-dot-slash (../)” sequences and variations, or by using absolute file paths. 

## Owasp ZAP

OWASP ZAP (short for Zed Attack Proxy) is an open-source web application security scanner. ZAP can be defined as a “man-in-the-middle proxy.” It stands between the tester’s browser and the web application so that it can intercept and inspect messages sent between browser and web application, modify the contents if needed, and then forward those packets on to the destination. It can be used as a stand-alone application, and as a daemon process. This scanner claims to test against Path Transversal Vulnerability.

To install and run this scanner the user needs to go to https://www.zaproxy.org/download/ and select the system in which this tool will be installed. This scanner requires Java 8 +.

After installation the application will ask the user if the tester wants to persist the ZAP session. By default, ZAP sessions are always recorded to disk in a HSQLDB database with a default name and location. If you do not persist the session, those files are deleted when you exit ZAP.

To start an automated scan it is only needed to do the following:

* Start ZAP and click the Quick Start tab of the Workspace Window;
* Click the large Automated Scan button;
* In the URL to attack text box, enter the full URL of the web application you want to attack;
* Click the Attack.

If this vulnerability is detected on the SUT it will be presented in the results bar.

## Burp Suite
Burp Suite is software developed in Java by PortSwigger, to perform security tests on web applications.The Burp Suite is divided into several components such has: Burp Proxy, Burp Spider, Burp Scanner, Burp Intruder, Burp Repeater. etc.
To download this tool the user needs to access https://portswigger.net/burp/communitydownload and download the program to their respective system.


To begin the testing with this tool the tester needs to config their browser's proxy configuration to "localhost" in port 8080.


To test the SUT the tester needs:

* Open the burp suite, go to the "Proxy" tab, click on "Intercept" and press the button "Intercept is off";
* Go to the browser and open the web page to be tested;

* Return to the "Proxy" tab, select intersect and then click on "Intercept is on";

* Access the URL with the parameter you wish to test;

* The request will be captured by the proxy "Intercept" tab;

* Right click anywhere on the request and select "Send to Repeater";

* Select the "Repeater" tab;

* Click the "Go" button;

* In the "Response" Panel you can observe the results of the request;

* To perform the test a variable to alter the path should be selected, usually these variables are represented by:
```HTML
    [variable name] = [Path]
```

* In the Request Tab it is possible to alter this variable with known paths such as : "	../", or "../../../../../../../../../../../../../../../../etc/passwd";

* Click on the "Go" button

* If the system is vulnerable the tester will see an difference in the response between the original request and the tampered request, usually the most notorious change is in the "Content-length" field. If the second command exemplified in the step above is successful the tester will have access to the passwd file of a Linux system.

From https://portswigger.net/support/using-burp-to-test-for-path-traversal-vulnerabilities