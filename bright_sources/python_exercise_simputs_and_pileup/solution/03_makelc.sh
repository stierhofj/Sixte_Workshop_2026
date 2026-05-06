#!/bin/bash

# --- create light curve of each source, using the extended filename syntax ---
# makelc EvtFile='sim_twosources_decay_evt.fits[EVENTS][sum(SRC_ID)==1]' [...]
# makelc EvtFile='sim_twosources_decay_evt.fits[EVENTS][sum(SRC_ID)==2]' [...]
#  - best put in a shell script
#  - the 'sum(SRC_ID)==2' is necessary as SRC_ID can be an array, as in an unlikely case
#    more than 1 photon can contribute to an array
#  - alternatively, a selection with [RA<?? && RA>?? && Dec<?? && Dec>??] works as well

makelc \
    EvtFile="${OUTDIR}/sim_twosources_evt.fits[EVENTS][sum(SRC_ID)==2]" \
    LightCurve=${OUTDIR}/lc_decay.fits \
    dt=10.0 \
    length=1300 \
    clobber=yes 

makelc \
    EvtFile="${OUTDIR}/sim_twosources_evt.fits[EVENTS][sum(SRC_ID)==1]" \
    LightCurve=${OUTDIR}/lc_const.fits \
    dt=10.0 \
    length=1300 \
    clobber=yes
