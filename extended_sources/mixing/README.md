This example shows the effect of spatial-spectral mixing, in which the photons
from different source regions contaminate their respective detector regions.

You can simulate it with either XRISM Resolve or NewAthena X-IFU - set the
INSTRUMENT
variable in setup.sh to change this.
It's recommended to run Resolve first, as the degree of cross-contamination is
higher - for this particular example, this effect is very weak in X-IFU.

Afterwards, you can execute the scripts in order of their numbering - though
you should also read the scripts, of course!


# Further exercises

## Estimate the degree of cross-contamination

After running your simulation:
Using region filtering and the SRC_ID column, estimate how many photons of each
source are detected in which region. How high is the degree of contamination per
region?

## Add another source

For example, split one of the hemispheres into two different quarter circles,
or add a point source in the center.
ARF generation and analysis would need to be adjusted accordingly.

## Try different spectral models

For example, two APECs, black bodies, ...
Or maybe two different spectral models altogether!
In either case, you would also need to adjust the models used in the analysis
scripts.

Note that as long as the spatial distribution of the models (i.e., the images)
and the regions stay the same, you do not need to re-generate the ARFs!
