#!/bin/bash

source ./setup.sh || exit 1  

# --- run the simulation (take care of the absolute time) ---
# sixtesim [....] MJDREF=55000
# - note: we need the same MJDREF when creating the light curve,
#    need to 'observe' during the same absolute time in which we
#    defined the light curve

sixtesim  \
  RA=0.0 Dec=0.0 \
  Prefix=${OUTDIR}/sim_twosources_ \
  Simput=${OUTDIR}/twosources_decay.simput \
  XMLFile=${XML} \
  MJDREF=55000 \
  Exposure=1300 \
  clobber=yes 


# note: you can use ds9 (or fv) to view the event file as an image
# (not on sciserver, though)
