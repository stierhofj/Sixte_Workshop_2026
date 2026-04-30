# Parameters for the test simulation

# Location of the test insturment files
INSTRUMENT_PATH="input"
XML="${INSTRUMENT_PATH}/dummy.xml"

# Define where the output is placed
OUTDIR="output"
# ensure directory exists
mkdir -p ${OUTDIR}

# file stem
STEM="dummy"

# exposure time
EXP="300"

# right ascesion and declination
RA="0.0"
DEC="0.0"

# The minimum required simput version
SIMPUT_VERSION="2.7.3"

# The minimum required sixte version
SIXTE_VERSION="3.3.3"
