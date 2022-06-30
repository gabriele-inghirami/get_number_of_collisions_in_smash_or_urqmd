#!/usr/bin/python3

# it reads the hadron data in the smash collision files, extracts
# the time and the type of collisions and saves a histogram on a file
# the program automatically detects if the file is
# a .f15 urqmd or oscar2013 smash collision file

import math
import numpy as np
import os
import sys

# time resolution of the histograms
dt = 0.5
tmax = 200 + dt/2 # careful, the intervals are t1 <= t < t2, i.e. the upper border is out
nt = int(tmax/dt)

times = np.linspace(dt/2.,tmax+dt/2,num=nt)

events = 0
decays = np.zeros(nt,dytpe=np.float64)
strings = np.zeros(nt,dytpe=np.float64)
elastic = np.zeros(nt,dytpe=np.float64)
other = np.zeros(nt,dytpe=np.float64)

file_kind="unset"

# format for quantities in output file
ff='{:14.10e}'
sp="    "

# if we want to print debugging messages or not (0=none,1=advancement infos)
verbose = 1

def check_file_type(inputfile,file_kind):
    try:
         infile=open(inputfile,"r")
    except OSError:
         print("Could not open/read file: ", inputfile)
         return False, file_kind

    initium = infile.readfile().split()[0]
    if initium == "-1":
        if ( file_kind == "unset" ) or ( file_kind == "urqmd" )):
            return True, "urqmd"
        else:
            # the inputfile must be all of the same type of the first one
            return False, "mismatch"
    elif initium == "#!OSCAR2013":
        if ( file_kind == "unset" ) or ( file_kind == "smash" )):
            return True, "smash"
        else:
            # the inputfile must be all of the same type of the first one
            return False, "mismatch"
    else:
        return False, "unknown"
    

def extract_data_smash(inputfile):
    # the file should be already open
    for line in infile:
        stuff=line.split()
        if(len(stuff)==0):
            continue
        if stuff[1] == "interaction": 
            ptype = int(stuff[13]) 
            # we read the time from the first entry of the next line
            t = float(infile.readline().split()[1])
            if t >= tmax:
                continue
            h = int(math.floor(t/dt))
            if ptype == 1:
               elastic[h] += 1
            elif ptype == 7:
               decays[h] += 1
            elif ((ptype >= 41) and (ptype <= 46)): #we do not consider case 47, FailedString
               strings[h] += 1
            elif (ptype == 47): #we print a warning in case of FailedString
               if verbose > 0:
                   print("Warning, failed string collision.")
            else:
               other[h] += 1
        if stuff[1] == "event":
            events += 1
    return 

if (__name__ == "__main__" ):
    if (len(sys.argv)<3):
        print ('Syntax: ./get_number_of_collisions.py <output file name> <smash collision file 1> [smash collision file 2] ...')
        sys.exit(1)
    else:
        if (os.path.exists(sys.argv[1])):
            print("Output file "+sys.argv[1]+" already exists, I will not overwrite it. I stop here.")
            sys.exit(1)
        else:
            outf = open(sys.argv[1],"w")
        
        number_of_read_files = 0
        for afl in sys.argv[2:]:
            accepted, file_kind = check_file_type(inputfile,file_kind)
            if accepted:
                number_of_read_files += 1
                extract_data_smash(inputfile)
                reference_file_kind = file_kind
            else:
                if file_kind == "mismatch":
                   print("Inputfile " + inputfile + " of file kind " + file_kind + " does not match the reference kind " + reference_file_kind)
                else:
                   if file_kind != "unkown":
                       print("Something weird happened, the file should have been declared unkwown, instead of " + file_kind)
                       sys.exit(2)
                   print("Format of inputfile " + inputfile + " unknown")
                file_kind = reference_file_kind
        
