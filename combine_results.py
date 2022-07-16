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
   print('Syntax: ./combine_results.py <outputfile> <inputfile 1> <inputfile 2> ... [inputfile n]')
   print("(The minimum number of input files is 2)")
   sys.exit(1)

outputfile=sys.argv[1]
if verbose > 0:
    print("Outputfile will be: "+outputfile)

with open(sys.argv[2],"rb") as infile:
    if verbose > 0:
        print("Opening: "+sys.argv[2])
    data = pickle.load(infile)

label_header,file_kind,events,dt,times,elastic,decays,strings,other,detailed,two_stable,one_stable,no_stable,\
        min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar = data[:]
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
    label_header_new,file_kind_new,events_new,dt_new,times_new,elastic_new,decays_new,strings_new,other_new,\
    detailed_new,two_stable_new,one_stable_new,no_stable_new,min_one_anti_new,BaBa_new,MeBa_new,MeMe_new,\
    NuNu_new,Nupi_new,pipi_new,NuNustar_new = data[:]
    data = None
    if ((label_header_new != label_header) or (file_kind_new != file_kind) or (dt_new != dt) or\
        (times_new.all() != times.all())):
        print("Warning, I skip input file "+sys.argv[fi])
        print("because it does not match the fundamental characteristics of the first file")
        continue
    events += events_new
    elastic += elastic_new
    decays += decays_new
    strings += strings_new
    other += other_new
    detailed += detailed_new
    two_stable += two_stable_new
    one_stable += one_stable_new
    no_stable += no_stable_new
    min_one_anti += min_one_anti_new
    BaBa += BaBa_new
    MeBa += MeBa_new
    MeMe += MeMe_new
    NuNu += NuNu_new
    Nupi += Nupi_new
    pipi += pipi_new
    NuNustar += NuNustar_new

if verbose > 0:
    print("Writing the results in "+outputfile)
    print("Warning, you are advised to take note of the commit number of the repository that you used to produce these results.")
with open(outputfile,"wb") as outf:
    pickle.dump((label_header,file_kind,events,dt,times,elastic,decays,strings,other,detailed,two_stable,one_stable,no_stable,\
                 min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar),outf)


