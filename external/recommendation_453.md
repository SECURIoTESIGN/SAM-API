# Testing for Insecure Direct Object References

When an application offers direct access to objects based on user-supplied input, this is known as insecure direct object references (IDOR). As a result of this flaw, attackers can circumvent authorization and gain direct access to device resources, such as database records or files.
This is caused by the fact that the application takes user supplied input and uses it to retrieve an object without performing sufficient authorization checks.

## Manually

To test for this flaw, the tester must first map out all areas of the application where user input is used to explicitly reference objects. The tester can then change the value of the parameter used to reference objects and see if it's possible to retrieve objects belonging to other users or circumvent authorization in any other way.

For example an tester can explore the follwing URL:

```
http://foo.bar/changepassword?user=user
```

By changing the value sent in the "user" field and if the SUT is vulnerable to this attack, the tester can change the password of a different user than the one logged in, for example by inserting:

```
http://foo.bar/changepassword?user=john
```

In this case, if the system is vulnerable to this attack the password of the user john will be changed without his permission.