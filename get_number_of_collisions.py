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
tmin = -3 - dt/2
tmax = 200 + dt/2 # careful, the intervals are t1 <= t < t2, i.e. the upper border is out
nt = int((tmax-tmin)/dt)

times = np.linspace(tmin+dt/2,tmax-dt/2,num=nt)

events = 0
decays = np.zeros(nt,dtype=np.float64)
strings = np.zeros(nt,dtype=np.float64)
elastic = np.zeros(nt,dtype=np.float64)
other = np.zeros(nt,dtype=np.float64)

file_kind="unset"

# format for quantities in output file
tf='{:7.3f}'
ff='{:14.10e}'
sp="    "

# if we want to print debugging messages or not (0=none,1=advancement infos)
verbose = 1

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
            # we read the time from the first entry of the next line
            t = float(ifile.readline().split()[0])
            if t >= tmax:
                continue
            h = int(math.floor((t-tmin)/dt))
            # if you change the process types, please, remeber to update the legend in the header of the output file
            if ptype == 1:
               elastic[h] += 1
            elif ptype == 5:
               decays[h] += 1
            elif ((ptype >= 41) and (ptype <= 46)): #we do not consider case 47, FailedString
               strings[h] += 1
            elif (ptype == 47): #we print a warning in case of FailedString
               if verbose > 0:
                   print("Warning, failed string collision.")
            else:
               other[h] += 1
        if stuff[1] == "event":
            events_in_file += 1
    return events_in_file

def extract_data_urqmd(ifile):
    events_in_file = 1 #the event flag is "-1", but it has been already read by check_file_type
    # the file should be already open
    for line in ifile:
        stuff=line.split()
        if(len(stuff)!=9):
            continue
        if stuff[0] == "-1":
            events_in_file += 1
            continue
        ptype = int(stuff[2]) 
        t = float(stuff[4])
        if t >= tmax:
            continue
        h = int(math.floor((t-tmin)/dt))
        # if you change the process types, please, remeber to update the legend in the header of the output file
        if ((ptype == 13) or (ptype == 17) or (ptype == 19) or (ptype == 22) or (ptype == 26)):
            elastic[h] += 1
        elif ptype == 20:
            decays[h] += 1
        elif ((ptype == 15) or (ptype == 23) or (ptype == 24) or (ptype == 27) or (ptype == 28)): 
            strings[h] += 1
        else:
            other[h] += 1
    return events_in_file 

if (len(sys.argv)<4):
    print ('Syntax: ./get_number_of_collisions.py <output file name> <output file header info> <collision file 1> [collision file 2] ...')
    sys.exit(1)

if os.path.exists(sys.argv[1]):
    print("Output file "+sys.argv[1]+" already exists, I will not overwrite it. I stop here.")
    sys.exit(1)
else:
    if os.path.exists(sys.argv[2]):
        print("The header of the output file "+sys.argv[2]+" is also the name of a collision file.")
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
            events += extract_data_smash(file_handler)
        else:
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
    print("Writing the results in "+sys.argv[1])
outf = open(sys.argv[1],"w")
outf.write("# "+sys.argv[2]+"\n")
outf.write("# Data from "+file_kind+" simulations\n")
outf.write("# Number of events: "+str(events)+"\n")
outf.write("# Process types considered: \n")
if file_kind == "smash":
    outf.write("# elastic: 1  *  decays: 5  *  strings: >=41,<=46\n")
elif file_kind == "urqmd":
    outf.write("# elastic: 13,17,19,22,26  *  decays: 20  *  strings: 15,23,24,27,28\n")
outf.write("# columns: 1: time [fm]     2: dN/dt elastic     3: dN/dt decays     4: dN/dt strings     6: dN/dt other\n")
for h in range(nt):
    outf.write(tf.format(times[h])+sp+ff.format(elastic[h]/(events*dt))+sp+ff.format(decays[h]/(events*dt))+sp+ff.format(strings[h]/(events*dt))+sp+ff.format(other[h]/(events*dt))+"\n")
outf.close()
