# Forced Browsing
The aim of forced browsing is to enumerate and access resources that are not referenced by the application but are still accessible.
Brute Force techniques can be used to scan the domain directory for unlinked contents such as temporary folders and data, as well as old backup and configuration files. These resources can store sensitive information about web applications and operating systems, such as source code, credentials, internal network addressing, and so on, making them a valuable resource for attackers.
## Manually 

 Manual testing can be performed in a browser by browsing to the web application of the SUT such that the url is something similar to:

 ```
 https://www.example.com/userdata.php?id=2258

 ```

 The "id" field can be changed to another number to try to access a different user, such as:

 ```
https://www.example.com/userdata.php?id=2262
 ```

The tester can also try to access common files and directories by using this vulnerability, for example the tester can try to acces the configuration file by changing the URL:

```
https://www.example.com/configuration/
```