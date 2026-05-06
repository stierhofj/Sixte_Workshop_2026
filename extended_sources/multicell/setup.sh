# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Set the source position and telescope pointing (the same variables are
# used for both) in degree.
RA="0"
DEC="0"

# Instrument identifier, used to switch instrument dependent variables below
# Define are: xifu, resolve
INSTRUMENT="xifu"

# Output directory, where all generated files will be placed
OUTDIR="output"
# make sure it exists
mkdir -p "${OUTDIR}"

# File stem, all files will start with this string
STEM="multicell"

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
  EXP="10000" # actual first light exposure!

  # Number of pixels in one direction
  NAXIS="6"

  # Reference pixel
  CRPIX="3.5"

  # Pixel size
  CDELT="85.12516e-04"

# If instrument is xifu
elif [ "${INSTRUMENT}" = "xifu" ]; then
  # Path to the instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/new-athena-xifu/baseline/"

  # The specific instrument configuration (think: observation mode)
  XML="${INSTRUMENT_PATH}/xifu_nofilt_infoc.xml"

  # Exposure time of the observation
  EXP="1000"

  # Number of pixels in one direction
  NAXIS="50"

  # Reference pixel
  CRPIX="25.5"

  # Pixel size
  CDELT="1.5136e-03"

# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  XML=
  EXP=
  NAXIS=
  CRPIX=
  CDELT=
fi
