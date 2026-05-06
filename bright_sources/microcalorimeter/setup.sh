# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Instrument identifier, used to switch instrument dependent variables below                            
# Defined are: xifu
INSTRUMENT="xifu"

# Output directory, where all generated files will be placed
OUTDIR="output"
# make sure it exists
mkdir -p "${OUTDIR}"

# File stem, all files will start with this string
STEM="simple_extsource"

# If instrument is xifu
if [ "${INSTRUMENT}" = "xifu" ] ; then
  INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/new-athena-xifu/baseline"
  # choose an X-IFU configuration. This has two parts:
  # 1. the used filter (nofilt, optical_filter, be_filter)
  # 2. whether the telescope is in focus or defocused
  #
  # run your simulations with different configs and observe the results!
  # the optical and Be filters mostly remove flux at lower energies, so they
  # only make sense to use when you have flux at those energies! 

  CONFIG=nofilt_infoc
  #CONFIG=nofilt_defoc
  #CONFIG=optical_filter_defoc
  #CONFIG=be_filter_defoc

  XML=${INSTRUMENT_PATH}/xifu_${CONFIG}.xml

  # We will perform simulations for different fluxes.
  # Here, we go up to a factor of 1000 - feel free to change this.
  FLUXFACTORS="1 10 100 1000"

  # to keep simulations times ~constant, we will scale down the exposure
  # time when simulating higher fluxes
  BASE_EXP=10000 # exposure for a flux factor of 1

  # if you want to use a different spectral model, change this!
  MODEL=lines
  
# Otherwise you need to provide your own values
else
# uncomment the below line (prepend a '#' sign) and set values after the '=' signs                    
  echo "***error: Instrument '${INSTRUMENT}' not working for this example" >&2 && return 1

  INSTRUMENT_PATH=
  CONFIG=
  XML=
  FLUXCATORS=
  BASE_EXP=
  MODEL=
fi
