from astropy.io import fits
import numpy as np
from os import environ

outdir = environ["OUTDIR"]

exp = float(environ["EXP"])
ra_cen = float(environ["RA_CEN"])
dec_cen = float(environ["DEC_CEN"])

# not corrected for declination!
ra_dir = 0.00003/2
dec_dir = -0.00002/2

time    = np.linspace(0.,exp,1000)   # number of time steps from 0 to EXP
ra      = ra_cen + (time-np.mean(time))*ra_dir # linear motion
dec     = dec_cen + (time-np.mean(time))*dec_dir
rollang = np.zeros(1000) # roll angle, zero for this case

# Define FITS columns
ftime    = fits.Column(name='TIME', format='D', array=time)
fra      = fits.Column(name='RA', format='D', array=ra) # 32-bit float
fdec     = fits.Column(name='DEC', format='D', array=dec)  # 1-char string
frollang = fits.Column(name='ROLLANG', format='D', array=rollang)

# Create a binary table HDU
hdu = fits.BinTableHDU.from_columns([ftime, fra, fdec, frollang])

hdu.name = "ATT"

# Set necessary headers
hdu.header["EXTNAME"] = "SLEW_ATTITUDE"
hdu.header["TUNIT1"]  = 's'
hdu.header["TUNIT2"]  = 'deg'
hdu.header["TUNIT3"]  = 'deg'
hdu.header["TUNIT4"]  = 'deg'
hdu.header["MJDREF"]  = 55000.
hdu.header["TSTART"]  = 0.
hdu.header["TSTOP"]   = 5000.
hdu.header["ALIGNMEN"]= 'NORTH'

# Write to file
hdu.writeto(outdir+'/slew_attitude.fits', overwrite=True)
