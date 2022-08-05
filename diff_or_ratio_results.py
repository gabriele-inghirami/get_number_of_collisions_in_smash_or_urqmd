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

# we choose the operation, that can be either difference or ratio between two sets of data
operation="ratio"
#operation="difference"

# indexes for the cross section array
# the approach (1 multidimensionl array) is different from the
# separated arrays for the number of collisions, but it has been
# planned and implemented later
# event type indexes
k_ela=0 # elastic
k_dec=2 # decays
k_str=2 # strings
k_oth=3 # other
# quantity indexes
k_tot=0 # total cross section
k_par=1 # partial cross section
k_cen=2 # collision energy

# we check that the operation has been chosen correctly
if ((operation != "ratio") and (operation != "difference")):
    print("Hardcoded option operation can be only either 'ratio' or 'difference'.")
    print("Please, check the script.")
    sys.exit(1)

N_args=len(sys.argv)

if(N_args!=4):
   print('Syntax: ./diff_or_ratio_results.py <outputfile> <inputfile 1> <inputfile 2>')
   sys.exit(1)

outputfile=sys.argv[1]
if verbose > 0:
    print("Outputfile will be: "+outputfile)

with open(sys.argv[2],"rb") as infile:
    if verbose > 0:
        print("Opening: "+sys.argv[2])
    data = pickle.load(infile)

header1,file_kind1,events1,dt1,times1,elastic1,decays1,strings1,other1,detailed1,two_stable1,one_stable1,no_stable1,\
        min_one_anti1,BaBa1,MeBa1,MeMe1,NuNu1,Nupi1,pipi1,NuNustar1,total_hadrons1,cross_sections1 = data[:]
data=None
den1=events1*dt1

with open(sys.argv[3],"rb") as infile:
    if verbose > 0:
        print("Opening: "+sys.argv[3])
    data = pickle.load(infile)

header2,file_kind2,events2,dt2,times2,elastic2,decays2,strings2,other2,\
detailed2,two_stable2,one_stable2,no_stable2,min_one_anti2,BaBa2,MeBa2,MeMe2,\
NuNu2,Nupi2,pipi2,NuNustar2,total_hadrons2,cross_sections2 = data[:]
data = None
den2=events2*dt2

#the two files might have different times arrays, so we build new arrays
if dt1 != dt2:
    print("Sorry, but the time interval in the two files must be the same")
    print("Here I have: "+sys.argv[2]+": "+str(dt1)+", "+sys.argv[3]+": "+str(dt2))
    sys.exit(1)

# we consider only the times covered in both files
dt=dt1 # we already checked that it is equal to dt2
tstart=max(times1[0],times2[0])
#print(str(tstart))
tend=min(times1[-1],times2[-1])
#print(str(tend))
nt=int((tend-tstart)/dt)+1
times=np.linspace(tstart,tend,num=nt)
i1s=np.argmin(abs(times1-tstart))
#print(str(i1s))
i2s=np.argmin(abs(times2-tstart))
#print(str(i2s))
i1e=np.argmin(abs(times1-tend))+1
#print(str(i1e))
i2e=np.argmin(abs(times2-tend))+1
#print(str(i2e))

nt_fin = i2e - i1e
total_hadrons = np.zeros(nt_fin,dtype=np.float64)
tot_cross_sections_elastic = np.zeros(nt_fin,dtype=np.float64)
tot_cross_sections_decays = np.zeros(nt_fin,dtype=np.float64)
tot_cross_sections_strings = np.zeros(nt_fin,dtype=np.float64)
tot_cross_sections_other = np.zeros(nt_fin,dtype=np.float64)
par_cross_sections_elastic = np.zeros(nt_fin,dtype=np.float64)
par_cross_sections_decays = np.zeros(nt_fin,dtype=np.float64)
par_cross_sections_strings = np.zeros(nt_fin,dtype=np.float64)
par_cross_sections_other = np.zeros(nt_fin,dtype=np.float64)
coll_energy_elastic = np.zeros(nt_fin,dtype=np.float64)
coll_energy_decays = np.zeros(nt_fin,dtype=np.float64)
coll_energy_strings = np.zeros(nt_fin,dtype=np.float64)
coll_energy_other = np.zeros(nt_fin,dtype=np.float64)

if (operation == "difference"):
   header="# Difference between "+header1+" and " +header2+"\n"
else:
   header="# Ratio between "+header1+" and " +header2+"\n"
header+="# stored in files "+sys.argv[1]+" and "+sys.argv[2]+"\n"

# if the counting at the denominator is 0 also the numerator should be 0, so it safe to set it to 1
for i in range(nt_new):
    i1 = i + i1s
    i2 = i + i2s
    if elastic1[i1] == 0:
        elastic1[i1] = 1
    if decays1[i1] == 0:
        decays1[i1] = 1
    if strings1[i1] == 0:
        strings1[i1] = 1
    if other1[i1] == 0:
        other1[i1] = 1
    if elastic2[i2] == 0:
        elastic2[i2] = 1
    if decays2[i2] == 0:
        decays2[i2] = 1
    if strings2[i2] == 0:
        strings2[i2] = 1
    if other2[i2] == 0:
        other2[i2] = 1

tot_cross_sections_elastic1 = cross_sections1[i1s:i1e,k_ela,k_tot]/elastic1[i1s:i1e]
tot_cross_sections_elastic2 = cross_sections2[i2s:i2e,k_ela,k_tot]/elastic2[i2s:i2e]
tot_cross_sections_decays1 = cross_sections1[i1s:i1e,k_dec,k_tot]/decays1[i1s:i1e]
tot_cross_sections_decays2 = cross_sections2[i2s:i2e,k_dec,k_tot]/decays2[i2s:i2e]
tot_cross_sections_strings1 = cross_sections1[i1s:i1e,k_str,k_tot]/strings1[i1s:i1e]
tot_cross_sections_strings2 = cross_sections2[i2s:i2e,k_str,k_tot]/stringss2[i2s:i2e]
tot_cross_sections_other1 = cross_sections1[i1s:i1e,k_oth,k_tot]/other1[i1s:i1e]
tot_cross_sections_other2 = cross_sections2[i2s:i2e,k_oth,k_tot]/other2[i2s:i2e]
par_cross_sections_elastic1 = cross_sections1[i1s:i1e,k_ela,k_par]/elastic1[i1s:i1e]
par_cross_sections_elastic2 = cross_sections2[i2s:i2e,k_ela,k_par]/elastic2[i2s:i2e]
par_cross_sections_decays1 = cross_sections1[i1s:i1e,k_dec,k_par]/decays1[i1s:i1e]
par_cross_sections_decays2 = cross_sections2[i2s:i2e,k_dec,k_par]/decays2[i2s:i2e]
par_cross_sections_strings1 = cross_sections1[i1s:i1e,k_str,k_par]/strings1[i1s:i1e]
par_cross_sections_strings2 = cross_sections2[i2s:i2e,k_str,k_par]/stringss2[i2s:i2e]
par_cross_sections_other1 = cross_sections1[i1s:i1e,k_oth,k_par]/other1[i1s:i1e]
par_cross_sections_other2 = cross_sections2[i2s:i2e,k_oth,k_par]/other2[i2s:i2e]
coll_energy_elastic1 = cross_sections1[i1s:i1e,k_ela,k_cen]/elastic1[i1s:i1e]
coll_energy_elastic2 = cross_sections2[i2s:i2e,k_ela,k_cen]/elastic2[i2s:i2e]
coll_energy_decays1 = cross_sections1[i1s:i1e,k_dec,k_cen]/decays1[i1s:i1e]
coll_energy_decays2 = cross_sections2[i2s:i2e,k_dec,k_cen]/decays2[i2s:i2e]
coll_energy_strings1 = cross_sections1[i1s:i1e,k_str,k_cen]/strings1[i1s:i1e]
coll_energy_strings2 = cross_sections2[i2s:i2e,k_str,k_cen]/stringss2[i2s:i2e]
coll_energy_other1 = cross_sections1[i1s:i1e,k_oth,k_cen]/other1[i1s:i1e]
coll_energy_other2 = cross_sections2[i2s:i2e,k_oth,k_cen]/other2[i2s:i2e]
    
if (operation == "difference"):
    elastic = elastic1[i1s:i1e]/den1 - elastic2[i2s:i2e]/den2
    decays = decays1[i1s:i1e]/den1 - decays2[i2s:i2e]/den2
    strings = strings1[i1s:i1e]/den1 - strings2[i2s:i2e]/den2
    other = other1[i1s:i1e]/den1 - other2[i2s:i2e]/den2
    two_stable = two_stable1[i1s:i1e]/den1 - two_stable2[i2s:i2e]/den2
    one_stable = one_stable1[i1s:i1e]/den1 - one_stable2[i2s:i2e]/den2
    no_stable = no_stable1[i1s:i1e]/den1 - no_stable2[i2s:i2e]/den2
    min_one_anti = min_one_anti1[i1s:i1e]/den1 - min_one_anti2[i2s:i2e]/den2
    BaBa = BaBa1[i1s:i1e]/den1 - BaBa2[i2s:i2e]/den2
    MeBa = MeBa1[i1s:i1e]/den1 - MeBa2[i2s:i2e]/den2
    MeMe = MeMe1[i1s:i1e]/den1 - MeMe2[i2s:i2e]/den2
    NuNu = NuNu1[i1s:i1e]/den1 - NuNu2[i2s:i2e]/den2
    Nupi = Nupi1[i1s:i1e]/den1 - Nupi2[i2s:i2e]/den2
    pipi = pipi1[i1s:i1e]/den1 - pipi2[i2s:i2e]/den2
    NuNustar = NuNustar1[i1s:i1e]/den1 - NuNustar2[i2s:i2e]/den2
    
    total_hadrons = total_hadrons1[i1s:i1e]/events1 - total_hadrons2[i2s:i2e]/events2

    tot_cross_sections_elastic = tot_cross_sections_elastic1 - tot_cross_sections_elastic2
    tot_cross_sections_decays = tot_cross_sections_decays1 - tot_cross_sections_decays2
    tot_cross_sections_strings = tot_cross_sections_strings1 - tot_cross_sections_strings2
    tot_cross_sections_other = tot_cross_sections_other1 - tot_cross_sections_other2
    par_cross_sections_elastic = par_cross_sections_elastic1 - par_cross_sections_elastic2
    par_cross_sections_decay = par_cross_sections_decay1 - par_cross_sections_decay2
    par_cross_sections_strings = par_cross_sections_strings1 - par_cross_sections_strings2
    par_cross_sections_other = par_cross_sections_other1 - par_cross_sections_other2
    coll_energy_elastic = coll_energy_elastic1 - coll_energy_elastic2
    coll_energy_decay = coll_energy_decay1 - coll_energy_decay2
    coll_energy_strings = coll_energy_strings1 - coll_energy_strings2
    coll_energy_other = coll_energy_other1 - coll_energy_other2
else:
    elastic = (elastic1[i1s:i1e]/den1) / (elastic2[i2s:i2e]/den2)
    decays = (decays1[i1s:i1e]/den1) / (decays2[i2s:i2e]/den2)
    strings = (strings1[i1s:i1e]/den1) / (strings2[i2s:i2e]/den2)
    other = (other1[i1s:i1e]/den1) / (other2[i2s:i2e]/den2)
    two_stable = (two_stable1[i1s:i1e]/den1) / (two_stable2[i2s:i2e]/den2)
    one_stable = (one_stable1[i1s:i1e]/den1) / (one_stable2[i2s:i2e]/den2)
    no_stable = (no_stable1[i1s:i1e]/den1) / (no_stable2[i2s:i2e]/den2)
    min_one_anti = (min_one_anti1[i1s:i1e]/den1) / (min_one_anti2[i2s:i2e]/den2)
    BaBa = (BaBa1[i1s:i1e]/den1) / (BaBa2[i2s:i2e]/den2)
    MeBa = (MeBa1[i1s:i1e]/den1) / (MeBa2[i2s:i2e]/den2)
    MeMe = (MeMe1[i1s:i1e]/den1) / (MeMe2[i2s:i2e]/den2)
    NuNu = (NuNu1[i1s:i1e]/den1) / (NuNu2[i2s:i2e]/den2)
    Nupi = (Nupi1[i1s:i1e]/den1) / (Nupi2[i2s:i2e]/den2)
    pipi = (pipi1[i1s:i1e]/den1) / (pipi2[i2s:i2e]/den2)
    NuNustar = (NuNustar1[i1s:i1e]/den1) / (NuNustar2[i2s:i2e]/den2)
    elastic[abs(elastic) == np.inf] = 0 
    decays[abs(decays) == np.inf] = 0
    strings[abs(strings) == np.inf] = 0
    other[abs(other) == np.inf] = 0
    two_stable[abs(two_stable) == np.inf] = 0
    one_stable[abs(one_stable) == np.inf] = 0
    no_stable[abs(no_stable) == np.inf] = 0
    min_one_anti[abs(min_one_anti) == np.inf] = 0
    BaBa[abs(BaBa) == np.inf] = 0
    MeBa[abs(MeBa) == np.inf] = 0
    MeMe[abs(MeMe) == np.inf] = 0
    NuNu[abs(NuNu) == np.inf] = 0
    Nupi[abs(Nupi) == np.inf] = 0
    pipi[abs(pipi) == np.inf] = 0
    NuNustar[abs(NuNustar) == np.inf] = 0

    total_hadrons = (total_hadrons1[i1s:i1e]/events1) / (total_hadrons2[i2s:i2e]/events2)

    tot_cross_sections_elastic = tot_cross_sections_elastic1 / tot_cross_sections_elastic2
    tot_cross_sections_decays = tot_cross_sections_decays1 / tot_cross_sections_decays2
    tot_cross_sections_strings = tot_cross_sections_strings1 / tot_cross_sections_strings2
    tot_cross_sections_other = tot_cross_sections_other1 / tot_cross_sections_other2
    par_cross_sections_elastic = par_cross_sections_elastic1 / par_cross_sections_elastic2
    par_cross_sections_decay = par_cross_sections_decay1 / par_cross_sections_decay2
    par_cross_sections_strings = par_cross_sections_strings1 / par_cross_sections_strings2
    par_cross_sections_other = par_cross_sections_other1 / par_cross_sections_other2
    coll_energy_elastic = coll_energy_elastic1 / coll_energy_elastic2
    coll_energy_decay = coll_energy_decay1 / coll_energy_decay2
    coll_energy_strings = coll_energy_strings1 / coll_energy_strings2
    coll_energy_other = coll_energy_other1 / coll_energy_other2

    tot_cross_sections_elastic[abs(tot_cross_sections_elastic) == np.inf] = 0
    tot_cross_sections_decays[abs(tot_cross_sections_decays) == np.inf] = 0
    tot_cross_sections_strings[abs(tot_cross_sections_strings) == np.inf] = 0
    tot_cross_sections_other[abs(tot_cross_sections_other) == np.inf] = 0
    par_cross_sections_elastic[abs(par_cross_sections_elastic) == np.inf] = 0
    par_cross_sections_decays[abs(par_cross_sections_decays) == np.inf] = 0
    par_cross_sections_strings[abs(par_cross_sections_strings) == np.inf] = 0
    par_cross_sections_other[abs(par_cross_sections_other) == np.inf] = 0
    coll_energy_elastic[abs(coll_energy_elastic) == np.inf] = 0
    coll_energy_decays[abs(coll_energy_decays) == np.inf] = 0
    coll_energy_strings[abs(coll_energy_strings) == np.inf] = 0
    coll_energy_other[abs(coll_energy_other) == np.inf] = 0

#print("Elastic 1: "+str(elastic1[i1s:i1e]/den1))
#print("Elastic 2: "+str(elastic2[i2s:i2e]/den2))



if verbose > 0:
    print("Warning, divison by zero (real divide) error messages are normal and are handled by the program, setting the result to 0")
    print("Writing the results in "+outputfile)
with open(outputfile,"wb") as outf:
    pickle.dump((header,dt,times,elastic,decays,strings,other,two_stable,one_stable,no_stable,\
                 min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar,total_hadrons,\
                 tot_cross_sections_elastic,tot_cross_sections_decays,tot_cross_sections_strings,tot_cross_sections_other,\
                 par_cross_sections_elastic,par_cross_sections_decays,par_cross_sections_strings,par_cross_sections_other,\
                 coll_energy_elastic,coll_energy_decays,coll_energy_strings,coll_energy_other,\
                 ),outf)
