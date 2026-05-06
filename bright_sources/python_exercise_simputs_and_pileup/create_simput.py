import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
from os import environ

outdir = environ["OUTDIR"]

# ########################################################################
# __0__ pre-requisites
# ########################################################################
# create a simputfile for start with a Crab-like spectrum (see exercise 3)
# - Gamma=2.1, nH=0.4, with a flux of 1mCrab (2e-11 erg/s/cm^2) in the 2-10 keV band
# - Source Position at RA=0.0, Dec=0.0
# - note: it is given in the input data as 'input/athenacrab_flux1mCrab.simput'


# ########################################################################
# _1.1_ load the SIMPUT file (it is a normal FITS file)
# ########################################################################
hdulist = fits.open("input/athenacrab_flux1mCrab.simput")

input_src_cat = hdulist[1]  # first extension stores the source catalog
input_spectrum = hdulist[2]  # second extension contains the spectrum
# note: you can use 'fstruct <file>' in the shell to list the structure of the simput file (see simulator manual)

# The following lines can be used to plot the spectrum
energy_grid = input_spectrum.data['ENERGY'][0]  # the [0] is only the first row, as in principle more spectra can be stored
photon_flux = input_spectrum.data['FLUXDENSITY'][0] # PHOTONS/s/cm^2/keV
plt.plot(energy_grid, photon_flux)
plt.ylim([1e-5,1e-1])
plt.xlabel("Energy [keV]")
plt.ylabel("photons/s/cm²/keV")
plt.loglog()
plt.showfig(outdir+"/spectrum.pdf")

###############################################################################################
# _1.2_ create a new source catalog, by copying what we have (first row) and adding a 2nd row #
###############################################################################################
new_src_cat = fits.BinTableHDU.from_columns(input_src_cat.columns, nrows=2)
new_src_cat.header = input_src_cat.header.copy()   # copy all header keywords


# **************************************************************************************
# *** Exercise (1): fill in the blanks [...] *******************************************
# **************************************************************************************
# set the fluxes to 0.5mCrab in the 2-10 keV energy band in the first source
# - note that 1mCrab = 2e-11 ergs/cm2/s  [in the 2-10keV band]
# - remember python starts indexing at "0", so the first source data is located
#   in "new_src_cat.data[0]". Access to the columns of this first source (a row in the
#   source catalog) is then done by adding the name of the column as a second index
# **************************************************************************************
new_src_cat.data[0]['FLUX'] = [...]
new_src_cat.data[0]['E_MIN'] = [...]
new_src_cat.data[0]['E_MAX'] = [...]
# **************************************************************************************


# *************************************************+************************************
# *** Exercise (2): fill in the blanks [...] *******************************************
# *************************************************+************************************
# now we need to set the following columns of the new source: SRC_ID, RA, DEC, FLUX
# - note: you can use 'fstruct <file>' in the shell to list the structure
#         (see simulator manual)
# - shift RA to 2arcmin and leave Dec unchanged
# - remember the flux of this source should be 1.5mCrab (factor 3 higher than
#   the other source flux)
# *************************************************+************************************
# copy the complete information of the first source to the second source (indexed by "1")
new_src_cat.data[1] = (new_src_cat.data.copy())[0]
new_src_cat.data[..][...] = [....]
[...]
# *************************************************+************************************



###############################################################################################
# _1.3_ adding a light curve:
###############################################################################################


# *************************************************+************************************
# *** Exercise (3): fill in the blanks [...] *******************************************
# *************************************************+************************************
#  - now add an exponential decay of the light curve, starting with 10mCrab
#  - we want it decay to half its value at 500sec, meaning the relative flux
#    is given by exp(-time/dt) with dt=500sec
#  - the exponential function is given with 'np.exp()'
# *************************************************+************************************
lc_time = np.arange(0, 1300,0.1) # create a linear time grid from 0-1300 seconds in 0.1sec steps
lc_relativ_flux = np.exp([...])
# *************************************************+************************************

# now let's plot the light curve we created
plt.plot(lc_time, lc_relativ_flux)
plt.xlabel('time [sec]')
plt.ylabel('relative flux')
plt.show()


###############################################################################################
# _1.5_ write the timing extension
###############################################################################################
# important: look at the reference in the SIMPUT format description
# https://hea-www.harvard.edu/heasarc/formats/simput-1.1.0.pdf
# Time Variability Extension -> Light Curve -> Extension Header

# build columns (arrays need to be in one row)
# not that the data is given in the "array=...",  and the units for the time are important (seconds in our case)
c_time = fits.Column(name="TIME",format="D",unit="s",array=lc_time)
c_flux=fits.Column(name="FLUX",format="D",array=lc_relativ_flux)

# create TIMING extension
hdu_timing = fits.BinTableHDU.from_columns([c_time, c_flux])

# set header keywords at are required
hdu_timing.name="TIMING"  # name of the extension
hdu_timing.header["HDUCLASS"] = "HEASARC/SIMPUT"
hdu_timing.header["HDUCLAS1"] = "LIGHTCURVE"
hdu_timing.header["HDUVERS"] = "1.1.0"

# *************************************************+************************************
# *** Exercise (4): fill in the blanks [...] *******************************************
# *************************************************+************************************
# now we also need to set the absolute time reference as additional header keywords
# - note that this needs to match the one given at runsixt (in the next part of the exercise), we suggest to use
#   MJDREF=55000 for both
# - hint: this means we need to set the "MJDREF" key to this value, and the additional TIMEZERO keyword to 0
#   (the latter can be used to define an offset)
# *************************************************+************************************
hdu_timing.header[...] = [...]
[...]
# *************************************************+************************************



# *************************************************+************************************
# *** Exercise (4): fill in the blanks [...] *******************************************
# *************************************************+************************************
# important step: we need to write the name of the timing extension in the SRC_CAT, for
#    source 2 (which is stored in 'new_src_cat.data[1]')
# hint: - look at how it's done for the spectrum (look at the SRC_CAT extension with fdump/fv,
#       and simply exchange the name, the name of the extenwsion (what we stored in
#       'hdu_timing.name')
#       - you can also use 'print(new_src_cat.data[1]['SPECTRUM'])' to display what is stored
#       for the spectrum extension
# *************************************************+************************************
new_src_cat.data[...][...] = '...'
# *************************************************+************************************


###############################################################################################
# _1.5_ write SIMPUT file
###############################################################################################
output_hdulist = fits.HDUList(fits.PrimaryHDU())
output_hdulist.append(new_src_cat)  # add the new SRC_CAT we created
output_hdulist.append(input_spectrum)  # copy the spectrum extension from the input SIMPUT file
output_hdulist.append(hdu_timing)
output_hdulist.writeto(outdir+'/twosources_decay.simput', overwrite=True)
output_hdulist.close()

