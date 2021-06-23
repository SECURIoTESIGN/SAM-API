# Reflected Cross Site Scripting

When an attacker injects browser executable code inside a single HTTP response, this is known as reflected cross-site Scripting (XSS).
The injected attack is not stored in the application; it is non-persistent and only affects users who click on a maliciously designed link or visit a third-party website. The attack string is included in the constructed URI or HTTP parameters, processed incorrectly by the program, and sent back to the victim. 

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

If the system is vulnerable to Reflected XSS it will appear on the Alerts tab with the name "Cross Site Scripting (Reflected). The tester can click on this alert an it will show the variables vulnerable within the code.

## Burp Suite

Burp Suite is software developed in Java by PortSwigger, to perform security tests on web applications.The Burp Suite is divided into several components such has: Burp Proxy, Burp Spider, Burp Scanner, Burp Intruder, Burp Repeater. etc.
To download this tool the user needs to access https://portswigger.net/burp/communitydownload and download the program to their respective system.


To begin the testing with this tool the tester needs to config their browser's proxy configuration to "localhost" in port 8080.


To test the SUT the tester needs:

* Open the burp suite, go to the "Proxy" tab, click on "Intercept" and press the button "Intercept is off";
* Go to the browser and open the web page to be tested;
* Return to Burp, in the Proxy "Intercept" tab, ensure "Intercept is on";
* Enter appropriate input in the web application and submit the request;
* Access the request in the Proxy "Intercept" tab;
*  Right click anywhere on the request to bring up the context menu and click "Send to Repeater";
* Go to the "Repeater" tab;
* It is possible to test various inputs by editing the "Value" of the appropriate parameter in the "Raw" or "Params" tabs;
* An example of a test can be changing the value of a parameter to: 
``` HTML
    <script> alert (1) </script>
```
* Click on "Go";
* Access if the payload has been modified in the "Response" tab;
* Right click on the response o bring up the context menu, click "Show response in browser" to copy the URL.You can also use "Copy URL" or "Request in browser",
* In the pop up window, click "Copy";
* Copy the URL to the address bar of the chosen browser and verify if the changes made appear in the page.

If the changes manifest in the page the system is vulnerable to this type of attack.

 

 