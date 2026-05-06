from astropy.io import fits
import numpy as np
import sys

################################################################################
# Here, we build a very simple data cube - we assume something like an expanding
# shell, producing a gaussian emission line, affected by redshift.

# This means that in the center of the image, we have two cleanly separated
# gaussians, while at the edge, the gaussians overlap at their "rest" energy.
################################################################################


if len(sys.argv) != 2:
    print("Usage: build_datacube.py name_of_output_file")

outfile = sys.argv[1]

# energy grid - we only sample a small part of the spectrum
ebins = np.arange(1.1,1.9,0.5e-3) # keV

# spatial grid - essentially a WCS
cdelt=2/3600 # degree, so 1 arcsec bins
npix=100
crpix = npix/2

# spectral info
# we create two gaussians at high distance in the center of the image
e_cen = (max(ebins) + min(ebins)) / 2
line_sigma = 5e-3

circle_radius = 45 # pixels
central_dE = 0.3 # keV


# build the cube
cube = np.zeros((len(ebins), npix, npix))

X,Y = np.meshgrid(np.linspace(0,npix-1,npix), np.linspace(0,npix-1,npix))

dist_in_pix = np.sqrt((X-crpix)**2 + (Y-crpix)**2)

# emission lines should have zero distance at the edge of the circle
line_distance = central_dE * np.cos(dist_in_pix / circle_radius * np.pi/2)

def gaussian(sigma, mu, x):
    return 1 / np.sqrt(2*np.pi/sigma) * np.exp(- (x-mu)**2 / (2*sigma**2))

# make sure we have no flux outside the radius
rad_filt = dist_in_pix < circle_radius

for ii in range(len(ebins)):
    cube[ii,:,:] += gaussian(line_sigma, e_cen + line_distance, ebins[ii]) * rad_filt
    cube[ii,:,:] += gaussian(line_sigma, e_cen - line_distance, ebins[ii]) * rad_filt

# write the output

# data cube is the primary HDU
phdu=fits.PrimaryHDU(cube)

# set up the WCS
phdu.header["WCSAXES"] = 2
phdu.header["CRPIX1"] = crpix
phdu.header["CRPIX2"] = crpix
phdu.header["CDELT1"] = cdelt
phdu.header["CDELT2"] = cdelt
phdu.header["CUNIT1"] = "deg"
phdu.header["CUNIT2"] = "deg"
phdu.header["CTYPE1"] = "RA--TAN"
phdu.header["CTYPE2"] = "DEC-TAN"
phdu.header["CRVAL1"] = 0
phdu.header["CRVAL2"] = 0

# energy grid is an additional HDU
ehdu = fits.ImageHDU(data=ebins, name="EGRID")

hdulist = fits.HDUList([phdu, ehdu]);
hdulist.writeto(outfile, overwrite=True)
