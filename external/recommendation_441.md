# ProVerif Authenticated Encryption

According to the LWCAR module the system to be developed will benefit from the use of an Authenticated Encryption.
An example of the application of an Authenticated Encryption Protocol with this tool can be observed bellow:



``` terminal
type key.

fun mac(bitstring,key):bitstring.

equation forall m: bitstring, k:key; mac(m,k)=mac(m,k).

event SuccessB(bitstring, bitstring).


free c:channel.

query m:bitstring, mac:bitstring; event(SuccessB(m, mac)).


let processA(k:key)=
    new m:bitstring;
    out(c, m);
    out(c, mac(m,k)).


let ProcessB (k:key)=
    in(c, m:bitstring);
    in(c, mac1:bitstring);
    if mac1 = mac(m,k) then 
        event SuccessB(m, mac1).


process
    new k:key;
    ((!processA(k))|(!ProcessB(k)))

```