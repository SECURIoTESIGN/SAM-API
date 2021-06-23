# ProVerif Keyed Hash

According to the LWCAR module the system to be developed will benefit from the use of a Keyed Hash.
An example of the application of a Keyed Hash Protocol with this tool can be observed bellow:

```terminal
type key.

fun mac(bitstring,key):bitstring.
fun hash(bitstring):bitstring.


equation forall m: bitstring, k:key; mac(m,k)=mac(m,k).
equation forall m:bitstring; hash(m)=hash(m).

event SuccessB(bitstring, bitstring).

query m:bitstring, mac:bitstring; event(SuccessB(m, mac)).


free c:channel.

let processA(k:key)=
    new m:bitstring;
    out(c, m);
    out(c, hash(mac(m,k))).


let ProcessB (k:key)=
    in(c, m:bitstring);
    in(c, hmac1:bitstring);
    if hmac1 = hash(mac(m,k)) then 
        event SuccessB(m, hmac1).


process
    new k:key;
    ((!processA(k))|(!ProcessB(k)))


```