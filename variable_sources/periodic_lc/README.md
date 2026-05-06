This example shows how to build a simple SIMPUT file with periodic variability.

You can execute the scripts in order of their numbering - though you should
also read the scripts, of course!

To get an overview of the steps that are executed you can use the 'run' script.
The default setup is that it will only show all steps on the command line but
not execute anything.

If you want to see the commands of one individual step you can execute './run 01',
then only the commands from the first step will be shown.

# Further exercises

## Analyze the output light curve
The input light curve contains components at two frequencies. Find out which!

## Variable periods
A real source does not necessarily have a constant period. This can be
represented in SIMPUT by specifying derivatives of the period up to the fifth
derivative, using specific header keywords in the timing extension.

Using the SIMPUT file format description, find out what these keywords are, and
add them to your SIMPUT file (using either the FTOOL `fthedit` or a scripting
language of your choice). Then, try to run simulations with it!
