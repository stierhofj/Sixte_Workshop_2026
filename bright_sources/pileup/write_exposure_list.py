import sys
from os import environ

outdir = environ["OUTDIR"]

if __name__ == "__main__":
    calib_counts = float(sys.argv[1])
    calib_exposure = float(sys.argv[2])
    flux = float(sys.argv[3])
    calib_flux = float(sys.argv[4])

    calib_count_rate = calib_counts/calib_exposure
    count_rate_estimate = (calib_count_rate * flux)/calib_flux

    # target 5000 counts
    exposure_estimate = 5000./count_rate_estimate

    with open(outdir + "/exposure_list.dat", "a") as f:
        f.write(f"{exposure_estimate},{count_rate_estimate},{flux:.0e}\n")
