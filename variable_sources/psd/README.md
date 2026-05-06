This example shows how to build a simple SIMPUT file with variability defined
by a power spectral density.

You can execute the scripts in order of their numbering - though you should
also read the scripts, of course!

To get an overview of the steps that are executed you can use the 'run' script.
The default setup is that it will only show all steps on the command line but
not execute anything.

If you want to see the commands of one individual step you can execute './run 01',
then only the commands from the first step will be shown.

# Further exercises

## Analyze the output light curve
Can you reproduce the input power spectral density? For plotting, you can also
use the TIMING extension of the generated SIMPUT, which contains the evaluated
input PSD.

## Reading in a PSD
The interface of `simputfile` allows for the definition of a PSD using up to
five Lorentzians. In case this is not flexible enough for you, you can also
directly read in a PSD from an ASCII file (see Appendix A.2.1 in the simulator
manual). Try this!
