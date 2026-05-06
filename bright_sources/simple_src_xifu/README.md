This example shows the high-countrate effects encountered when simulating
microcalorimeters, using the example of NewAthena X-IFU.

We first build basic SIMPUT composed with a rather low flux. You can then play around with the simulation pipeline and the output files to get an understanding of the effects of grading and crosstalk, and how to mitigate them.

Some suggestions:

# Different choice of detector configuration
In `setup.sh`, using the `XML` variable, we choose the "standard" X-IFU
configuration by default - an in-focus observation with no additional filter.

You can instead choose to enable defocusing (use the DETX and DETY columns of
the event files to visualize this effect), and see the effect on your spectra.

You may also use a different filter!

# Information in event files
By examining the output event file, you can gather information on how strongly
you are affected by high count rate effects.

The `GRADING` column indicates the grade of the event (1 being the highest
resolution), while the `E_XT` and `N_XT` indicate the energy shift caused by
crosstalk and the number of photons causing this crosstalk, respectively. Try
to plot these columns, for example by making histograms!

The header of the `EVENTS` extension also contains useful summary statistics,
such as `NVALID`, `NINVALID`, `NGRAD1` and so on (see the header comments for
their meaning). You can use these header keys to make a plot of the instrument
throughput as a function of source flux.
certain criteria.

`03_check_grading.sh` already has some ideas on how to analyze the event file and find out how the grading is distributed. 




