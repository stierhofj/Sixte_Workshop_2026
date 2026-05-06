require("isisscripts");
xspec_abund("angr");

variable det = "resolve";
%variable det = "xifu";

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This ISIS script performs a combined fit of the two sources, using the
% extracted ARFs.
% Check the documentation of the "combine_datasets" function to see how this
% works deep down.
%
% Do the resulting power law spectral indices now match the input values?
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


variable phafile_east = "output/mixing_east.pha";
variable phafile_west = "output/mixing_west.pha";


% need to get the RMF for the next step
variable rmf = fits_read_header(phafile_east).RESPFILE;


% load in all the datasets, with the correct ARFs
% first two datasets are the ones "in region"
variable soft_in_east = 1;
load_dataset(phafile_east, rmf, "./output/mixing_soft_in_east.arf");

variable hard_in_west = 2;
load_dataset(phafile_west, rmf, "./output/mixing_hard_in_west.arf");

% the next are the "contamination"
variable hard_in_east = 3;
load_dataset(phafile_east, rmf, "./output/mixing_hard_in_east.arf");

variable soft_in_west = 4;
load_dataset(phafile_west, rmf, "./output/mixing_soft_in_west.arf");


% combine the datasets
variable weights = [0.5,0.5];


() = combine_datasets(soft_in_east, hard_in_east, weights);
() = combine_datasets(hard_in_west, soft_in_west, weights);

% rebin
group([soft_in_east, hard_in_east]; min_sn=100);
group([hard_in_west, soft_in_west]; min_sn=100);

% set up the combined model
% for our models, we assume the same N_H, but different powerlaws
define model_soft() {
    return phabs(1) * powerlaw(1);
}

define model_hard() {
    return phabs(1) * powerlaw(2);
}

define coupled_model() {
    switch (Isis_Active_Dataset)
    {case soft_in_east or case soft_in_west: return model_soft(); }
    {case hard_in_west or case hard_in_east: return model_hard(); }
}

set_eval_grid_method(SEPARATE_GRID, [1:4]);

fit_fun("coupled_model()");


% final prep, depends on instrument
if (det == "resolve") {
    % gate valve
    ignore_en([1:4], 0, 1);
    freeze("phabs(1).nH");

    % no flux
    ignore_en([1:4], 15,100);

    % could initialize the fit from the naive ones - but that's not needed!
    %set_par("powerlaw(1).PhoIndex", 2.3);
    %set_par("powerlaw(2).PhoIndex", 1.7);
}

if (det == "xifu") {
    % could initialize the fit from the naive ones - but that's not needed!
    % (especially here)
    %set_par("powerlaw(1).PhoIndex", 2.5);
    %set_par("powerlaw(2).PhoIndex", 1.5);

}


% go!
vmessage("Performing fit!");
fit_counts;
list_free;
