# Man in the Middle Attack

This type of attack is used to eavesdrop the traffic between the smart device and the gateway by using an Address Resolution Protocol (ARP) poisoning to redirect all traffic to the device of the attacker.

Bellow some tools to test against this type of attack will be presented with instructions to do so. If the system is not secured against this type of attacks the tools will succeed in penetrating the system.

## Bettercap

Bettercap is a framework that aims to offer to security researchers, red teamers and reverse engineers an easy to use, all-in-one solution with all the features they might possibly need for performing reconnaissance and attacking WiFi networks, Bluetooth Low Energy devices, wireless HID devices and Ethernet networks.

An easy MITM attack to capture credentials with this tool is performed as follows:

1- Install the framework with:
 ``` bash
    sudo apt-get install build-essential ruby-dev libpcap-dev net-tools
    apt-get update
    apt-get dist-upgrade
    apt-get install bettercap
```

2- Initiate bettercap:
``` bash
    bettercap
```

3- When bettercap discovers the target you are looking for, note down its IP address. Let us call it TARGET_IP.

4- Run the command:

``` bash
    bettercap -T [TARGET_IP] — proxy -P POST 
```

After the insertion of this commands the terminal will show all the data being captured from the victim who is accessing the specified website, including credentials that are inserted. When accessing the attacked website the url goes from HTTPS to HTTP in order for the tester to see the information in plain text.


## Ettercap

Ettercap is a comprehensive suite for man in the middle attacks. It offers content filtering on the fly, sniffing of live connections, and many others.

First the user needs to install and launch ettercap with:
``` bash
    sudo apt install ettercap-common
    ettercap -G
```

After the GUI has opened the user should do the following:

1- Hit the ‘sniff’ button and choose United sniffing;

2- Select the network interface that is in your use at the moment;

3- Click on the host tabs and choose one of the lists. If there’s no appropriate host available, you may click the scan host to see more options;

4- Designate an host to Target 1 and other to target 2. After this selection the user will be in the middle of the communications between these two hosts.

5- Click the MITM tab and select ARP poisoning;

6- Select it and it will open a pop window. Select "Sniff remote connections"

8- Finally, go to the start menu where you may finally begin with the attack.

To have access to the packets the user needs to install Wireshark.
After the installation of this tool, to launch the system the user needs to write on the terminal "wireshark" and, after the program is loaded, read the information sent on the network.

## Cain & Abel

Cain & Abel is a very useful security tool used for decryption and decoding of passwords for a wide array of offline programs and network services.

To perform a MitM attack with this tool the user needs to follow the next steps:

1- Activate the sniffer by clicking the "Sniffer" button to allow the network adapter discover local area network IP addresses.

2- Scan for list of IP address to target the victim traffic, by clicking on the button with the "+" icon;

3- Add the range of IP’s to scan;

4- Select All hosts in the Subnet;

5- Select the system under test Ip and default gateway so that the ARP request can be sent;

6- Poison the SUT network by clicking the button with the radioactive icon;

After following this steps the SUT traffic will be captured to the users computer to be analysed.

In order to facilitate the use of this tool a tutorial with images can be found at https://gbhackers.com/man-in-the-middle-attack-with-cain-and-abel-tool/



