# Setup script for parameters in this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# survey coordinates
RA=0.0
DEC=0.0

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: wfi
INSTRUMENT="wfi"

# output directory
export OUTDIR="output"
# make sure directory exists
mkdir -p "${OUTDIR}"

# Most output files will start with this stem
export STEM="dither"

# If instrument is wfi
if [ "${INSTRUMENT}" = "wfi" ] ; then
  # Path to instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_w_filter"

  # XML file to use (think: observation mode)
  XML="${INSTRUMENT_PATH}/ld_wfi_ff_all_chips.xml"
  
  # Vignetting file for the instrument
  VIGNET="${INSTRUMENT_PATH}/athena_vig_13rows_20231211.fits"

  # survey exposure
  EXP=5000

# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  XML=
  EXP=
fi
