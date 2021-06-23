# Firmware Cracking

This type of attack is when a third party analyses the firmware of an IoT in order to gain access to useful information that is stored in the firmware code that, sometimes, is in plaintext giving access to sensitive  data  like  default  passwords,  private  IP  addresses,  services  running  on  the  server,  default  ports and their credentials etc.
With the analysis of the firmware it is possible for the tester to see if the firmware of the system under test is revealing any sensible and possibly dangerous information to attackers.


Bellow some tools to test against this type of attack will be presented with instructions to do so.

## IoT Inspector

IoT Inspector is a platform for automated security analysis of IoT firmware. Besides examining the IoT device’s firmware for vulnerabilities, it also checks the compliance with international security standards without requiring access to source code or network or physical access to the IoT device.

This tool allows to:
* Detect vulnerabilities in the firmware of IoT devices
* Check firmware for conformity or non-conformity with the most essential IoT security standards
* Instant results, comprehensive reporting and alerting


## Binwalk

Binwalk is a firmware analysis tool that allows to analyzing,  reverse   engineering, and extracting firmware images.

To install this tool the user needs to download the repository from https://github.com/ReFirmLabs/binwalk, unzip the file and run the following command in the directory of the tool:

``` bash
    sudo python setup.py install
```

To scan the firmware it is only needed:

``` bash
    binwalk firmware.bin
```

To extract the files found in the firmware analysis te user needs to input:

``` bash
    binwalk -e firmware.bin
```
 
 A more in depth guide about the usage of this tool can be found at https://github.com/ReFirmLabs/binwalk/wiki/Usage


There are some additional, but not required, dependencies that might be needed, the instructions to install this dependencies can be found at https://github.com/ReFirmLabs/binwalk/blob/master/INSTALL.md

## QEMU

QEMU is an opensource machine emulator and virtualizer. With this tool it is possible to emulate a system and study the way it works leading to, possibly, finding security flaws in said system. A small tutorial on how to install and run this system on Linux Mint will be presented bellow:

``` bash
    sudo apt install qemu qemu-kvm libvirt-bin
```

After installation, to use this system an image file needs to be created using the quemu-img tool. With thw following command it will be created an image file with the size of 10GB and qcow2 format (default format for QEMU images):

 ``` bash
    qemu-img create -f qcow2 testing-image.img 10G
```

To boot the system the user needs to write:

``` bash
qemu-system-x86_64 -m 1024 -boot d -enable-kvm -smp 3 -net nic -net user -hda testing-image.img -cdrom ubuntu-16.04.iso
```


## FIRMADYNE 

FIRMADYNE is a scalable and  automated tool for performing emulation and dynamic analysis of Linux-based embedded firmware.

First it is needed to install the software and respective dependencies with the following:

``` bash
    sudo apt-get install busybox-static fakeroot git dmsetup kpartx netcat-openbsd nmap python-psycopg2 python3-psycopg2 snmp uml-utilities util-linux vlan
    git clone --recursive https://github.com/firmadyne/firmadyne.git
```

FIRMADYNE uses the tool mentioned above (Binwalk) to perform the extraction of the firmware so the user needs to install this tool with:

``` bash
    
    git clone https://github.com/ReFirmLabs/binwalk.git
    cd binwalk
    sudo ./deps.sh
    sudo python ./setup.py install
    sudo -H pip install git+https://github.com/ahupp/python-magic
    sudo -H pip install git+https://github.com/sviehb/jefferson
```

After this process the databases, pre-built binaries and QUEMO need to be installed:

``` bash
    sudo apt-get install postgresql
    sudo -u postgres createuser -P firmadyne , with password firmadyne
    sudo -u postgres createdb -O firmadyne firmware
    sudo -u postgres psql -d firmware < ./firmadyne/database/schema
    cd ./firmadyne; ./download.sh
    sudo apt-get install qemu-system-arm qemu-system-mips qemu-system-x86 qemu-utils
```

Following the tutorial from https://github.com/firmadyne/firmadyne to use this tool the user needs to:


Set FIRMWARE_DIR in firmadyne.config to point to the root of this repository.
Download a firmware image, e.g. v2.0.3 for Netgear WNAP320.

``` bash
    wget http://www.downloads.netgear.com/files/GDC/WNAP320/WNAP320%20Firmware%20Version%202.0.3.zip
```
    
    
Use the extractor to recover only the filesystem, no kernel (-nk), no parallel operation (-np), populating the image table in the SQL server at 127.0.0.1 (-sql) with the Netgear brand (-b), and storing the tarball in images.

``` bash
    ./sources/extractor/extractor.py -b Netgear -sql 127.0.0.1 -np -nk "WNAP320 Firmware Version 2.0.3.zip" images
```

Identify the architecture of firmware 1 and store the result in the image table of the database.

``` bash
    ./scripts/getArch.sh ./images/1.tar.gz
```

Load the contents of the filesystem for firmware 1 into the database, 
populating the object and object_to_image tables.

``` bash
    ./scripts/tar2db.py -i 1 -f ./images/1.tar.gz
```


Create the QEMU disk image for firmware 1.

``` bash
    sudo ./scripts/makeImage.sh 1
```

Infer the network configuration for firmware 1. Kernel messages are logged to ./scratch/1/qemu.initial.serial.log.

``` bash
    ./scripts/inferNetwork.sh 1
```

Emulate firmware 1 with the inferred network configuration. This will modify the configuration of the host system by creating a TAP device and adding a route.
``` bash
    ./scratch/1/run.sh
```

The system should be available over the network, and is ready for analysis. Kernel messages are mirrored to ./scratch/1/qemu.final.serial.log. The filesystem for firmware 1 can be mounted to and unmounted from scratch/1/image with ./scripts/mount.sh 1 and ./scripts/umount.sh 1.

``` bash
    ./analyses/snmpwalk.sh 192.168.0.100
    ./analyses/webAccess.py 1 192.168.0.100 log.txt
    mkdir exploits; ./analyses/runExploits.py -t 192.168.0.100 -o exploits/exploit -e x (requires Metasploit Framework)
    sudo nmap -O -sV 192.168.0.100
```

The default console should be automatically connected to the terminal. You may also login with root and password. Note that Ctrl-c is sent to the guest; use the QEMU monitor command Ctrl-a + x to terminate emulation.



# Firmware Analysis Toolkit (FAT)

FAT is a toolkit used for firmware emulation. This toolkit is simply an automated script to run FIRMADYNE.

To install this tool it is only needed to run:

``` bash
    git clone https://github.com/attify/firmware-analysis-toolkit
cd firmware-analysis-toolkit
./setup.sh
```

After the successful installation the user needs to edit the file fat.config and provide the sudo password as shown below:

``` bash
    [DEFAULT]
    sudo_password=[Password]
    firmadyne_path=/home/attify/firmadyne
```

To run this emulator the user should input the following:

``` bash
    ./fat.py [firmware file]
```

The source code of this tool can be found at https://github.com/attify/firmware-analysis-toolkit

