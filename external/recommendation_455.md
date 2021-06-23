# Testing for SEU sensitivity

Single event upsets (SEUs) are caused by ionizing radiation strikes that discharge the charge in storage elements, such as configuration memory cells, user memory, and registers. In terrestrial applications, the two ionizing radiation sources of concern are alpha particles emitted from package impurities and high-energy neutrons caused by the interaction of cosmic rays with the earth's atmosphere. Studies conducted over the last 20 years have led to high purity package materials minimizing SEU effects caused by alpha particle radiation. Unavoidable atmospheric neutrons remain the primary cause for SEU effects today. Soft errors are random and happen according to a probability related to energy levels, flux, and cell susceptibility.

## Manually 

The sensitivity of a device to SEU can be empirically estimated by placing a test device in a particle stream at a cyclotron or other particle accelerator facility. This particular test methodology is especially useful for predicting the SER (soft error rate) in known space environments, but can be problematic for estimating terrestrial SER from neutrons. In this case, a large number of parts must be evaluated, possibly at different altitudes, to find the actual rate of upset.
Another way to empirically estimate SEU tolerance is to use a chamber shielded for radiation, with a known radiation source, such as Caesium-137.
When testing microprocessors for SEU, the software used to exercise the device must also be evaluated to determine which sections of the device were activated when SEUs occurred. 