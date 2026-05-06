import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
from os import environ

outdir = environ["OUTDIR"]

###############################################################################################
# _4_ plot the light curves and compare it with the input
###############################################################################################

# helper function to get a light curve with 'time', 'count rate', and 'error rate'
def get_lightcurve(filename_lc):
    lc = fits.getdata(filename_lc, ext=1)
    lc_header = fits.getheader(filename_lc, ext=1)

    dt = lc_header['TIMEDEL']
    counts_per_bin = lc['COUNTS']

    # define a time grid, where with start of each bin of width dt [0, dt, 2*dt, ...]
    time_lo = np.arange(0, len(counts_per_bin)) * dt
    count_rate = counts_per_bin / dt
    err_rate = np.sqrt(counts_per_bin) / dt

    time_bin_middle = time_lo + 0.5 * dt

    return time_bin_middle, count_rate, err_rate


# now, we call our helper function and plot the values
(lc_const_time, lc_const_countrate, lc_const_err) = get_lightcurve(outdir+'/lc_const.fits')
plt.errorbar(lc_const_time, lc_const_countrate, yerr=lc_const_err, fmt='.')

(lc_decay_time, lc_decay_countrate, lc_decay_err) = get_lightcurve(outdir+'/lc_decay.fits')
plt.errorbar(lc_decay_time, lc_decay_countrate, yerr=lc_decay_err, fmt='.')

# **************************************************************************************
# *** Exercise (1): fill in the blanks [...] *******************************************
# **************************************************************************************
# read the timing extension from the SIMPUT-file and compare it with our input
# - again the columns of the Simput file loaded in python is accessed by the
#   string, which has the column name in it, so to get the time of the light curve
#   we use '[TIME]'
# - note, you can always use 'fstruct twosources_decay.simput' to display the column
#   names
# **************************************************************************************
lc_reference = fits.getdata(outdir+'/twosources_decay.simput', extname='TIMING')
ref_time = lc_reference['TIME']
ref_flux = [...]
# **************************************************************************************


# **************************************************************************************
# *** Exercise (2): fill in the blanks [...] *******************************************
# **************************************************************************************
# now we need to plot the reference light curve we just loaded form the simput file
# - remember that the light curve given in the SIMPUT-file is relativ to the 'SRCFLUX'
#   given in the SIMPUT-SRC_CAT extensions for the source, so we need to re-normalize the flux
# - as we know that for the constant source we have 0.5mCrab and for the decaying source
#   set 1.5mCrab, we need to multiply the relative light curve with 3 times the mean-count-rate of the constant
#   source
# - fill in the correct flux value
# **************************************************************************************
mean_count_rate_constant_source = np.mean(lc_const_countrate)
plt.plot(ref_time, [...])
# **************************************************************************************

plt.xlabel("Time [sec]")
plt.ylabel("Count Rate [counts/sec]")
plt.savefig(outdir+"/lightcurve.pdf")
