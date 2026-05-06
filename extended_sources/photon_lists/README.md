This example shows how to work with Photon List based SIMPUTs.

The python scryp create_photlist_simput.py shows how to use the SOXS
software to generate a simple Photon List based SIMPUT
**NOTE**: You do not need to run this script if you do not have SOXS installed - 
the SIMPUT file has already been generated, though with a short exposure time.
If you do have SOXS, feel free to play around with it!

You can then inspect the generated file (input/clusters_simput.fits) and run a quick
X-IFU simulation with it.

The script 02_run_xifu uses the generated simput in input/clusters_simput.fits.
If you generate your own simput it will be located in ${OUTDIR} (most likely 'output'),
so make sure to change the simulation script such that it uses the correct file!

# Further exercises

## Extract spectra and create (multi-color band) images
See the other exercises for examples on how to do this. Do the spectra change
as a function of location within each cluster?
