# Test scripts to verify working installation and instrument files

## Setup

To run the exercises in this repository you need simput and sixte installed and at least one set of instrument files. To install the software see <https://www.sternwarte.uni-erlangen.de/sixte/linux/>. Instrument files can be found on this web page as well. When you have followed the installation instructions on the web page you should have a variable _SIXTE_ set. The exercises in this repository check for a variable SIXTE_INSTRUMENTS where it is expected to find the folders which contain all relevant files. If this variable is not set it will be assumed to be _${SIXTE}/share/sixte/instruments_.

Prepare your environment as described in the [manual](https://www.sternwarte.uni-erlangen.de/~sixte/data/simulator_manual.pdf), then navigate to the test/install directory inside the repository. If you have unpacked the instrument files to ${SIXTE}, you are ready to run the test. If you have placed them elsewhere (e.g., /home/user/data/sixte/), please set the environment variable SIXTE_INSTRUMENTS accordingly (e.g., /home/user/data/sixte/share/sixte/instruments).

Run the instrument-specific tests by navigating to each instrument test directory (e.g., test/athena_wfi) and executing the run script. For the workshop, please test at least athena_wfi and new_athena_xifu.

## First step: Verify installation

To ensure that simput and sixte are installed an can be found enter the `install` directory. The numbered scripts in here each test different aspects. The scripts depend on each other such that they should be run in order indicated by their numbering. To run all tests simply execute the `run` script with `./run`. If you are greeted with `Installation seems good!` your are most likely okay. If this is not the case, the error message might hopefully help you to figure out where the problem is. Fix the issue and re-run until you get the mentioned message.

You will also find output files in the output/ folder — including an event file, an image, and a light curve — which you can use to check that you are able to inspect such files.

## Next step: Verify instrument files

Most likely you will not have all instrument files installed. Therefore make sure you know which instrument you are about to use and enter the respective directory. The test scripts contained work the same way as before. To run all tests execute `./run`. Again you want to see a message ending in _seem good!_.
