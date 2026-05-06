# Setup script for parameters in this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# pointing coordinates
RA=30
DEC=0

# Instrument identifier, used to switch instrument dependent variables below
# Defined are: wfi
INSTRUMENT="wfi"

# output directory
OUTDIR="output"
# make sure directory exists
mkdir -p "${OUTDIR}"

# Most output files will start with this stem
STEM="psd"

# If instrument is wfi
if [ "${INSTRUMENT}" = "wfi" ] ; then
  # Path to instrument files
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_wo_filter"

  # XML file to use (think: observation mode)
  # Here, we actually use the fast chip of Athena WFI for optimal time
  # resolution
  XML="${INSTRUMENT_PATH}/fd_wfi_ff_df35mm.xml"

  # exposure
  EXP=10000

# Otherwise you need to provide your own values
else
  # uncomment the below line (prepend a '#' sign) and set values after the '=' signs
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  XML=
  EXP=
fi
