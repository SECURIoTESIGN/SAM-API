# Error Handling

All applications are bound to generate errors for various reasons. These errors must be correctly handled or else an attacker can use them to attack a system.

As a result of incorrect error management, attackers may be able to:

* Understand the APIs that are used within the business;
* Map the different services that integrate with one another by learning about the internal structures and frameworks that are in use, which allows for attack chaining;
* Compile a list of the software that are being used, including their versions and types;
* DoS the machine by putting it in a deadlock or throwing an unhandled exception, which sends a panic signal to the engine that's running it;
* Controls bypass when the logic set along the expected path does not limit a specific exception.


## Manually

To test against this vulnerability the tester needs to force unexpected data into the system and analyse the error messages or return values of the system when exposed to these kid of unexpected scenarios.

### Web Servers

In order to trigger error messages in Web servers the tester needs to:

* Search for random files/folders that will not be found (error 404);
* Try to request for directories that don exist and observe the result (403s, blank page, or directory listing),
* Send a request that crashes the HTTP RFC. Sending a very long path, breaking the headers format, or changing the HTTP version are all examples.
*  Analyze if there is any kind of information leakage present in the error messages

## Web Applications

In order to trigger a web application to trow errors the tester must:

1. Find possible input locations;
2. Analyze the expected input types;
3. Fuzzy all the inputs based on the information collected above
4. Recognize the service responding with the error message and attempting to refine the fuzz list in order to extract further knowledge or error data from the service.
5. Analyze if there is any kind of information leakage present in the error messages


A more detailed file in this topic can be found in https://owasp.org/www-project-web-security-testing-guide/stable/4-Web_Application_Security_Testing/08-Testing_for_Error_Handling/01-Testing_For_Improper_Error_Handling.html
