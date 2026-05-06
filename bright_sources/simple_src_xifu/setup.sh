# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Set the source position and telescope pointing (the same variables are
# used for both) in degree.
RA="83.633125"
DEC="22.0145"

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: xifu, resolve
INSTRUMENT="xifu"

# Output directory, where all generated files will be placed
OUTDIR="output"
# make sure it exists
mkdir -p "${OUTDIR}"

# File stem, all files will start with this string
STEM="simple_src_xifu"

# Here we set some variables depending on the instrument.
# If you want to use a different instrument, you can change the
# XML variable

# by default we use the X-IFU
INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/new-athena-xifu/baseline"

# here we choose the standard infocus xml
XML="${INSTRUMENT_PATH}/xifu_nofilt_infoc.xml"
EXP="200"

