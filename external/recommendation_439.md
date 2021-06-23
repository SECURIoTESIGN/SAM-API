# ProVerif Symmetrical Cypher

According to the LWCAR module the system to be developed will benefit from the use of a symmetrical lightweight cryptographic algorithm.
An example of the application of a Symmetrical Protocol with this tool can be observed bellow:

``` terminal 

type key.

fun senc(bitstring, key): bitstring.

reduc forall k:key, m:bitstring; sdec(senc(m, k), k) = m.

free c:channel.
free m:bitstring [private].
free k:key [private].


event SuccessB(bitstring, key).

query attacker (m).
query attacker(k).


let ProcessA=
    out(c, senc(m, k)).


let ProcessB=
    in (c, m1:bitstring);
    let m2 = sdec(m1, k) in 
    if m2=m1 then event SuccessB(m2, k).

process
    ((!ProcessA)|(!ProcessB))

```