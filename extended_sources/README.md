This directory contains multiple SIXTE simulation pipelines, showing how to generate SIMPUT files, run simulations, and analyze their output, focused on extended sources.

**NOTE**: If you are running your own installation of SIXTE, you may need to modify the `xml_setup.sh` file in this directory, such that it correctly retrieves the instrument files needed for the simulations!

There are several exercises:

# simple_extsource
Create a simple extended source whose spectrum does not vary with position.

# multispec
Create a spatially variable extended source based on 2D parameter maps.

# multicell
Create a spatially variable extended source based on a 3D parameter grid. It's recommended to run the `multispec` example first.

# photon_list
Run simulations using a simple photon-list based SIMPUT file.

# mixing
Run a simulation with two neighboring extended sources whose spectra cross-contaminate each other, and account for this effect in spectral fitting.

# data cube
Create an extend source SIMPUT from a 3D data cube (RA, Dec, Energy)
