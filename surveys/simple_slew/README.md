## All-Sky survey example

Here you can find example scripts to create an all-sky survey simulation with NewAthena WFI. We do this by decribing the telescope slew over the sky by using attitude files.

_For further information also checkout chapter 10.6.2 of the SIXTE manual._

### Folder structure

You can execute the scripts in order of their numbering - though you should
also read the scripts, of course!

0. [setup.sh](setup.sh) is where you should define your setup parameters for the exercise before starting. 
1. [01_create_simput](01_create_simput) will create the SIMPUT files for the desired sources for the exercise.
2. [02_slew_attitude](02_slew_attitude) will run the Python script [slew_attitude.py](slew_attitude.py), which will generate a slew attitude file.
3. [03_simulate](03_simulate) will simulate your observation including the previously generated slew attitude file.
4. [04_imgev](04_imgev) will generate an example image of the observation.
5. [05_chip_image](05_chip_image) will run the Python script [chip_image.py](chip_image.py), which will display an image of one of the chips.

* [run](run) script that contains commands to run all the scripts at once, whilst printing out the current progress.
* [input](input) contains an example xcm source spectrum file [mcrab.xcm](input/mcrab.xcm) and and image file used to decsribe an extended source [beta.fits](input/beta.fits)

---
_Last updated:04.05.26 by E.G.Gulbahar_
