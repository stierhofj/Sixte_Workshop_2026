#!/bin/env python

"""
This script builds an image of a flat circle with a diameter roughly equal to the
FOV of XRISM Resolve.

It then splits it into two images of the hemispheres, used to generate SIMPUT files.
"""

from astropy.io import fits
from astropy import wcs
import numpy as np
import sys

outdir = sys.argv[1]
stem = sys.argv[2]

# make a "master" image which is a circle
img = np.zeros((101,101))

cen = [50,50]

x = np.arange(0,img.shape[0]) - cen[0]
y = np.arange(0,img.shape[1]) - cen[1]

xx,yy = np.meshgrid(x,y)

img = (np.sqrt(xx**2 + yy**2) < 50) * 100.

# create the WCS
w = wcs.WCS(naxis=2)

# size is encoded here in cdelt - 3 arcmin is the width of the Resolve array
w.wcs.cdelt = np.array([3./60/img.shape[0], 3./60./img.shape[1]])
w.wcs.cunit = np.array(['deg','deg'])
w.wcs.crpix = [cen[0]+1,cen[1]+1]
w.wcs.crval = [45,00]
w.wcs.ctype = ["RA---TAN", "DEC--TAN"]

hdr = w.to_header()

# create an east and west half of the sphere, with a gap in between
img_west = img.copy()
img_west[:,np.where(x>-1)] = 0

img_east = img.copy()
img_east[:,np.where(x<1)] = 0


hdu = fits.PrimaryHDU(header=hdr, data=img)
hdu.writeto(outdir+"/"+stem+"_simput_img.fits", overwrite=True)

hdu = fits.PrimaryHDU(header=hdr, data=img_west)
hdu.writeto(outdir+"/"+stem+"_simput_img_west.fits", overwrite=True)

hdu = fits.PrimaryHDU(header=hdr, data=img_east)
hdu.writeto(outdir+"/"+stem+"_simput_img_east.fits", overwrite=True)
