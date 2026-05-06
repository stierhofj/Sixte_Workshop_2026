# Pileup study example

In this example a basic simulation is performed first ([01_create_simput](01_create_simput) and [02_run_simulation](02_run_simulation)). This simulation is used to establish a relation between exposure time and valid counts. From this we generate with a [python script](write_exposure_list.py) a list of exposures such that roughly the same number of valid events are achieved for several flux levels of a point source.

Running simulations with the determined exposure and flux levels [04_simulate_flux](04_simulate_flux) gives ratio of valid events vs. piled up (but valid) events. This is commonly called the _pileup fraction_.

A simple [python script](plot_pileup.py) plots the flux dependent pileup fraction.
