# Format String

When the application evaluates the submitted data of an input string as a command, the Format String exploit occurs.
The attacker could then execute code, read the stack, or trigger a segmentation fault in the running program, resulting in new behaviors that could jeopardize the protection or stability of the system. 

## Manual Testing

A manual test can be performed in a browser by browsing to the web application of the SUT such that the query has conversion specifiers. An example of a test can be a string of specifiers %s%s%s%n, for example:

https://vulnerable_sut/userinfo?username=%25s%25s%25s%25n

If the web site is vulnerable, the browser or tool should receive an error, which may include a timeout or an HTTP return code 500.

## Wfuzz

Wfuzz is a tool for bruteforcing Web applications. It can be used to locate resources that aren't linked (directories, servlets, scripts, etc. ), bruteforce GET and POST parameters for checking various types of injections (SQL, XSS, LDAP, etc. ), bruteforce Forms parameters (User/Password), and more. 

To download this tool the user must input the follwing in the terminal:

``` bash
    pip install wfuzz
```

Start with a text file (fuzz.txt in this example) with one input per line:

[Valid Input]
%s%s%s%n
%p%p%p%p%p
{event.__init__.__globals__[CONFIG][SECRET_KEY]}

The fuzz.txt file contains the following:

* A valid input alice to verify the application can process a normal input
* Two strings with C-like conversion specifiers
* One Python conversion specifier to attempt to read global variables

To send the file to the SUT the user needs to input the following:


wfuzz -c -z file,[File path],urlencode https://vulnerable_sut/userinfo?[Variable to test]=FUZZ