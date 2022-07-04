#!/usr/bin/python3

import fileinput
import math
import numpy as np
import sys
import os

sp="    "

# if 0: only error messages, if > 0: progress messages
verbose=1

N_input_files=len(sys.argv)-2

if(N_input_files<2):
   print('Syntax: ./combine_results.py <outputfile> <inputfile 1> <inputfile 2> ... <inputfile n>')
   print("(The minimum number of input files is 2)")
   sys.exit(1)

outputfile=sys.argv[1]
print("Outputfile will be: "+outputfile+"\n")

inputfiles=[]
times=[]

for i in range(2,N_input_files+1):
    if verbose > 0:
        print("Add to input: "+sys.argv[i]+"\n")
    inputfiles.append(sys.argv[i])

datas = open(inputfiles[0],"r")
if verbose > 0:
    print("Opened: "+inputfiles[0]+"\n")


header1=datas.readline()
simtype=header.split()[1]

header2=datas.readline()
datas.readline()
header4=datas.readline()
header5=datas.readline()
header6=datas.readline()


for line in datas:
    stuff=line.split()
    times.append(float(stuff[0]))

date1.close()

nt=len(times)
dt=float(times[1])-float(times[0])

decays = np.zeros(nt,dtype=np.float64)
strings = np.zeros(nt,dtype=np.float64)
elastic = np.zeros(nt,dtype=np.float64)
other = np.zeros(nt,dtype=np.float64)

t=np.array(times,dtype=np.float64)

total_events = 0

for fi in range(0,N_input_files):
    if verbose > 0:
        print("Opening: "+inputfiles[fi]+"\n")
    datas = open(inputfiles[fi],"r")
    if datas.readline().split()[1] != simtype:
        print("Error, reference file is "+simtype+", but in "+inputfiles[fi]+" I found "+datas.readline().split()[1]+"!")
        print("I skip this file.")
    datas.readline() # we skip a row
    events = int(datas.readline().split()[4])
    total_events += events
    for i in range(3):
        datas.readline()
    for h in range(nt):
        entry_elastic,entry_decay,entry_string,entry_other=float(datas.readline.split()[1:])*dt*events
        elastic[h] += entry_elastic
        decays[h] += entry_decay
        strings[h] += entry_string
        other[h] += entry_other
    datas.close()

# now we print the results

# format for quantities in output file
tf='{:7.3f}'
ff='{:14.10e}'
sp="    "

if verbose > 0:
    print("Writing the results in "+outputfile)
outf = open(outputfile,"w")
outf.write(header1+"\n")
outf.write(header2+"\n")
outf.write("# Number of events: "+str(total_events)+"\n")
outf.write(header4+"\n")
outf.write(header5+"\n")
outf.write(header6+"\n")
for h in range(nt):
    outf.write(tf.format(t[h])+sp+ff.format(elastic[h]/(total_events*dt))+sp+ff.format(decays[h]/(total_events*dt))+sp+ff.format(strings[h]/(total_events*dt))+sp+ff.format(other[h]/(total_events*dt))+"\n")
outf.close()
