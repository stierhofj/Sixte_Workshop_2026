# Setup script for parameters in this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# survey coordinates
RA_SUR=53.13
DEC_SUR=-27.8

# source coordinates
export RA_CEN=53.0360213
export DEC_CEN=-27.7927127

RA_OUT=52.880339
DEC_OUT=-27.57455

RA_EXT=53.36
DEC_EXT=-27.9

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: wfi
export INSTRUMENT="wfi"

# output directory
export OUTDIR="output"
# make sure directory exists
mkdir -p "${OUTDIR}"

# Most output files will start with this stem
export STEM="slew"

# If instrument is wfi
if [ "${INSTRUMENT}" = "wfi" ] ; then
  # Path to instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_w_filter"

  # XML file to use (think: observation mode)
  XML="${INSTRUMENT_PATH}/ld_wfi_ff_all_chips.xml"

  # survey exposure
  export EXP=5000

# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  XML=
  export EXP=
fi
