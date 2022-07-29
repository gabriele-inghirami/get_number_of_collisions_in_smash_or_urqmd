#!/usr/bin/python3

# it reads the hadron data in the smash collision files, extracts
# the time and the type of collisions and saves the results as .pickle darchive 
# the program automatically detects if the file is
# a .f15 urqmd or oscar2013 smash collision file

import math
import numpy as np
import os
import pickle
import sys
from definition import *

# if > 0 it prints messages about the advancement status of the program
verbose = 1

# format for quantities in output file
tf='{:7.3f}'
ff='{:14.10e}'
sp="    "

if (len(sys.argv)<3):
    print ('Syntax: ./print_txt.py <pickled data> <output directory>')
    sys.exit(1)

infile=sys.argv[1]
outdir=sys.argv[2]

if (not os.path.isfile(infile)):
    print("Error, input data file "+infile+" does not exist.")
    sys.exit(1)
if os.path.exists(outdir):
    print("Output directory "+outdir+" already exists, I will not overwrite it. I stop here.")
    sys.exit(1)

with open(infile,"rb") as inputfile:
    data = pickle.load(inputfile)


header,dt,times,elastic,decays,strings,other,two_stable,one_stable,no_stable,\
        min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar = data[:]
    
nt = len(times)

# now we print the results
os.mkdir(outdir) # in the case of already existing directory, we would have stopped at the beginning
collision_type_outfile=outdir+"/collision_types.dat"
if verbose > 0:
    print("Writing the results of collision types in the file "+collision_type_outfile)
outf = open(collision_type_outfile,"w")
outf.write(header)
outf.write("# SMASH: elastic: 1  *  decays: 5  *  strings: >=41,<=46\n")
outf.write("# UrQMD elastic: 13,17,19,22,26,38  *  decays: 20  *  strings: 15,23,24,27,28\n")
outf.write("# columns: 1 time [fm]     2 dN/dt elastic     3 dN/dt decays     4 dN/dt strings     6 dN/dt other\n")
for h in range(nt):
    outf.write(tf.format(times[h])+sp+ff.format(elastic[h])+sp+ff.format(decays[h])+sp+ff.format(strings[h])+sp+ff.format(other[h])+"\n")
outf.close()

hadron_type_outfile=outdir+"/hadron_types.dat"
if verbose > 0:
    print("Writing the results of hadron types in the file "+hadron_type_outfile)
outf = open(hadron_type_outfile,"w")
outf.write(header)
outf.write("# Columns:\n# 1 time [fm]\n")
outf.write("# 2 dN/dt (Mininum) 2 stable particles\n")
outf.write("# 3 dN/dt (Mininum) 1 stable particle\n")
outf.write("# 4 dN/dt No stable particles\n")
outf.write("# 5 dN/dt (Minimum) 1 antiparticle\n")
outf.write("# 6 dN/dt (Minimum) 2 baryons\n")
outf.write("# 7 dN/dt (Minimum) 1 baryon and 1 meson\n")
outf.write("# 8 dN/dt (Minimum) 2 mesons\n")
outf.write("# 9 dN/dt (Minimum) 2 nucleons\n")
outf.write("# 10 dN/dt (Minimum) 1 nucleon and 1 pion\n")
outf.write("# 11 dN/dt (Minimum) 2 pions\n")
outf.write("# 12 dN/dt (Minimum) 1 nucleon and 1 excited nucleon\n")

outf.write("# Note: pion- are considered antiparticles.\n")
outf.write("# Note: Stable particles are: p, n, K, eta, eta', omega, phi, Lambda, Xi, Omega and their antiparticles.\n")
for h in range(nt):
    outf.write(tf.format(times[h]))
    outf.write(sp+ff.format(two_stable[h]))
    outf.write(sp+ff.format(one_stable[h]))
    outf.write(sp+ff.format(no_stable[h]))
    outf.write(sp+ff.format(min_one_anti[h]))
    outf.write(sp+ff.format(BaBa[h]))
    outf.write(sp+ff.format(MeBa[h]))
    outf.write(sp+ff.format(MeMe[h]))
    outf.write(sp+ff.format(NuNu[h]))
    outf.write(sp+ff.format(Nupi[h]))
    outf.write(sp+ff.format(pipi[h]))
    outf.write(sp+ff.format(NuNustar[h]))
    outf.write("\n")
outf.close()
