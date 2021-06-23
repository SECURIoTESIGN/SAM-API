# Avoid Incorrect Selection of Fuse Values

Secret data, such as protection configuration data, is often stored in fuses. A fuse is assumed to store a logic 0 when it is not blown, and a logic 1 when it is blown. Fuses are usually one-directional, meaning that once blown to logic 1, they cannot be reset to logic 0. An intruder may blow the fuse and force the device into an insecure state if the logic used to evaluate system security state (by exploiting the values sensed from the fuses) uses negative logic.


## Guide to Select Fuse Values

* **Select the fuse type** Select from time-delay fuses for inductive loads or fast-acting fuses for resistive loads.
* **Select the voltage rating required** The voltage rating must be equal to or greater than the circuit voltage for the proper application of an overcurrent protective device. The device can have a higher rating, but not a lower one; when an overcurrent protective device is applied beyond its rating, there may be potential for fire and arcing energy, posing a severe fire risk to other components in the panel.
* **Verify that the interrupting rating of the selected fuse is sufficient for the circuit application** The interrupting rating must be equal to or greater than the available short-circuit current. An overcurrent protective device must be able to safely interrupt short-circuit currents to which the equipment can be subjected. If the fault current exceeds a level beyond the capacity of the protective device, the device may rupture, causing additional damage. Therefore, it is important to use a fuse that can sustain the largest potential short-circuit currents. Failure to apply fuses with the appropriate interrupting rating can be a serious safety hazard.


Taken from: https://www.controleng.com/articles/three-steps-to-select-the-right-fuse-for-control-circuit-protection/