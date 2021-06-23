# Hardware Fault Injection

Hardware-implemented fault injection introduces faults into the target system's hardware using additional hardware. Hardware-implemented fault injection methods are divided into two groups based on the faults and their positions.
* Hardware Fault Injection with Contact: The injector is in direct physical contact with the target device, causing voltage or current adjustments on the target chip from the outside. Methods that use pin-level probes and sockets are examples.
* Hardware fault injection without Contact: There is no direct physical interaction between the injector and the goal device. Instead, an external source causes spurious currents within the target chip by inducing physical phenomena such as heavy-ion radiation and electromagnetic interference.

## Manually

### Testing Radiation-based fault injection

Heavy-ion radiation is used to trigger these faults. An ion produces current as it passes through the depletion area of the target system. Injecting faults into the target hardware by placing it in or near an electromagnetic field is also an option. These methods are common among engineers because they closely resemble natural physical phenomena.
