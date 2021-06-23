# Command Injection

The purpose of a command injection attack is to execute arbitrary commands on the host operating system via a compromised program.
When an application sends insecure user-supplied data (forms, cookies, HTTP headers, etc.) to a device shell, command injection attacks are possible. 

## Manual

When viewing a file in a web application, the file name is often shown in the URL, to manualy test this vulnerability the tester can alter the URL to perform a know command. For example:
 ``` bash
#Example URL before alteration:

http://sensitive/cgi-bin/userData.pl?doc=user1.txt

#Example URL modified:

http://sensitive/cgi-bin/userData.pl?doc=/bin/ls|

```

If vulnerable the system will execute the command /bin/ls.

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

* In the Request Tab it is possible to alter this variable with known commands, for example using "Dir c:\": 
``` bash
    Doc=Doc1.pdf+|+Dir c:\
```

If the system is vulnerable to command injections the information of c: will be presented in the response tab.