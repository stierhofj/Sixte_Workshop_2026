# SIXTE online hands-on workshop: NewAthena Simulations

This directory contains supplementary scripts for the day 1 workshop presentation "Introduction to Basic Simulations with SIXTE". The following scripts demonstrate simplified usage of SIMPUT and SIXTE tasks to run and analyse a SIXTE simulation.

**Important**: The scripts can not be run from the get go and require user input. There are empty areas which are meant to be modified while following along the presentation. Example answers can be found on the presentation slides and in the [solutions](solutions) folder provided alongside the extra materials.

## Script running order:

1. Preparation of the simulation inputs using SIMPUT:

* [01_sim_input](01_sim_input) : uses the task simputfile to generate astrophysical source input

2. Running the simulation:

* [02_sim_run](02_sim_run) : uses the task sixtesim to produce an event file, simulating telescope, mirror, and detector model of an instrument

3. Analysing the simulation:

* [03_image_gen](03_image_gen) : uses the task imgev to generate an image of the event file
* [04_spec_gen](04_spec_gen) : uses the task makespec to generate a spectrum 
* [05_lc_gen](05_lc_gen) : uses makelc to generate a light curve; **Note!** this script generates a new simputfile and event file to include a TIMING extension

## [input](input) folder

The [input](input) folder contains an example xcm spectrum file, [mcrab.xcm](input/mcrab.xcm) and an example light curve file [example_lightcurve.dat](input/example_lightcurve.dat).

## [solutions](solutions) folder

Here you can find the solutions for the exercise, which contains the scripts with example answers:

* [11_sim_input](solutions/11_sim_input) : is [01_sim_input](01_sim_input) with filled in gaps for example run.

* [12_sim_run](solutions/12_sim_run) : is [02_sim_run](02_sim_run) with filled in gaps for example run.

* [13_image_gen](solutions/13_image_gen) : is [03_image_gen](03_image_gen) with filled in gaps for example run.

* [14_spec_gen](solutions/14_spec_gen) : is [04_spec_gen](04_spec_gen) with filled in gaps for example run.

* [15_lc_gen](solutions/15_lc_gen) : is [05_lc_gen](05_lc_gen) with filled in gaps for example run.

