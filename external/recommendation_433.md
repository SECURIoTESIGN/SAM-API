# Heartbleed Bug
Heartbleed is a catastrophic bug in OpenSSL, announced in April 2014.
A missing bounds check before a memcpy() call with non-sanitized user input as the length parameter causes this serious flaw (CVE-2014-0160).
An attacker can trick OpenSSL into allocating a 64KB buffer, copying more bytes than required into the buffer, then returning the buffer, leaking the contents of the victim's memory 64KB at a time. 

## Openssl 

To be protected against this vulnerability the system must have the most recent version of Openssl, specificity versions above OpenSSL 1.0.1g.

To verify the version of the openssl of the SUT the tester needs to input the following in the terminal:

```bash
    openssl version
```

To upgrade openssl and other linux packages the user can insert:

``` bash
    sudo apt-get update
    sudo apt-get upgrade
```