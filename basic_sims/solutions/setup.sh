# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: wfi
export INSTRUMENT="wfi"

# If instrument is wfi
if [ "${INSTRUMENT}" = "wfi" ]; then
  # Path to the instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_w_filter"

  # The specific instrument configuration (think: observation mode)
  XML="${INSTRUMENT_PATH}/ld_wfi_ff_large.xml"
  
# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  XML=
fi
