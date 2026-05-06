This example shows the application of the sixte_arfgen tool to the extraction
of source spectra from surveys using the Athena WFI.

You can execute the scripts in order of their numbering - though you should
also read the scripts, of course!

After running the scripts, fit your spectra either with the "standard" SIXTE
ARFs (automatically written into the .pha file headers by makespec) or the ARFs
you generated. How do the retrieved spectral parameters and source fluxes
change?

# Further Tasks
## ARF sampling
To generate our ARFs, we currently generate 10,000 photons for every 10th bin.
You can play with both parameters to see what effect this would have on the
corrected ARF files!
