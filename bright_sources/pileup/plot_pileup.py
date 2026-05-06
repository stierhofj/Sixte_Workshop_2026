import glob
from os import environ
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np

exposure = []
counts = []
flux = []

outdir = environ["OUTDIR"]
stem = environ["STEM"]

# Read exposure file
with open(outdir + "/exposure_list.dat", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        a,b,c = line.split(",")

        exposure.append(float(a))
        counts.append(float(b))
        flux.append(float(c))

valid = []
invalid = []
pileup = []
invalid_pileup = []
for f in flux:
    hdu = fits.open(outdir + "/" + stem + f"_flux{f:.0e}_evt.fits")
    header = hdu[1].header

    valid.append(header["NVALID"])
    invalid.append(header["NINVALID"])
    pileup.append(header["NPVALID"])
    invalid_pileup.append(header["NPINVALI"])


valid = np.array(valid)
invalid = np.array(invalid)
pileup = np.array(pileup)
invalid_pileup = np.array(invalid_pileup)

plt.plot(flux, pileup/valid)

plt.title("Pileup fraction")
plt.xlabel("Flux [cgs]")
plt.ylabel("Fraction [%]")
plt.xscale("log")

plt.show()
