# coding: utf-8

# # Two Clusters -- Adapted from the SOXS example, this notebook only generates the SIMPUT file

# Using the SOXS Python interface, this example shows how to generate photons from two thermal spectra and two $\beta$-model spatial distributions, as an approximation of two galaxy clusters. 

# Note that in this particular case, the generated SIMPUT is equivalent to generating two images of the beta profile and attaching them to an APEC spectrum each - meaning there is no change of spectral parameters with position.
# 
# More complex photon lists can be created with SOXS or other packages

import os

import matplotlib

matplotlib.rc("font", size=18)
import soxs


# ### Generate Spectral Models

# We want to generate thermal spectra, so we first create a spectral generator using the ``ApecGenerator`` class:


emin = 0.05  # keV
emax = 20.0  # keV
nbins = 20000
agen = soxs.ApecGenerator(emin, emax, nbins)


# Next, we'll generate the two thermal spectra. We'll set the APEC norm for each to 1, and renormalize them later:


kT1 = 6.0
abund1 = 0.3
redshift1 = 0.05
norm1 = 1.0
spec1 = agen.get_spectrum(kT1, abund1, redshift1, norm1)



kT2 = 4.0
abund2 = 0.4
redshift2 = 0.1
norm2 = 1.0
spec2 = agen.get_spectrum(kT2, abund2, redshift2, norm2)


# Now, re-normalize the spectra using energy fluxes between 0.5-2.0 keV:


flux1 = 1.0e-13  # erg/s/cm**2
flux2 = 5.0e-14  # erg/s/cm**2
emin = 0.5  # keV
emax = 2.0  # keV
spec1.rescale_flux(flux1, emin=0.5, emax=2.0, flux_type="energy")
spec2.rescale_flux(flux2, emin=0.5, emax=2.0, flux_type="energy")


# We'll also apply foreground galactic absorption to each spectrum:


n_H = 0.04  # 10^20 atoms/cm^2
spec1.apply_foreground_absorption(n_H)
spec2.apply_foreground_absorption(n_H)


# ``spec1`` and ``spec2`` are ``Spectrum`` objects. Let's have a look at the spectra:


fig, ax = spec1.plot(
    xmin=0.1,
    xmax=20.0,
    ymin=1.0e-8,
    ymax=1.0e-3,
    label="$\mathrm{kT\ =\ 6\ keV,\ Z\ =\ 0.3\ Z_\odot,\ z\ =\ 0.05}$",
)
spec2.plot(
    label="$\mathrm{kT\ =\ 4\ keV,\ Z\ =\ 0.4\ Z_\odot,\ z\ =\ 0.1}$", fig=fig, ax=ax
)
ax.legend()


# ### Generate Spatial Models

# Now what we want to do is associate spatial distributions with these spectra. Each cluster will be represented using a $\beta$-model. For that, we use the ``BetaModel`` class. For fun, we'll give the second ``BetaModel`` an ellipticity and tilt it by 45 degrees (a bit extreme, but it demonstrates the functionality nicely):


# Parameters for the clusters
r_c1 = 30.0  # in arcsec
r_c2 = 20.0  # in arcsec
beta1 = 2.0 / 3.0
beta2 = 1.0

# Center of the field of view
# clusters are both centered at RA=Dec=0 - we move them later in the SIMPUT catalog
ra0=0
dec0=0

# Now actually create the models
pos1 = soxs.BetaModel(ra0, dec0, r_c1, beta1, ellipticity=0.5, theta=45.0)
pos2 = soxs.BetaModel(ra0, dec0, r_c2, beta2)


# ### Create SIMPUT files

# Now, what we want to do is generate energies and positions from these models. We want to create a large sample that we'll draw from when we run the instrument simulator, so we choose a large exposure time and a large collecting area (should be bigger than the maximum of the ARF). To do this, we use the `from_models()` method of the `SimputPhotonList` class to make instances of the latter:


t_exp = (50.0, "ks")
area = (3.0, "m**2")
cluster_phlist1 = soxs.SimputPhotonList.from_models(
    "cluster1", spec1, pos1, t_exp, area
)
cluster_phlist2 = soxs.SimputPhotonList.from_models(
    "cluster2", spec2, pos2, t_exp, area
)


# We can quickly show the positions using the `plot()` method of the `SimputPhotonList` instances. For simplicity, we'll only show every 100th event using the ``stride`` argument, and restrict ourselves to a roughly $20'\times~20'$ field of view.


fig, ax = cluster_phlist1.plot(
    [0,0], 6.0, marker=".", stride=100, label="Cluster 1"
)
cluster_phlist2.plot(
    [0,0], 6.0, marker=".", stride=100, fig=fig, ax=ax, label="Cluster 2"
)
ax.legend()


# Now that we have the positions and the energies of the photons in the `SimputPhotonList`s, we can write them to a SIMPUT catalog, using the `SimputCatalog` class. Each cluster will have its own photon list, but be part of the same SIMPUT catalog:
# 
# The position of the sources is set by changing their .ra and .dec values, equivalent to choosing different values in the catalog FITS extension of the file.


# Position the SIMPUT sources in the sky

ra_cen = 30
dec_cen = 45

cluster_phlist1.ra = ra_cen - 0.03
cluster_phlist1.dec = dec_cen - 0.03

cluster_phlist2.ra = ra_cen + 0.03
cluster_phlist2.dec = dec_cen + 0.03

# Create the SIMPUT catalog "sim_cat" from the photon lists "cluster1" and "cluster2"
sim_cat = soxs.SimputCatalog.from_source(
    os.getenv("OUTDIR")+"/clusters_simput.fits", cluster_phlist1, overwrite=True
)
sim_cat.append(cluster_phlist2)

