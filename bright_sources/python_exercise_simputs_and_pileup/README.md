# Exercise : creating a SIMPUT file with multiple sources and a light curve

The scripts here exercise and not working in their current form. The are prepared to guide you through the exercise. The solutions are in `solutions/`.

## (0) create a SIMPUT file of a point source with a Crab spectrum and a
    flux of 0.5\,mCrab (1e-11erg/cm²/s in the 2-10\,keV energy band);
    note that you use the SIMPUT file input/athenacrab_1mCrab.simput given
    in the data package and set the proper flux values

## (1) add a second source 2 arcmin away form the first one
 - use the script create_simput.py for this and fill in the
   blanks
 - create a simput with both sources, re-using the first simput
 - set the flux of the second source a factor 3 higher (to 1.5 mCrab)
 - calculate a relative light curve, starting at 1, decaying
   exponentially such that it is at a value of 0.5 at t=500sec (total
   length of the light curve should be 1300sec)
 - add this light curve as timing extension to the SIMPUT file and
   attach it to the second source (the one starting at 1.5 mCrab)

## (2) simulate a 1300sec observations with the WFI large chip     (`02_runsixt`)

## (3) extract a light curve of each source with makelc (`03_makelc`)
 - use the extended filename syntax for this (see simulator manual),
   which should look like
   "makelc EvtFile='sim_twosources_decay_evt.fits[EVENTS][sum(SRC_ID)==1]'  [...]  "
   for the first source
 - best put in a shell script
 - the 'sum(SRC_ID)==1' is necessary as SRC_ID can be an array, as in
   an unlikely case more than 1 photon can contribute to an array
 - alternatively, a selection with [RA<?? && RA>?? && Dec<?? &&
   Dec>??] works as well

## (4) plot the light curve and compare it with the input from the SIMPUT
 - you can use the script analysis.py for this and fill in the blanks
 - question: why does the decaying light curve not follow the input?

## (5) Bonus 1: calculate the pile-up fraction

## (6) Bonus 2: redo the simulation with an appropriate detector/readout    configuration
 - verify that the extracted light curve now follows the simulated one
 - what is the pile-up fraction now?

