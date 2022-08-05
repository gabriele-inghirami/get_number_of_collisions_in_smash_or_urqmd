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

if len(data) == 31:

    header,dt,times,elastic,decays,strings,other,two_stable,one_stable,no_stable,\
        min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar,created_hadrons,\
        tot_cross_sections_elastic,tot_cross_sections_decays,tot_cross_sections_strings,tot_cross_sections_other,\
        par_cross_sections_elastic,par_cross_sections_decays,par_cross_sections_strings,par_cross_sections_other,\
        coll_energy_elastic,coll_energy_decays,coll_energy_strings,coll_energy_other\
        = data[:]
    diff_ratio_kind = True
    den=1
else:
    header,file_kind,events,dt,times,elastic,decays,strings,other,detailed,two_stable,one_stable,no_stable,\
        min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar,created_hadrons,cross_sections\
        = data[:]
    diff_ratio_kind = False
    den=dt*events
    
nt = len(times)

# now we print the results
os.mkdir(outdir) # in the case of already existing directory, we would have stopped at the beginning
collision_type_outfile=outdir+"/collision_types.dat"
if verbose > 0:
    print("Writing the results of collision types in the file "+collision_type_outfile)
outf = open(collision_type_outfile,"w")
if diff_ratio_kind:
    outf.write(header)
    outf.write("# SMASH: elastic: 1  *  decays: 5  *  strings: >=41,<=46\n")
    outf.write("# UrQMD elastic: 13,17,19,22,26,38  *  decays: 20  *  strings: 15,23,24,27,28\n")
    outf.write("# columns: 1 time [fm]     2 dN/dt elastic     3 dN/dt decays     4 dN/dt strings     6 dN/dt other\n")
else:
    outf.write("# "+header+"\n")
    outf.write("# Data from "+file_kind+" simulations\n")
    outf.write("# Number of events: "+str(events)+"\n")
    outf.write("# Process types considered: \n")
    if file_kind == "smash":
        outf.write("# elastic: 1  *  decays: 5  *  strings: >=41,<=46\n")
    elif file_kind == "urqmd":
        outf.write("# elastic: 13,17,19,22,26,38  *  decays: 20  *  strings: 15,23,24,27,28\n")

for h in range(nt):
    outf.write(tf.format(times[h])+sp+ff.format(elastic[h]/den)+sp+ff.format(decays[h]/den)+sp+ff.format(strings[h]/den)+sp+ff.format(other[h]/den)+"\n")
outf.close()

if (not diff_ratio_kind):
    process_type_outfile=outdir+"/process_types.dat"
    if verbose > 0:
        print("Writing the results of process types in the file "+process_type_outfile)
    outf = open(process_type_outfile,"w")
    outf.write("# "+header+"\n")
    outf.write("# Data from "+file_kind+" simulations\n")
    outf.write("# Number of events: "+str(events)+"\n")
    outf.write("# Columns:\n# 1 time [fm]\n")
    if file_kind == "smash":
        for v in ptype_smash.values():
            outf.write("# "+'{:2d}'.format(v[0])+" dN/dt"+v[1]+"\n")
    elif file_kind == "urqmd":
        for v in ptype_urqmd.values():
            outf.write("# "+'{:2d}'.format(v[0])+" dN/dt"+v[1]+"\n")
    for h in range(nt):
        outf.write(tf.format(times[h]))
        if file_kind == "smash":
            for v in ptype_smash.values():
                outf.write(sp+ff.format(detailed[h,v[0]]/den))
        else:
            for v in ptype_urqmd.values():
                outf.write(sp+ff.format(detailed[h,v[0]]/den))
        outf.write("\n")
    outf.close()


hadron_type_outfile=outdir+"/hadron_types.dat"
if verbose > 0:
    print("Writing the results of hadron types in the file "+hadron_type_outfile)
outf = open(hadron_type_outfile,"w")
if diff_ratio_kind:
    outf.write(header)
else:
    outf.write("# "+header+"\n")
    outf.write("# Data from "+file_kind+" simulations\n")
    outf.write("# Number of events: "+str(events)+"\n")

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
    outf.write(sp+ff.format(two_stable[h]/den))
    outf.write(sp+ff.format(one_stable[h]/den))
    outf.write(sp+ff.format(no_stable[h]/den))
    outf.write(sp+ff.format(min_one_anti[h]/den))
    outf.write(sp+ff.format(BaBa[h]/den))
    outf.write(sp+ff.format(MeBa[h]/den))
    outf.write(sp+ff.format(MeMe[h]/den))
    outf.write(sp+ff.format(NuNu[h]/den))
    outf.write(sp+ff.format(Nupi[h]/den))
    outf.write(sp+ff.format(pipi[h]/den))
    outf.write(sp+ff.format(NuNustar[h]/den))
    outf.write("\n")
outf.close()

if diff_ratio_kind:
    den_elastic = np.ones_like(elastic)
    den_decays = np.ones_like(decays)
    den_strings = np.ones_like(strings)
    den_other = np.ones_like(other)
else:
    den_elastic = elastic
    den_decays = decays
    den_strings = strings
    den_other = other
    den_elastic[abs(den_elastic) < 1e-14] = 1.
    den_decays[abs(den_decays) < 1e-14] = 1.
    den_strings[abs(den_strings) < 1e-14] = 1.
    den_other[abs(den_other) < 1e-14] = 1.

created_hadrons_outfile=outdir+"/average_created_hadrons.dat"
if verbose > 0:
    print("Writing the results of average created hadrons in the system in the file "+created_hadrons_outfile)
outf = open(created_hadrons_outfile,"w")
if diff_ratio_kind:
    outf.write(header)
else:
    outf.write("# "+header+"\n")
outf.write("# Columns:\n# 1 time [fm]\n")
outf.write("# 2 average created number of hadrons in the system in the time interval t-dt/2, t+dt/2\n")
for h in range(nt):
    outf.write(tf.format(times[h]))
    outf.write(sp+ff.format(created_hadrons[h])/events)
    outf.write("\n")
outf.close()

# indexes for the cross section array
# event type indexes
k_ela=0 # elastic
k_dec=2 # decays
k_str=2 # strings
k_oth=3 # other
# quantity indexes
k_tot=0 # total cross section
k_par=1 # partial cross section
k_cen=2 # collision energy

tot_cross_sections_elastic = cross_sections[:,k_ela,k_tot]
tot_cross_sections_decays = cross_sections[:,k_dec,k_tot]
tot_cross_sections_strings = cross_sections[:,k_str,k_tot]
tot_cross_sections_other = cross_sections[:,k_oth,k_tot]
par_cross_sections_elastic = cross_sections[:,k_ela,k_par]
par_cross_sections_decays = cross_sections[:,k_dec,k_partot]
par_cross_sections_strings = cross_sections[:,k_str,k_partot]
par_cross_sections_other = cross_sections[:,k_oth,k_partot]
coll_energy_elastic = cross_sections[:,k_ela,k_cen]
coll_energy_decays = cross_sections[:,k_dec,k_cen]
coll_energy_strings = cross_sections[:,k_str,k_cen]
coll_energy_other = cross_sections[:,k_oth,k_cen]

collision_energies_outfile=outdir+"/average_collision_energies.dat"
if verbose > 0:
    print("Writing the results of average collision energies in the file "+collision_energies_outfile)
outf = open(collision_energies_outfile,"w")
if diff_ratio_kind:
    outf.write(header)
else:
    outf.write("# "+header+"\n")
outf.write("# Columns:\n# 1 time [fm]\n")
outf.write("# 2 average collision energy for elastic interactions\n")
outf.write("# 3 average collision energy for decays interactions\n")
outf.write("# 4 average collision energy for strings interactions\n")
outf.write("# 5 average collision energy for other interactions\n")
for h in range(nt):
    outf.write(tf.format(times[h]))
    outf.write(sp+ff.format(coll_energy_elastic[h]/den_elastic[h]))
    outf.write(sp+ff.format(coll_energy_decays[h])/den_decays[h])
    outf.write(sp+ff.format(coll_energy_strings[h])/den_strings[h])
    outf.write(sp+ff.format(coll_energy_other[h]/den_other[h]))
    outf.write("\n")
outf.close()

cross_sections_outfile=outdir+"/cross_sections.dat"
if verbose > 0:
    print("Writing the results of average cross sections in the file "+cross_sections_outfile)
outf = open(cross_sections_outfile,"w")
if diff_ratio_kind:
    outf.write(header)
else:
    outf.write("# "+header+"\n")
outf.write("# Columns:\n# 1 time [fm]\n")
outf.write("# 2 average total cross section for elastic interactions\n")
outf.write("# 3 average total cross section for decays interactions\n")
outf.write("# 4 average total cross section for strings interactions\n")
outf.write("# 5 average total cross section for other interactions\n")
outf.write("# 6 average partial cross section for elastic interactions\n")
outf.write("# 7 average partial cross section for decays interactions\n")
outf.write("# 8 average partial cross section for strings interactions\n")
outf.write("# 9 average partial cross section for other interactions\n")
for h in range(nt):
    outf.write(tf.format(times[h]))
    outf.write(sp+ff.format(tot_cross_sections_elastic[h]/den_elastic[h]))
    outf.write(sp+ff.format(tot_cross_sections_decays[h])/den_decays[h])
    outf.write(sp+ff.format(tot_cross_sections_strings[h])/den_strings[h])
    outf.write(sp+ff.format(tot_cross_sections_other[h])/den_other[h])
    outf.write(sp+ff.format(par_cross_sections_elastic[h])/den_elastic[h])
    outf.write(sp+ff.format(par_cross_sections_decays[h])/den_decays[h])
    outf.write(sp+ff.format(par_cross_sections_strings[h])/den_strings[h])
    outf.write(sp+ff.format(par_cross_sections_other[h])/den_other[h])
    outf.write("\n")
outf.close()
