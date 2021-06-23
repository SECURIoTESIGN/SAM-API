# DNS Spoofing/Poisoning

This type of attack works by by poisoning the cache from the DNS
server, which is responsible for the translation from domain names to Internet Protocol (IP) addresses and vice­versa, the attacker is able to, then, redirect the data from the device to a destination designed by himself.

Bellow some tools to test against this type of attack will be presented with instructions to do so. If the system is not secured against this type of attacks the tools will succeed in penetrating the system.

## Arpspoof & DNSspoof

Arpspoof is a preinstalled Kali Linux utility used to redirect packets trough a device of choice.

DNSspoof lets you forge DNS responses for a DNS server on the local network.

To use these tools do poison the DNS of the system under test the user needs to run the following commands:

1- Turn on the packet forwarding in Linux, in order to let the packets flow trough the users machine, by tipping in the terminal:

``` bash
    sysctl -w net.ipv4.ip_forward=1
```
2- Redirect packages to your machine with arpspoof:

``` bash
     arpspoof -t [SUT IP] [Gateway IP]
```

3-  Intercept packages from the Gateway:

``` bash
    arpspoof -t [Gateway IP] [SUT]
```

4- Listening for DNS traffic involving SUT;
``` bash
    dnsspoof -f spoofhosts.txt host [SUT IP] and udp port 53 
```

An example of the spoofhost file can be:

``` bash
    [Tester IP] mail*
    [Tester IP] www*
```


After the completion of this steps any queries for hosts beginning with www or mail will be answered with an IP address of the machine running the test.
To disable packet forwarding, after the completion of the test, it is needed to insert the following in the terminal:

``` bash
    sysctl -w net.ipv4.ip_forward=0
```
## Cain & Abel

Cain & Abel is a very useful security tool used for decryption and decoding of passwords for a wide array of offline programs and network services.

To perform a DNS spoofing in this tool the user needs to follow the next steps:

1- Install Cain & Abel and open it, go to configure and select your adapter;

2- Select Sniffer option and then select the start/stop sniffer option from the toolbar;

3- Right click in the white area and then click on scan MAC addreses;

4- After scanning click on the APR option in the left bottom corner;

5- click on the "+" sign in the top and select the devices you want to test;

6- After that, select APR-DNS and again click on "+" sign to specify  the websites to be redirected, then click on resolve and type the website name that you want to open up instead of;

7- Click on the start/stop option.

## Ettercap

Ettercap is a comprehensive suite for man in the middle attacks. It offers content filtering on the fly, sniffing of live connections, and many others.

To test against DNS Spoofing with this tool the first step is to launch it by writting in the terminal:

```bash
    ettercap -G
```
The the user needs to perform a ARP attack by doing the following:

1- Click “Sniff->Unified Sniffing”;

2- Choose the interface which you want to use for ARP Poisoning;

3- Click “Hosts->Scan for Host”;

4- Among the outputted list, select the two targets and associate them with Target 1 and Target 2, respectively;

5- Select “Mitm->Arp Poisoning”;

6- Select “Sniff Remote Connection”;

7- “Start->Start Sniffing.

After the ARP is poisoned the user can start to initiate de DNS poisoning by:

1- Opening the /usr/share/ettercap/etter.dns

2- Creating the redirecting paths. An example could be:

``` bash
*.google.co.in A [IP address of server]
*.google.com A [IP address of server]
google.com A [IP address of server]

www.google.com PTR [IP address of server]
www.google.co.in PTR [IP address of server]

```

3- Click “Plugins->Manage Plugins”;

4- Select the “dns_spoof” plugin and double click to activate.

After this test, if the system is not protected, the user will observe that the URL inserted will be redirected to the machine specified in step 2. 

## Wireshark

Wireshark is one of the most used network protocol analyzer with this tool it is possible to observe the the traffic generated and redirected by the testing done with the tools mentioned above. This tool is only available to Windows and MacOS.

To install this tool the user only need to access https://www.wireshark.org/ and click the link to download and install de system.

