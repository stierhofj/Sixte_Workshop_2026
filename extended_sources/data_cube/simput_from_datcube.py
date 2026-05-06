import numpy as np
from astropy.io import fits
import astropy.wcs as wcs
import sys

################################################################################
# This script generates a SIMPUT based on the data cube produced in
# build_datcube.py, but should work with any data cube of compatible format.
# 
# Generally, it assumes that the given data cube (in the primary extension)
# contains the source flux in photons/s/cm^2 and converts the spectra accordingly,
# using the energy grid given by the EGRID extension.
# This script then essentially collapses the cube in the energy axis, and turns
# any "pixel" which has flux into its own simput source.
#
# Note that this script is not an official SIXTE tool, though we may create one
# based on it if there's sufficent interest. This code might thus be a little
# awkward!
################################################################################

################################################################################
# reading
################################################################################
if len(sys.argv) != 6:
    print("Usage: simput_from_datcube.py data_cube_file output_file E_min E_max Flux")

infile = sys.argv[1]
outfile = sys.argv[2]

do_extsrc = False  # don't represent source as a set of extended sources

hdu_in = fits.open(infile)

spec_arr = hdu_in[0].data

energy = hdu_in["EGRID"].data

emin = float(sys.argv[3]) #0.3
emax = float(sys.argv[4]) #8
totflux = float(sys.argv[5]) #32e-11

fluxbins = np.argwhere(
             np.logical_and(energy >= emin, energy <= emax)
           ).flatten()

# reshaping for convenience
n_ra = spec_arr.shape[2]
n_dec = spec_arr.shape[1]
n_spec = n_ra * n_dec
spec_arr = np.swapaxes(spec_arr, 0, 2).reshape((n_spec, len(energy)))

################################################################################
# calculate the fluxes
################################################################################
# convert from phots/s/cm^2 to erg/s/cm^2
keV2erg = 1.60218e-9
fluxes = np.sum(spec_arr[:, fluxbins] * energy[fluxbins] * keV2erg, axis=1)
print("Flux sum = {}".format(np.sum(fluxes)))

fluxes *= totflux / np.sum(fluxes)
print("Renormed to {}".format(np.sum(fluxes)))

# convert spec_arr to phots/s/cm^2/keV from phots/s/cm^2/bin
midpoints = (energy[1:] + energy[:-1]) * 0.5
dE = np.ones(energy.shape)
dE[0] = midpoints[0] - energy[0]
dE[-1] = energy[-1] - midpoints[-1]
dE[1:-1] = midpoints[1:] - midpoints[:-1]
spec_arr /= dE


################################################################################
# get ra/dec values
################################################################################
pix_size = hdu_in[0].header["CDELT1"]

bins_ra = range(0, n_ra)
bins_dec = range(0, n_dec)

# use WCS
w = wcs.WCS(hdu_in[0].header)
m_ra, m_dec = np.meshgrid(bins_ra, bins_dec)

skycoords = w.pixel_to_world(m_ra, m_dec, 0)
grid_ra = skycoords[0]
grid_dec = skycoords[1]

# apply same transformation as to spec_arr
grid_ra = np.swapaxes(grid_ra, 0, 1).reshape(n_spec)
grid_dec = np.swapaxes(grid_dec, 0, 1).reshape(n_spec)

################################################################################
# set up the spectra
################################################################################
# Filter out the grid points with flux == 0
hasflux = np.where(fluxes > 0)[0]

fluxes = fluxes[hasflux]
spec_arr = spec_arr[hasflux, :]
grid_ra = grid_ra[hasflux]
grid_dec = grid_dec[hasflux]

n_spec = grid_ra.shape[0]


# create spectra names for the simput tables
# just name by number...
spec_names = ["spec_{}".format(ii+1) for ii in range(n_spec)]

hdu_in.close()


###############################################################################
# prepare the FITS output file
###############################################################################

hdulist = fits.HDUList(fits.PrimaryHDU())


###############################################################################
# image extension - single pixel to simulate extended cells
# note that this does not really work like this (due to projection effects),
# so we skip it
###############################################################################

if do_extsrc:
    img = np.array([[1]])  # single pixel, 2D image

    img_hdu = fits.ImageHDU(img)
    img_hdu.name = "IMG"

    # define WCS
    img_hdu.header["RADESYS"] = "FK5"
    img_hdu.header["EQUINOX"] = 2000

    img_hdu.header["HDUCLASS"] = "HEASARC/SIMPUT"
    img_hdu.header["HDUCLAS1"] = "IMAGE"
    img_hdu.header["HDUVERS"] = "1.1.0"

    img_hdu.header["CTYPE1"] = "RA---TAN"
    img_hdu.header["CTYPE2"] = "DEC--TAN"

    img_hdu.header["CUNIT1"] = "deg"
    img_hdu.header["CUNIT2"] = "deg"

    # pixels are centered at 0/0
    # sixte will then move them around to correctly place them
    # on the sky during the simulation
    img_hdu.header["CRVAL1"] = 0.
    img_hdu.header["CRVAL2"] = 0.

    img_hdu.header["CRPIX1"] = 0.5
    img_hdu.header["CRPIX2"] = 0.5

    img_hdu.header["CDELT1"] = pix_size
    img_hdu.header["CDELT2"] = pix_size

    hdulist.append(img_hdu)

###############################################################################
# spectra extension
###############################################################################

# here, we need to build up individual FITS column objects

# Energy column is just the repeated energy grid
# NOTE: I need to use fixed length columns here - for some reason,
#       writing with variable length causes issues in the last N spectra

c_en = fits.Column(name="ENERGY",
                   format="{}E".format(spec_arr.shape[1]),
                   unit="keV",
                   array=(n_spec)*[energy])

# fluxdensity column is our table, as reshaped above
c_fluxdens = fits.Column(name="FLUXDENSITY",
                         format="{}E".format(spec_arr.shape[1]),
                         unit="photon/s/cm**2/keV",
                         array=spec_arr)

c_name = fits.Column(name="NAME", format="48A", array=spec_names)

spec_hdu = fits.BinTableHDU.from_columns([c_en, c_fluxdens, c_name])
spec_hdu.name = "SPECTRUM"

spec_hdu.header["HDUCLASS"] = "HEASARC/SIMPUT"
spec_hdu.header["HDUCLAS1"] = "SPECTRUM"
spec_hdu.header["HDUVERS"] = "1.1.0"

hdulist.append(spec_hdu)

###############################################################################
# catalog extension - these are the actual source definitions,
# using the data we created above
###############################################################################

c_srcid = fits.Column(name="SRC_ID", format="J", array=range(1, n_spec+1))

# need to create source names - I'll just name them by number
srcnames = ["src_{}".format(ii+1) for ii in range(n_spec)]
c_srcname = fits.Column(name="SRC_NAME", format="64A", array=srcnames)

# RA and Dec were calculated before
c_ra = fits.Column(name="RA", format="D", unit="deg", array=grid_ra)
c_dec = fits.Column(name="DEC", format="D", unit="deg", array=grid_dec)

# Image rotation is zero, scale is 1 (could use this to rescale pixels)
c_irot = fits.Column(name="IMGROTA", format="E", unit="deg", array=n_spec*[0.])
c_iscal = fits.Column(name="IMGSCAL", format="E", array=n_spec*[1.])

# Choose the energy borders for E_MIN and E_MAX
c_emin = fits.Column(name="E_MIN", format="E", unit="keV",
                     array=n_spec*[emin])
c_emax = fits.Column(name="E_MAX", format="E", unit="keV",
                     array=n_spec*[emax])

c_flux = fits.Column(name="FLUX", format="E", unit="erg/s/cm**2", array=fluxes)

# spectrum references must include the relative paths, e.g. the extension name
spec_paths = ["[{},1][NAME=='{}']".format(spec_hdu.name, nam)
              for nam in spec_names]
c_spectrum = fits.Column(name="SPECTRUM", format="64A", array=spec_paths)


if do_extsrc:
    # image references must also include the relative paths
    # note that you could save both the spectra and the images in separate
    # FITS files
    # You would just need to give the full file name here (it uses the
    # FITS file selection syntax)
    imgname = "[{}]".format(img_hdu.name)
else:
    imgname = "NULL"

c_image = fits.Column(name="IMAGE", format="64A", array=n_spec*[imgname])


# no timing information
c_timing = fits.Column(name="TIMING", format="64A", array=n_spec*["NULL"])

cat_hdu = fits.BinTableHDU.from_columns([c_srcid, c_srcname, c_ra, c_dec,
                                         c_irot, c_iscal,
                                         c_emin, c_emax, c_flux,
                                         c_spectrum, c_image, c_timing])

cat_hdu.name = "SRC_CAT"

cat_hdu.header["HDUCLASS"] = "HEASARC/SIMPUT"
cat_hdu.header["HDUCLAS1"] = "SRC_CAT"
cat_hdu.header["HDUVERS"] = "1.1.0"

hdulist.append(cat_hdu)

###############################################################################
# write everything
###############################################################################
hdulist.writeto(outfile, overwrite=True)
