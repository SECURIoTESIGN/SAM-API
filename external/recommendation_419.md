# Subvert Trust Controls: Code Signing 

To sign their malware or tools, adversaries can make, acquire, or steal code signing materials. Code signing verifies the developer's validity and ensures that the binary has not been tampered with. The adversary can establish, acquire, or steal the certificates used during an operation.
Code signing certificates may be used to bypass security policies that require signed code to execute on a system.

# Manual Detection

To detect a flaw it is important to collect and analyze signing certificate metadata on software that executes within the environment to look for unusual certificate characteristics and outliers.