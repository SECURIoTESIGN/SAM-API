# Assumed-Immutable Data is Stored in Writable Memory

Safe boot, code and data, and system attestation all necessitate implicitly trustworthy assets such as the first stage bootloader, public keys, golden hash digests, and so on. Storing these assets in read-only memory (ROM), fuses, or one-time programmable (OTP) memory ensures their integrity and serves as a foundation for the rest of the system's protection. If properties that were thought to be immutable can be changed, security is lost.

## Manually

To guarantee that the system does not possess this vulnerability the tester needs to make sure that all immutable code or data are programmed into ROM or write-once memory. 