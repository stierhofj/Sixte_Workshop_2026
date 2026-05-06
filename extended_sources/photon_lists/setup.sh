# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Set the source position and telescope pointing (the same variables are
# used for both) in degree.
RA="30"
DEC="45"

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: xifu
INSTRUMENT="xifu"

# Output directory, where all generated files will be placed
OUTDIR="output"
# make sure it exists
mkdir -p "${OUTDIR}"

# File stem, all files will start with this string
STEM="simple_extsource"

# Here we set some variables depending on the instrument.
# If you want to use a different instrument, you can change the
# variables in the 'else' section and set the INSTRUMENT variable
# above to the empty string (""). Make sure to uncomment the
# 'echo' line below!

# If instrument is xifu
if [ "${INSTRUMENT}" = "xifu" ]; then
  # Path to the instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/new-athena-xifu/baseline/"

  # The specific instrument configuration (think: observation mode)
  XML="${INSTRUMENT_PATH}/xifu_nofilt_infoc.xml"

  # Exposure time of the observation
  EXP="500000"

# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  XML=
  EXP=
fi
