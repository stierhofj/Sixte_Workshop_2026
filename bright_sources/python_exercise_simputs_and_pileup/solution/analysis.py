import numpy as np
from astropy.io import fits
from matplotlib import pyplot as plt
from os import environ

outdir = environ["OUTDIR"]

# helper function to get a light curve with 'time', 'count rate', and 'error rate'
def get_lightcurve(filename_lc):
    lc = fits.getdata(filename_lc, ext=1)
    lc_header = fits.getheader(filename_lc, ext=1)

    tstart = lc_header['TSTART']
    dt = lc_header['TIMEDEL']
    counts_per_bin = lc['COUNTS']

    # define a time grid, where with start of each bin of width dt [0, dt, 2*dt, ...]
    time_lo = np.arange(0, len(counts_per_bin))*dt  + tstart
    count_rate = counts_per_bin / dt
    err_rate = np.sqrt(counts_per_bin) / dt

    time_bin_middle = time_lo + 0.5*dt

    return time_bin_middle, count_rate, err_rate


# now, we call our helper function and plot the values
(lc_const_time, lc_const_countrate, lc_const_err) = get_lightcurve(outdir+'/lc_const.fits')
plt.errorbar(lc_const_time, lc_const_countrate, yerr=lc_const_err, fmt='.')

(lc_decay_time, lc_decay_countrate, lc_decay_err) = get_lightcurve(outdir+'/lc_decay.fits')
plt.errorbar(lc_decay_time, lc_decay_countrate, yerr=lc_decay_err, fmt='.')

# read the timing extension from the SIMPUT-file and compare it with our input
lc_reference = fits.getdata(outdir+'/twosources_decay.simput', extname='TIMING')
ref_time = lc_reference['TIME']
ref_flux = lc_reference['FLUX']

# we need to re-normalize the flux:
# - remember that the light curve given in the SIMPUT-file is relativ to the 'SRCFLUX'
#   given in the SIMPUT-SRC_CAT extensions for the source
# - as we know that for the constant source we have 0.5mCrab and for the we set SRCFLUX=1.5mCrab
#   we need to multiply the relativ light curve with 3 times the mean-count-rate of the constant
#   source
mean_count_rate_constant_source = np.mean(lc_const_countrate)
flux_normalization_factor = 3*mean_count_rate_constant_source
plt.plot(ref_time, ref_flux * flux_normalization_factor)

plt.xlabel("Time [sec]")
plt.ylabel("Count Rate [counts/sec]")
plt.savefig(outdir+'/lightcurve.pdf')
