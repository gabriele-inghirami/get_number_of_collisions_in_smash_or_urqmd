#!/usr/bin/python3

# it converts into text format the output of get_urmqd_avg_reduction_factor.py
# and combine_avg_red_factor.py

import math
import numpy as np
import os
import pickle
import sys

# if > 0 it prints messages about the advancement status of the program
verbose = 1

# format for quantities in output file
tf='{:7.3f}'
ff='{:14.10e}'
sp="    "

if (len(sys.argv)<3):
    print ('Syntax: ./print_reduction_factor_txt.py <pickled data> <output file>')
    sys.exit(1)

infile=sys.argv[1]
outfile=sys.argv[2]

if (not os.path.isfile(infile)):
    print("Error, input data file "+infile+" does not exist.")
    sys.exit(1)
if os.path.exists(outfile):
    print("Output file "+outfile+" already exists, I will not overwrite it. I stop here.")
    sys.exit(1)

with open(infile,"rb") as inputfile:
    data = pickle.load(inputfile)

times,cross_section_reduction_factor_array,hadrons_array,events = data[:]

nt = len(times)

# now we print the results
tf = '{:3.1f}'
ff = '{:12.7f}'
if verbose > 0:
    print("Writing the results in "+outfile)
with open(outfile,"w") as outf:
    outf.write("# total number of events: "+str(events)+"\n")
    outf.write("# time [fm]    average reduction factor\n")
    for h in range(nt):
        if hadrons_array[h] > 0:
            outf.write(tf.format(times[h])+"  "+ff.format(cross_section_reduction_factor_array[h]/hadrons_array[h])+"\n")
