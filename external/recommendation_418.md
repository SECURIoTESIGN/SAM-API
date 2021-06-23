# Code Injection

The term "code injection" applies to a variety of attacks that include inserting code that is then interpreted/executed by the application. This form of attack takes advantage of poor data handling. These attacks are usually made possible by a lack of proper input/output data validation.

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

* To perform the test a variable to add a command should be selected, usually these variables are represented by:
```HTML
    [variable name] = [Path]
```

* In the Request Tab it is possible to alter this variable with a known shell command, for examples nslookup:

``` bash
    [variable name] = require('child_process').exec("nslookup+burpcollaborator.net')
```

If successful, the command will cause a connection with Burp server. 