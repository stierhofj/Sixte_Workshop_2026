# Deep field simulation with Athena WFI

This example shows how to simulate the Chandra Deep Field South (CDFS) with
the Athena WFI.

The setup is based on the CDFS deep-field simulation from Sect. 10.4 of the
SIXTE manual. It uses two prebuilt SIMPUT catalogs from the SIXTE web page:
one catalog for point sources based on Lehmer et al. (2005), and one catalog
for galaxy clusters based on Finoguenov et al. (2015).

The first simulation observes the CDFS for 5 ks with a fixed pointing. This
shows the four WFI chips and the gaps between them. The second simulation uses
a Lissajous dithering pattern and creates an exposure map before running the
same field again with the time-dependent attitude.

Run `./prepare` once before the numbered steps. It downloads and extracts the
CDFS SIMPUT catalogs into the `input` directory.

Afterwards, execute the numbered steps in order:

- `01_run_sim` simulates the fixed-pointing WFI observation and merges the chip
  event files.
- `02_extract_img` creates a sky image from the fixed-pointing event file.
- `03_create_dither` creates a Lissajous attitude file and an exposure map.
- `04_run_dithered_sim` simulates the dithered WFI observation and merges the
  chip event files.
- `05_extract_dithered_img` creates a sky image from the dithered event file.

To inspect the commands without executing them, use `./run`. To inspect one
step only, pass the step number, e.g. `./run 03`.
