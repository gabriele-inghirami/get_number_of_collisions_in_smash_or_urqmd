#!/usr/bin/python3

# it reads the hadron data from UrQMD .f14 extended (i.e. with "cto 41 1"
# in inputfile) output files and it writes a text file with the average
# reduction factor

import math
import numpy as np
import os
import sys
import pickle

events = 0

tmin = 0
tmax = 5

red_factor_list = []

# if we want to print debugging messages or not (0=none,1=advancement infos)
verbose = 1

def count_times(infile):
    times_list = []
    go_on = True
    with open(infile,"r") as ifile:
        for i in range(17):
            bb = ifile.readline()
        while go_on:
            try:
                raw_item = ifile.readline().split()[0]
            except:
                go_on = False
                continue
            if raw_item == "UQMD":
                go_on = False
                continue
            items = int(raw_item) - 1
            bb = ifile.readline().split() # unuseful line
            new_time = float(ifile.readline().split()[0])
            if new_time > tmax:
                go_on = False
                continue
            elif new_time < tmin:
                continue
            else:
                times_list.append(new_time)
            if items > 0:
                for i in range(items):
                    bb = ifile.readline()
    times = np.array(times_list,dtype=np.float64)
    nt = times.size
    return nt, times

def extract_data_urqmd(infile,redf_arr,had_arr,times,dt):
    events_in_file = 0
    if verbose > 0:
        print("Reading data from "+infile)
    with open(infile,"r") as ifile:
        nl = 0
        for line in ifile:
            nl += 1
            stuff = line.split()
            if stuff[0] == "UQMD":
                events_in_file += 1
            else:
                # this algorithm is not efficient, it does not use the information available on the content of the file, but it is simple
                if (len(stuff) == 19):
                    t = float(stuff[0])
                    if ((t >= times[0]) and (t <= times[-1])):
                        t_index = int((t-times[0])/dt)
                        redf_arr[t_index] += float(stuff[17])
                        had_arr[t_index] += 1
    return events_in_file

if (len(sys.argv)<3):
    print ('Syntax: ./get_urmqd_avg_reduction_factor.py <output file> <extended .f14 file 1> [extended .f14 file 2] ...')
    sys.exit(1)

outfile=sys.argv[1]

if os.path.exists(outfile):
    print("Output file "+outfile+" already exists, I will not overwrite it. I stop here.")
    sys.exit(1)
    
nt, times = count_times(sys.argv[2])
dt = times[1] - times[0] # we assume to have more than one time
cross_section_reduction_factor_array = np.zeros(nt,dtype=np.float64)
hadrons = np.zeros(nt,dtype=np.float64)
events += extract_data_urqmd(sys.argv[2],cross_section_reduction_factor_array,hadrons,times,dt)

for infile in sys.argv[3:]:
    events += extract_data_urqmd(infile,cross_section_reduction_factor_array,hadrons,times,dt)

# we save the results
with open(outfile,"wb") as outf:
    pickle.dump((times,cross_section_reduction_factor_array,hadrons,events),outf)
