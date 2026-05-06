from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
from os import environ

outdir = environ["OUTDIR"]
stem = environ["STEM"]

# We look at one chip here. How does the combined image look?
evtfile = outdir+"/"+stem+"_chip0_evt.fits"

# Open FITS file
with fits.open(evtfile) as hdul:
    data = hdul[1].data

    x = data["rawx"]
    y = data["rawy"]

    hist, xedges, yedges = np.histogram2d(x, y, bins=512)

    plt.imshow(
      hist.T,
      origin="lower",
      aspect="auto",
      extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    plt.colorbar(label="Counts")
    plt.xlabel("RAW X")
    plt.ylabel("RAW Y")
    plt.title("Integrated Image")
    plt.savefig(outdir+"/chip-image.pdf")
