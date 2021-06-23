# Brute Force/ Weak Authentication

Brute Force is when an attacker tries to guess the user credentials by trying a lot of different combinations. Some IoT devices come with default user credentials, if not changed these can give an attacker easy access to the system.

If the tester is able to log into an account using the next methods and tools, the system under test is not safe against brute force attacks and possesses a weak authentication system.

A password or authentication is considered strong if these tools take days to crack the passwords tested.

## Cain & Abel

Cain & Abel is a very useful security tool used for decryption and decoding of passwords for a wide array of offline programs and network services.

When performing a MitM attack with this tool, if any password supported hashes are captured Cain & Abel automatically sends the hashes to the Cracker tab but, it is also possible to import SAM files with the hashes previously stored. To use brute force in order to discover passwords the tester needs to do the following:

1- Click the Cracker tab;

2- Select a hashing algorithm (for example NL & NTLM Hash)

2- Click in the "+" button and select a SAM file;

3- In the right pane, right-click the user with the password to be cracked

4- Select "Brute-Force Attack";

5- Click "NTLM Hashes";

6- Select the charset and password length.


After this last step the tool will attempt to crack the password. If successful the clear text password will appear.


## THC Hydra

THC Hydra is a fast and flexible login cracker which can be used on both Linux and Windows, and supports protocols like AFP, HTTP-FORM-GET, HTTP-GET, HTTP-FORM-POST, HTTP-HEAD, HTTP-PROXY.

To install Hydra the user needs to input:

``` bash
    git clone https://github.com/vanhauser-thc/thc-hydra
    cd thc-hydra/
    ./configure
    make
    make install

```

The next step is to install the required libraries:

``` bash
    apt-get install libssl-dev libssh-dev libidn11-dev libpcre3-dev \
                libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev \
                firebird-dev libncp-dev
```


To perform a brute force attack with this tool the tester first needs to find the target IP address by writting in the terminal the following:

``` bash
    dig <TAGRET>
```

To launch a test with hydra the tester needs a file .lst with the most popular passwords and another with usernames, in order, for hydra to try all combinations. To launch a ssh test the following must be inserted:


```bash
    hydra -L [path to user list] -P [path to password list] [Target IP] -t 6 ssh
```

## John the Ripper

John the Ripper (also called simply ‘John’ ) is one of the most well known free password cracking tool.

This tool is pre-installed in Kali Linux, but if this is not he used system it can be installed by typing the following on the command line:

``` bash
    sudo apt-get install john -y
```

To begin testing the system against this vulnerability it is necessary to have a valid password for said system stored and hashed stored in a file. An example of the file could be:

``` bash
    [username]:[hashed password]
```
To begin cracking the passward it is only needed to input:

```bash
    john [Password file] --format=[Hash Algorithm]
```

If no further instruction are given John will begin the process by going into single mode in which it uses default passwords, if the password is not cracked by this process john goes into wordlist mode in which it uses a wordlist dictionary, the last method used by this tool is incremental in which the tool tries all possible combinations of characters until it finds the right correspondence between word and hash.
