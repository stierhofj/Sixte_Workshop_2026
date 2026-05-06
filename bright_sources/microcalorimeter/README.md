This example shows the high-countrate effects encountered when simulating
microcalorimeters, using the example of NewAthena X-IFU.

We first build an (admittedly unphysical) SIMPUT composed of two emission
lines, then simulate it at increasing flux levels. After extracting the
spectra, you can analyze them in your favorite analysis software.

You can then play around with the simulation pipeline and the output files to
get an understanding of the effects of grading and crosstalk, and how to mitigate
them.
Some suggestions:

# Different choice of detector configuration
In `setup.sh`, using the `CONFIG` variable, we choose the "standard" X-IFU
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

# Event filtering
`makespec` can use the FITS extended filename syntax to filter out events under
certain criteria.

`03_extract_spec.sh` already has some suggestions - try them out! How do they
affect your spectra?

Do note that discarding events reduces the effective throughput of the instrument!
