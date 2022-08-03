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

# time resolution of the histograms
dt = 0.5
tmin = -3 - dt/2
tmax = 200 + dt/2 # careful, the intervals are t1 <= t < t2, i.e. the upper border is out
nt = int((tmax-tmin)/dt)

times = np.linspace(tmin+dt/2,tmax-dt/2,num=nt)

events = 0
decays = np.zeros(nt,dtype=np.float64)
strings = np.zeros(nt,dtype=np.float64)
elastic = np.zeros(nt,dtype=np.float64)
other = np.zeros(nt,dtype=np.float64)

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
# first index: time, second index: event type, third index: quantity
cross_sections = np.zeros((nt,4,3),dtype=np.float64)

two_stable = np.zeros(nt,dtype=np.float64)
one_stable = np.zeros(nt,dtype=np.float64)
no_stable = np.zeros(nt,dtype=np.float64)
min_one_anti = np.zeros(nt,dtype=np.float64)
BaBa = np.zeros(nt,dtype=np.float64)
MeBa = np.zeros(nt,dtype=np.float64)
MeMe = np.zeros(nt,dtype=np.float64)
NuNu = np.zeros(nt,dtype=np.float64)
Nupi = np.zeros(nt,dtype=np.float64)
pipi = np.zeros(nt,dtype=np.float64)
NuNustar = np.zeros(nt,dtype=np.float64)

tot_hadrons = np.zeros(nt,dtype=np.float64)

file_kind="unset"

# if we want to print debugging messages or not (0=none,1=advancement infos)
verbose = 1

def count_based_on_hadron_property(had_prop,h):
    if (had_prop[had_prop_dict["is_stable"]]>1):
        two_stable[h] += 1
    elif(had_prop[had_prop_dict["is_stable"]]==1):
        one_stable[h] += 1
    else:
        no_stable[h] += 1
    if (had_prop[had_prop_dict["is_antiparticle"]]>0):
        min_one_anti[h] +=1
    if (had_prop[had_prop_dict["is_baryon"]]>1):
        BaBa[h] += 1
    if ((had_prop[had_prop_dict["is_baryon"]]>0) and (had_prop[had_prop_dict["is_meson"]]>0)):
        MeBa[h] += 1
    if (had_prop[had_prop_dict["is_meson"]]>1):
        MeMe[h] += 1
    if (had_prop[had_prop_dict["is_nucleon"]]>1):
        NuNu[h] +=1
    if ((had_prop[had_prop_dict["is_nucleon"]]>0) and (had_prop[had_prop_dict["is_pion"]]>0)):
        Nupi[h] +=1
    if (had_prop[had_prop_dict["is_pion"]]>1):
        pipi[h] +=1
    if ((had_prop[had_prop_dict["is_nucleon"]]>0) and (had_prop[had_prop_dict["is_N_star"]]>0)):
        NuNustar[h] +=1


def check_file_type(inputfile,file_kind):
    try:
         infile=open(inputfile,"r")
    except OSError:
         print("Could not open/read file: ", inputfile)
         return False, file_kind, None

    initium = infile.readline().split()[0]
    if initium == "-1":
        if (( file_kind == "unset" ) or ( file_kind == "urqmd" )):
            if (( verbose > 0 ) and ( file_kind == "unset" )):
                print("Detected urqmd output file type")
            return True, "urqmd", infile
        else:
            # the inputfile must be all of the same type of the first one
            return False, "mismatch", None
    elif initium == "#!OSCAR2013":
        if (( file_kind == "unset" ) or ( file_kind == "smash" )):
            if (( verbose > 0 ) and ( file_kind == "unset" )):
                print("Detected smash output file type")
            return True, "smash", infile
        else:
            # the inputfile must be all of the same type of the first one
            return False, "mismatch", None
    else:
        return False, "unknown", None
    

def extract_data_smash(ifile):
    events_in_file = 0
    # the file should be already open
    for line in ifile:
        stuff=line.split()
        if(len(stuff)==0):
            continue
        if stuff[1] == "interaction": 
            ptype = int(stuff[13]) 
            n_incoming = int(stuff[3])
            n_outgoing = int(stuff[5])
            new_particles = n_outgoing - n_incoming
            total_cross_section = float(stuff[9])
            partial_cross_section = float(stuff[11])
            # we read the time from the first entry of the next line
            stuff_N=ifile.readline().split()
            t = float(stuff_N[0])
            if t >= tmax:
                continue
            h = int(math.floor((t-tmin)/dt))
            # if you change the process types, please, remeber to update the legend in the header of the output file
            if ptype == 1:
               elastic[h] += 1
               k_idx = k_ela
            elif ptype == 5:
               decays[h] += 1
               k_idx = k_dec
            elif ((ptype >= 41) and (ptype <= 46)): #we do not consider case 47, FailedString
               strings[h] += 1
               k_idx = k_str
            elif (ptype == 47): #we print a warning in case of FailedString
               if verbose > 0:
                   print("Warning, failed string collision.")
            else:
               other[h] += 1
               k_idx = k_oth

            detailed[h,ptype_smash[ptype][0]]+=1

            tot_hadrons[h] += new_particles

            had_prop = np.zeros(7,dtype=np.int32)
            pid = stuff_N[9] # we have already read the first line after the interaction event header to get the collision time
            tot4m = np.array(float(stuff_N[4:8]))
            had_prop += get_hadron_info_smash(pid) #the function returns a list which is automatically converted into np array
            if n_incoming > 1:
                for had in range(n_incoming-1):
                   stuff_N = ifile.readline().split()
                   pid = stuff_N[9]
                   tot4m += np.array(float(stuff_N[4:8]))
                   had_prop += get_hadron_info_smash(pid) #the function returns a list which is automatically converted into np array

            count_based_on_hadron_property(had_prop,h)
            coll_energy = tot4m[0]**2-tot4m[1]**2-tot4m[2]**2-tot4m[3]**2

            cross_sections[h,k_idx,k_tot] += total_cross_section
            cross_sections[h,k_idx,k_par] += partial_cross_section
            cross_sections[h,k_idx,k_cen] += coll_energy


        if stuff[1] == "event":
            events_in_file += 1
    return events_in_file

def extract_data_urqmd(ifile):
    events_in_file = 1 #the event flag is "-1", but it has been already read by check_file_type
    # the file should be already open
    for line in ifile:
        stuff = line.split()
        if(len(stuff)!=9):
            continue
        if stuff[0] == "-1":
            events_in_file += 1
            continue
        ptype = int(stuff[2]) 
        t = float(stuff[4])
        n_incoming = int(stuff[0])
        n_outgoing = int(stuff[1])
        new_particles = n_outgoing - n_incoming
        coll_energy = float(stuff[5])
        total_cross_section = float(stuff[6])
        partial_cross_section = float(stuff[7])
        if t >= tmax:
            continue
        h = int(math.floor((t-tmin)/dt))
        # if you change the process types, please, remeber to update the legend in the header of the output file
        if ((ptype == 13) or (ptype == 17) or (ptype == 19) or (ptype == 22) or (ptype == 26) or (ptype == 38)):
            elastic[h] += 1
            k_idx = k_ela
        elif ptype == 20:
            decays[h] += 1
            k_idx = k_dec
        elif ((ptype == 15) or (ptype == 23) or (ptype == 24) or (ptype == 27) or (ptype == 28)): 
            strings[h] += 1
            k_idx = k_str
        else:
            other[h] += 1
            k_idx = k_oth

        detailed[h,ptype_urqmd[ptype][0]]+=1

        tot_hadrons[h] += new_particles

        had_prop = np.zeros(7,dtype=np.int32)
        for had in range(n_incoming):
            stuff = ifile.readline().split()
            pid = int(stuff[10])
            charge = int(stuff[12])
            had_prop += get_hadron_info_urqmd(pid,charge) #the function returns a list which is automatically converted into np array

        count_based_on_hadron_property(had_prop,h)

        cross_sections[h,k_idx,k_tot] += total_cross_section
        cross_sections[h,k_idx,k_par] += partial_cross_section
        cross_sections[h,k_idx,k_cen] += coll_energy

    return events_in_file 

if (len(sys.argv)<4):
    print ('Syntax: ./get_number_of_collisions.py <output file> <output file header info> <collision file 1> [collision file 2] ...')
    sys.exit(1)

outfile=sys.argv[1]
label_header=sys.argv[2]

if os.path.exists(outfile):
    print("Output file "+outfile+" already exists, I will not overwrite it. I stop here.")
    sys.exit(1)
else:
    if os.path.exists(label_header):
        print("The header of the output file "+label_header+" is also the name of a collision file.")
        print("Probably this is not what you want. The header file can be also a empty string.")
        sys.exit(1)
    
number_of_read_files = 0
for infile in sys.argv[3:]:
    accepted, file_kind, file_handler = check_file_type(infile,file_kind)
    if accepted:
        number_of_read_files += 1
        if verbose > 0:
            print("Reading file "+infile)
        if file_kind == "smash":
            if (number_of_read_files == 1):
                detailed=np.zeros((nt,n_ptype_smash),dtype=np.float64)
            events += extract_data_smash(file_handler)
        else:
            if (number_of_read_files == 1):
                detailed=np.zeros((nt,n_ptype_urqmd),dtype=np.float64)
            events += extract_data_urqmd(file_handler)
        reference_file_kind = file_kind
    else:
        if file_kind == "mismatch":
           print("Inputfile " + infile + " of file kind " + file_kind + " does not match the reference kind " + reference_file_kind)
        else:
           if file_kind != "unkown":
               print("Something weird happened, the file should have been declared unkwown, instead of " + file_kind)
               sys.exit(2)
           print("Format of inputfile " + infile + " unknown")
        file_kind = reference_file_kind

if number_of_read_files == 0:
    print("Sorry, something went wrong, I did not read any file...")
    sys.exit(2)
    
# now we print the results
if verbose > 0:
    print("Writing the results in "+outfile)
    print("Warning, you are advised to take note of the commit number of the repository that you used to produce these results.")
with open(outfile,"wb") as outf:
    pickle.dump((label_header,file_kind,events,dt,times,elastic,decays,strings,other,detailed,two_stable,one_stable,no_stable,\
                 min_one_anti,BaBa,MeBa,MeMe,NuNu,Nupi,pipi,NuNustar,tot_hadrons,cross_sections),outf)
