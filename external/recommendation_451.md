# Insecure Transport 


## Testssl

Testssl.sh is a, free, command line tool that checks the correct use of the TLS/SSL ciphers, protocols as well as some cryptographic flaws.

This tool can be found at https://github.com/drwetter/testssl.sh and can be donaloaded and used following the next steps:

``` bash
git clone --depth 1 https://github.com/drwetter/testssl.sh.git
cd testssl.sh
./testssl.sh [URL]
```

The example bellow only shows a genetic test using this tool, for more options it is needed to check the manual provided by the authors.


## OWASP O-Saft

O-Saft is a tool developed by OWASP with the intent to test the SSL connection and show information about the SSL certificates under test. This tool also has the ability to test a system against vulnerabilities such has BEAST, CRIME, DROWN, FREAK, Heartbleed, etc.


Before installing O-Saft it is needed the following Perl modules: Net::SSLeay, IO::Socket::SSL, IO::Socket::INET, Net::DNS. After the installation of said modules it is needed to download the last stable release of O-Saft from https://github.com/OWASP/O-Saft, unpack it and remove the o-saft-README from the unziped folders.

A simple check with this tool can be done by inserting the following in the terminal:

```bash
     o-saft +check your.tld
```

More test options are available and can be accessed by consulting the help file trough the " o-saft --help" command.

