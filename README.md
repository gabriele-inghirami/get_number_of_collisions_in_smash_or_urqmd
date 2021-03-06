## Purpose:

This progam reads the hadron data in the SMASH or UrQMD collision files, extracts
the time and the type of collisions and saves a histogram on a file.
The program automatically detects if the file is a .f15 UrQMD or
an oscar2013 SMASH collision file.

## Syntax:

`python3 get_number_of_collisions.py <output file name> <output file header info> <collision file 1> [collision file 2] ...`

Example: `python3 get_number_of_collisions.py smash_200.dat "Au+Au, 200 GeV, b=0-3.3 fm" out1/full_event_history.oscar out2/full_event_history.oscar`

The script automatically recognizes if the collision files have been generated by UrQMD or SMASH.
A short description of the content of the output file is provided in its header.

### Combining the results
It is possible to combine the results of two or more results file created by get_number_of_collisions.py with:

`python3 ./combine_results.py <outputfile> <inputfile 1> <inputfile 2> ... [inputfile n]`

## Plots

The gnuplot script (tested with Gnuplot 5.4) make_plots.gp is an example of plotting script.

## Config files and slurm scripts

The directory *slurm_scripts_and_configs* contains example confiuration files and slurm scripts (used on the Virgo cluster at GSI).
