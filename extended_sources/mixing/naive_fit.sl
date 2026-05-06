require("isisscripts");
xspec_abund("angr");

%variable det = "xifu";
variable det = "resolve";

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This ISIS script performs a naive fit of one of the regions, assuming
% point-source responses.
% Does the resulting power law spectral index match the input values?
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

variable phafile_east = "output/mixing_east.pha";
variable phafile_west = "output/mixing_west.pha";

load_data(phafile_east);
%load_data(phafile_west);

group(1; min_sn=10);

fit_fun("phabs*powerlaw");

if (det == "resolve") {
    % gate valve
    ignore_en(1, 0, 1);
    freeze("phabs(1).nH");

    % no flux
    ignore_en(1, 15,100);
}

fit_counts;

list_free;
