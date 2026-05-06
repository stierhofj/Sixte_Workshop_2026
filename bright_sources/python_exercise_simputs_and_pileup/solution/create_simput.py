import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
from os import environ

outdir = environ["OUTDIR"]

# #####  for installing if not available #####
# - pip install numpy
# - pip install astropy
# - pip install matplotlib
# ############################################


# ##### __4.0__ pre-requisites #####
# create a simputfile for start with a Crab-like spectrum (see exercise 3)
# - Gamma=2.1, nH=0.4, with a flux of 1mCrab (2e-11 erg/s/cm^2) in the 2-10 keV band
# - Source Position at RA=0.0, Dec=0.0
# ##################################



# ########################################################################
# ##### __4.1__ create a SIMPUT file with two source plus light curve ####
# ########################################################################

# _4.1.1_ load the SIMPUT file (it is a normal FITS file)
hdulist = fits.open("input/athenacrab_flux1mCrab.simput")

input_src_cat = hdulist[1]  # first extension stores the source catalog
input_spectrum = hdulist[2]  # second extension contains the spectrum
# note: you can use 'fstruct <file>' in the shell to list the structure (see simulator manual)

# __ uncomment these lines to plot the spectrum  __
energy_grid = input_spectrum.data['ENERGY'][0]  ## the [0] is only the first row,
photon_flux = input_spectrum.data['FLUXDENSITY'][0] # PHOTONS/s/cm^2/keV
plt.plot(energy_grid, photon_flux)
plt.ylim([1e-5,1e-1])
plt.xlabel("Energy [keV]")
plt.ylabel("photons/s/cm²/keV")
plt.loglog()
plt.savefig(outdir+"/spectrum.pdf")


# _4.1.2_ create a new source catalog, by copying what we have (first row) and adding a 2nd row
new_src_cat = fits.BinTableHDU.from_columns(input_src_cat.columns, nrows=2)
new_src_cat.header = input_src_cat.header.copy()   # copy all header keywords

# set the fluxes to 0.5mCrab in the 2-10 keV energy band
new_src_cat.data[0]['FLUX'] = 0.5 * 2e-11 # 1mCrab = 2e-11 ergs/cm2/s  [in the 2-10keV band]
new_src_cat.data[0]['E_MIN'] = 2.0
new_src_cat.data[0]['E_MAX'] = 10.0

new_src_cat.data[1] = (new_src_cat.data.copy())[0]   # copy the complete information of the first source
new_src_cat.data[1]['SRC_ID'] = 2   # set the SRC ID
new_src_cat.data[1]['RA'] = 2./60  # 2 min distance
new_src_cat.data[1]['DEC'] = 0.0
new_src_cat.data[1]['FLUX'] = 1.5 * 2e-11  # 1.5mCrab, factor 3 higher than the other source flux


# _4.1.3_ adding a light curve:
#    - now add an exponential decay of the light curve, starting with 10mCrab
#      we want it decay to half its value at 500sec, meaning the relative flux
#      is given by exp(-time/dt) with dt=500sec
lc_time = np.arange(0, 1300,0.1)  # create a linear time grid from 0-1300 seconds in 0.1sec steps
dt = 500.0
lc_relativ_flux = np.exp(-lc_time * np.log(2) / dt)


# _4.1.4_ write the timing extension
# important: look at the reference in the SIMPUT format description
# https://hea-www.harvard.edu/heasarc/formats/simput-1.1.0.pdf
# Time Variability Extension -> Light Curve -> Extension Header

# build columns (arrays need to be in one row)
c_time = fits.Column(name="TIME",format="D",unit="s",array=lc_time)
c_flux=fits.Column(name="FLUX",format="D",array=lc_relativ_flux)

# create TIMING extension
hdu_timing = fits.BinTableHDU.from_columns([c_time, c_flux])

# set header keywords at are required
hdu_timing.name="TIMING" # name of the extension
hdu_timing.header["HDUCLASS"] = "HEASARC/SIMPUT"
hdu_timing.header["HDUCLAS1"] = "LIGHTCURVE"
hdu_timing.header["HDUVERS"] = "1.1.0"
hdu_timing.header["MJDREF"] = 55000  # important: needs to match the one given at runsixt
hdu_timing.header["TIMEZERO"] = 0    # we could define a time offset here


# ## important step: we need to write the name of the timing extension in the SRC_CAT, for
#    source 2 (which is stored in 'new_src_cat.data[1]')
#    hint: look at how it's done for the spectrum and simply exchange the name,
#          the name is what we stored in 'hdu_timing.name'
new_src_cat.data[1]['TIMING'] = '[TIMING,1]'


# _4.1.5_ in a last step, we create a new FITS file (just add all extsion and write it to a file)
output_hdulist = fits.HDUList(fits.PrimaryHDU())
output_hdulist.append(new_src_cat)  # add the new SRC_CAT we created
output_hdulist.append(input_spectrum)  # copy the spectrum extension from the input SIMPUT file
output_hdulist.append(hdu_timing)
output_hdulist.writeto(outdir+'/twosources_decay.simput', overwrite=True)
output_hdulist.close()


# _4.1.6_ now let's plot the light curve we created and added to the SIMPUT file
plt.plot(lc_time, lc_relativ_flux)
plt.xlabel('time [sec]')
plt.ylabel('relative flux')
plt.savefig(outdir+"/simput-lightcurve.pdf")
