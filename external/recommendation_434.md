# Log Injection
Log files are widely used by applications to keep track of activities or transactions for later analysis, statistics collection, or debugging.
The task of reviewing log files can be performed manually on an as-needed basis or automated with a tool that automatically culls logs for important events or trending information, depending on the nature of the application. 
An intruder can forge log entries or inject malicious content into log files by writing invalidated user input to said log files. This is referred to as log injection. 

## Manually 

To manually test against this vulnerability the tester needs to have an understanding of hexadecimal characters to build the injection command.
To inject a space for example the tester needs to input %3a in order to represent the ":" character, %0a represents a line break, etc.
With the right combination of hexadecimal symbols and if the SUT is vulnerable the tester will be able to inject information in the logs.

An example of an Log injection can be observed in the following example:

``` bash
     ...
    String val = request.getParameter("val");
    try {
        int value = Integer.parseInt(val);
    }
    catch (NumberFormatException) {
        log.info("Failed to parse val = " + val);
    }
    ...
```

If a user submits the string “twenty-one” for val, the following entry is logged:

    INFO: Failed to parse val=twenty-one

However, if an attacker submits the string “twenty-one%0a%0aINFO:+User+logged+out%3john” equivalent to "INFO: User logged out=john, the following entry is logged:

    INFO: Failed to parse val=twenty-one

    INFO: User logged out=john

This kind of tests can be applied to the inputs requested in the SUT, if the tester can successfully inject information in the logs then the SUT is vulnerable to this attack.
