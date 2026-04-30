# simulation_examples

## General purpose
This repository contains example simulations to be presented at, e.g., workshops.

## Organization
Top level folders should contain broad categories of simulations, such as extended sources, bright sources, surveys, etc.

These folders can have subfolders which contain indivdual simulation threads. These threads should be executable by users with minimal setup (such as providing the location of XMLs). 

If using external SIMPUTs, a prepare script (prepare.sh) is provided for each example. This script downloads necessary data (if not already available).

## Preparation
To ensure that a working SIXTE & SIMPUT environment is present the folder 'test' contains a number of scripts that check various files and programs. They are setup in the same way as the exercises. Users should make sure that at least the test/install thread runs successful and any of the required instruments.

## Running an exercise
To run a simulation example enter the relevant folder. The scripts expect to find all required tools in PATH and that all required instrument files are found in a path stored in SIXTE_INSTRUMENTS

An overview of the full exercise is provided with a script 'run' which per defaul only displays the commands that are executed for this thread in order.

## Navigation help

Each exercise is separated into tasks represented by scripts 01_<extercise>, 02_<exercise>, ... Each task runs a step in the exercise and usually requires that the previous steps have been executed sucessfully. Almost all exercises are configured with a setup.sh script, which can be used to customize the script, however, when starting completely from zero it is best to ignore the setup script initially. Each exercise also contains a script 'run', when executed prints all comands that are run for this exercise on the command line. This is useful to inspect all basic comands with the command line parameters. A specific step may be shown only by providing the two digit number as argument (e.g., './run 01'). Sometimes an exercise requires additional files, those are provided in a folder 'input', and for external files (mostly for larger files) a script 'prepare' is provided downloading the relevant data.

For reference here is a (fictitious) exercise structure:

- prepare   # if this script exists, it must be run once before any of the tasks.
- README.md # for information about this exercise check the readme!
- 01_simput # task creating a simput file
- 02_simrun # task running simulation
- 03_imgev  # task generating an image
- run       # script that allows to inspect all or a selected task (also allows to run all task after modification)
- setup.sh  # a script that is sourced by all task scripts and sets common variables
- input/    # folder in which necessary files are located
- output/   # output folder, usually generated files will be placed here (can be configured in setup.sh)
