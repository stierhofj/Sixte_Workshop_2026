## Dithering and Exposure Map example

Here you can find example scripts to simulate the satellite in dithering mode. We will be using the tool "attgen_dither" to generate an attitude file describing the time-varying pointing.

After running the scripts, you can try to calculate the exposure map using the tool "exposure_map". The exposure map specifies the amount of time for which each part of the sky has been observed by the satellite.

_For further information also checkout chapter 10.4.4 of the SIXTE manual._

### Folder structure

You can execute the scripts in order of their numbering - though you should
also read the scripts, of course!

0. [setup.sh](setup.sh) is where you should define your setup parameters for the exercise before starting. 
1. [01_create_simput](01_create_simput) will create the SIMPUT files for the desired sources for the exercise.
2. [02_create_attitude](02_create_attitude) will create a dithering pattern using a Lissajous curve by using the tool "attgen_dither".
3. [03_simulate](03_simulate) will simulate your observation including the previously generated attitude file.
4. [04_chip_image](04_chip_image) will run the python script [chip_image.py](chip_image.py), which will display one chip's image.
5. [05_exposure_map](05_exposure_map) will calculate a short snapshot of the attitude by executing the tool "exposure_map".

* [run](run) script that contains commands to run all the scripts at once, whilst printing out the current progress.
