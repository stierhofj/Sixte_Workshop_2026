This example shows how to build an extended source SIMPUT from a
three-dimensional data cube

You can simulate it with either XRISM Resolve or Athena X-IFU - set the
ISNTRUMENT
variable in setup.sh to change this.

Afterwards, you can execute the scripts in order of their numbering - though
you should also read the scripts, of course!

To get an overview of the steps that are executed you can use the 'run' script.
The default setup is that it will only show all steps on the command line but
not execute anything.

If you want to see the commands of one individual step you can execute './run 01',
then only the commands from the first step will be shown.

# Further exercises

## Plot and fit the spectra
Visualize the "cen" and "edge" regions using the generated image files.
After spectral extraction, compare the spectra of the "cen" and "edge" regions.
You could also extract spectra from different regions, such as several annuli.

## Create narrow-band images
To reveal the "3D" structure of our source, you can create images in several
narrow energy bands, creating a "movie" which steps through energy.
