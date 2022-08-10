#!/usr/bin/python3

import fileinput
import math
import numpy as np
import pickle
import sys
import os

sp="    "

# if 0: only error messages, if > 0: progress messages
verbose=1

N_args=len(sys.argv)
N_input_files=N_args-2

if(N_input_files<2):
   print('Syntax: ./combine_avg_red_factor.py <outputfile> <inputfile 1> <inputfile 2> ... [inputfile n]')
   print("(The minimum number of input files is 2)")
   sys.exit(1)

outputfile=sys.argv[1]
if verbose > 0:
    print("Outputfile will be: "+outputfile)

with open(sys.argv[2],"rb") as infile:
    if verbose > 0:
        print("Opening: "+sys.argv[2])
    data = pickle.load(infile)

times,cross_section_reduction_factor_array,hadrons_array,events = data[:]
data=None

for fi in range(3,N_args):
    if verbose > 0:
        print("Opening: "+sys.argv[fi])
    try:
        with open(sys.argv[fi],"rb") as infile:
            data = pickle.load(infile)
    except:
        print("Error in reading "+sys.argv[fi])
        continue
    times_new,cross_section_reduction_factor_array_new,hadrons_array_new,events_new = data[:]
    data = None
    if (times_new.all() != times.all()):
        print("Warning, I skip input file "+sys.argv[fi])
        print("because it has different time intervals")
        continue
    events += events_new
    cross_section_reduction_factor_array += cross_section_reduction_factor_array_new
    hadrons_array += hadrons_array_new

if verbose > 0:
    print("Writing the results in "+outputfile)
    print("Warning, you are advised to take note of the commit number of the repository that you used to produce these results.")
with open(outputfile,"wb") as outf:
    pickle.dump((times,cross_section_reduction_factor_array,hadrons_array,events),outf)
