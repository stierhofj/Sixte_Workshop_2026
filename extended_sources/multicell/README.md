This example shows how to build an extended source SIMPUT using the `simputmulticell` tool.

*NOTE*: You need to run the `prepare` script to get the required input files!


You can simulate it with either XRISM Resolve or Athena X-IFU - set the
INSTRUMENT
variable in setup.sh to change this.
It's recommended to run X-IFU first, as the degree of cross-contamination is
higher in Resolve.

Afterwards, you can execute the scripts in order of their numbering - though
you should also read the scripts, of course!


# Further exercises

## Plot and fit the spectra
Visualize the "cen" and "out" regions using the generated image files.
After spectral extraction, compare the spectra of the "cen" and "out" regions.
You can also fit them and compare your results with the values of the input maps

## Make images in different color bands
Change the color bands used in the final script
