# Malicious Applications

By downloading a malicious application, the attacker
can spread is control over to the IoTs connected to the infected system.

To mitigate this threat the system must have a functioning firewall or anti-virus system.

## Wafw00f

Wafw00f is a tool that identifies if a firewall is being used within a system. To determine which WAP is being used this tool does the following:

    * Sends a normal HTTP request and analyses the response; this identifies a number of WAF (Web application firewall) solutions.
    * If that is not successful, it sends a number of (potentially malicious) HTTP requests and uses simple logic to deduce which WAF it is.
    * If that is also not successful, it analyses the responses previously returned and uses another simple algorithm to guess if a WAF or security solution is actively responding to our attacks.

To install this tool the user needs to insert the following in the terminal:

``` bash
    apt install wafw00f
    cd wafw00f
    python3 setup.py install
```

A generic WAF test with this tool can be as follows:

``` bash    
    wafw00f -a [URL]
```
