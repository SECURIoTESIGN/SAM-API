# ProVerif Hash Functions

According to the LWCAR module the system to be developed will benefit from the use of a Hash function.
An example of the application of hash function with this tool can be observed bellow:

``` terminal

fun hash(bitstring):bitstring.


equation forall m:bitstring; hash(m)=hash(m).

free c:channel.

event SuccessB(bitstring, bitstring).

query m1:bitstring, m2:bitstring; event(SucessB(m1, m2)).

let ProcessA =
    new m1:bitstring;
    out(c, m1);
    out(c, hash(m1)).


let ProcessB=
    in(c, m1:bitstring);
    in(c, hashedm1:bitstring);
    if hash(m1) = hashedm1 then 
    event SuccessB(hash(m1), hashedm1).


process
    ((!ProcessA)|(!ProcessB))


```