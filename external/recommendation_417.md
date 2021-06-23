# Buffer Overflow

Buffer Overflow is when an attacker takes advantage of improperly used pointers to gain access to information from the system.


## OllyDbg

OllyDbg is an x86 debugger for Windows that focus more on binary code analysis. It traces registers, recognizes procedures, API calls, switches, tables, constants and strings, as well as locates routines from object files and libraries.
To instal this tool the user simply needs to download it from http://www.ollydbg.de/download.htm, unzip it, click in the .exe file and proceed with the required steps.

After installation the tester needs to run the service, open OllyDbg and under "file" select the "attach" command, then select the SUT to attach it.

To verify if the SUT is vulnerable to Buffer Overflow attacks the tester should run a .spk script similar to the one bellow, to try to Overflow the registers.

``` python
    s_readline();
    s_string("[Name of variable to test]");
    s_string_variable("0");
```

To do a spike test on the system the tester needs to input the following:

``` bash
    generic_send_tcp [IP address of SUT] [Port] [Path to .spk file] 0 0
```

While running this program the effects of it in the SUT can be observed in  OllyDbg. If the overflow is successful the application will crash and OllyDbg will pause the program in the moment of said crash and it will show the values stored in the registers and show an access violation message. With this tool it will be possible to observe if an overflow occurred by looking at the EBP and EIP, if any of the sent values overflows to these locations the system is vulnerable to Buffer Overflow attacks.

Tutorial from https://www.youtube.com/watch?v=3x2KT4cRP9o&t=345s

