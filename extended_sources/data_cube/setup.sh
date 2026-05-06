# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Set the source position and telescope pointing (the same variables are
# used for both) in degree.
RA="0"
DEC="0"

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: xifu, wfi, resolve
INSTRUMENT="xifu"

# Output directory, where all generated files will be placed
OUTDIR="output"
# make sure it exists
mkdir -p "${OUTDIR}"

# File stem, all files will start with this string
STEM="data_cube"

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
  EXP="120000"

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
  EXP="1200"

  # Number of pixels in one direction
  NAXIS="50"

  # Reference pixel
  CRPIX="25.5"

  # Pixel size
  CDELT="1.5136e-03"
elif [ "${INSTRUMENT}" = "wfi" ]; then
  # Path to the instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_wo_filter/"

  # The specific instrument configuration (think: observation mode)
  # Here, we only simulate a simplified version of the WFI with a single chip
  # If you want to simulate the full WFI, you will have to perform a slight off-axis
  # pointing in sixtesim, as the source will otherwise be in the chip gaps
  XML="${INSTRUMENT_PATH}/ld_wfi_ff_large.xml"

  # Exposure time of the observation
  EXP="1200"

  # Number of pixels in one direction
  NAXIS="512"

  # Reference pixel
  CRPIX="256.5"

  # Pixel size
  CDELT="6.207043e-4"


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
