# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Set the source position and telescope pointing (the same variables are
# used for both) in degree.
RA="83.633125"
DEC="22.0145"

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: wfi, resolve
INSTRUMENT="wfi"

# Output directory, where all generated files will be placed
export OUTDIR="output"
# make sure it exists
mkdir -p "${OUTDIR}"

# File stem, all files will start with this string
export STEM="pileup"

# Here we set some variables depending on the instrument.
# If you want to use a different instrument, you can change the
# variables in the 'else' section and set the INSTRUMENT variable
# above to the empty string (""). Make sure to uncomment the
# 'echo' line below!

# If instrument is resolve
if [ "${INSTRUMENT}" = "resolve" ]; then
  # Path to the instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/xrism/resolve"

  # The specific instrument configuration (think: observation mode)
  XML="${INSTRUMENT_PATH}/resolve_baseline_GVclosed.xml"

  # Exposure time of the observation
  EXP="5000"

# If instrument is xifu
elif [ "${INSTRUMENT}" = "wfi" ]; then
  # Path to the instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_wo_filter/"

  XML="${INSTRUMENT_PATH}/ld_wfi_ff_large.xml"
  EXP="1200"

# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  XML=
  EXP=
fi
