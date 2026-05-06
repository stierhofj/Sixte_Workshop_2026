# Setup script for common variables used throughout this exercise

SIXTE_INSTRUMENTS=${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}

# Telescope pointing in degree for the CDFS field.
POINTING_RA="53.13"
POINTING_DEC="-27.8"

# Exposure time of the observation
EXPOSURE="5000"

# Dither amplitude in degree
DITHER_AMPLITUDE="0.035"

# Output directory, where all generated files will be placed
OUTDIR="output"
mkdir -p "${OUTDIR}"

# File stem, all files will start with this string
STEM="cdfs"

# Input SIMPUT catalogs downloaded by the prepare script
SIMPUT_LEHMER="input/CDFS_cat_lehmer.fits"
SIMPUT_GALAXIES="input/CDFS_cat_galaxies.fits"
SIMPUTS="${SIMPUT_LEHMER},${SIMPUT_GALAXIES}"

# Path to the Athena WFI instrument files. Set SIXTE_INSTRUMENTS manually if
# your instrument files live outside the standard SIXTE installation tree.
SIXTE_INSTRUMENTS="${SIXTE_INSTRUMENTS:-${SIXTE}/share/sixte/instruments}"
INSTRUMENT_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/wfi_wo_filter"
CALIBRATION_PATH="${SIXTE_INSTRUMENTS}/athena-wfi/calibration_files"

# The full-frame large detector array without optical blocking filter
XML="${INSTRUMENT_PATH}/ld_wfi_ff_all_chips.xml"

# Calibration file used for exposure map generation
VIGNETTING="${CALIBRATION_PATH}/athena_vig_13rows_20231211.fits"

# Names of generated products used by multiple steps
FIXED_COMBINED_EVT="${OUTDIR}/${STEM}_combined_evt.fits"
DITHER_ATTITUDE="${OUTDIR}/${STEM}_attitude_lissajous.fits"
EXPOSURE_MAP="${OUTDIR}/${STEM}_exposure_map.fits"
DITHERED_COMBINED_EVT="${OUTDIR}/${STEM}_dithered_combined_evt.fits"

# Image grid for the full four-chip WFI field
NAXIS="1063"
CRPIX="532"
CDELT="6.207043e-04"
