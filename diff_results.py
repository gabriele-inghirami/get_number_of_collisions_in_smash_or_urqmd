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

if(N_args!=4):
   print('Syntax: ./combine_results.py <outputfile> <inputfile 1> <inputfile 2>')
   sys.exit(1)

outputfile=sys.argv[1]
if verbose > 0:
    print("Outputfile will be: "+outputfile)

with open(sys.argv[2],"rb") as infile:
    if verbose > 0:
        print("Opening: "+sys.argv[2])
    data = pickle.load(infile)

header1,file_kind1,events1,dt1,times1,elastic1,decays1,strings1,other1,detailed1,two_stable1,one_stable1,no_stable1,\
        min_one_anti1,BaBa1,MeBa1,MeMe1,NuNu1,Nupi1,pipi1,NuNustar1 = data[:]
data=None
den1=events1*dt1

with open(sys.argv[3],"rb") as infile:
    if verbose > 0:
        print("Opening: "+sys.argv[3])
    data = pickle.load(infile)

header2,file_kind2,events2,dt2,times2,elastic2,decays2,strings2,other2,\
detailed2,two_stable2,one_stable2,no_stable2,min_one_anti2,BaBa2,MeBa2,MeMe2,\
NuNu2,Nupi2,pipi2,NuNustar2 = data[:]
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


header="# Difference between "+header1+" and " +header2+"\n"
header+="# stored in files "+sys.argv[1]+" and "+sys.argv[2]+"\n"

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

if verbose > 0:
    print("Writing the results in "+outputfile)
with open(outputfile,"wb") as outf:
    pickle.dump((header,dt,times,elastic,decays,strings,other,two_stable,one_stable,no_stable,\
                 min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar),outf)


