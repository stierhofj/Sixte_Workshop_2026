# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# output directory
export OUTDIR='output'
# make sure it exists
mkdir -p ${OUTDIR}

# by default we use the WFI
INSTRUMENT='wfi'

# If instrument is WFI
if [ ${INSTRUMENT} = 'wfi' ] ; then
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_w_filter"

  # here we choose the standard infocus xml
  XML="${INSTRUMENT_PATH}/ld_wfi_ff_large.xml"


# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=

  XML=
fi
