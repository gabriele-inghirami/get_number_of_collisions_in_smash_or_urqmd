#!/usr/bin/python3

import fileinput
import math
import numpy as np
import sys
import os

skip_rows=6
sp="    "

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
    print("Add to input: "+sys.argv[i]+"\n")
    inputfiles.append(sys.argv[i])

date1 = open(inputfiles[0],"r")
print("Opened: "+inputfiles[0]+"\n")

for i in range(skip_rows):
    date1.readline()

for line in date1:
    stuff=line.split()
    times.append(float(stuff[0]))

date1.close()

nt=len(times)
dt=float(times[1])-float(times[0])

t=np.array(times,dtype=np.float64)


for fi in range(0,N_input_files):
    print("Opening: "+inputfiles[fi]+"\n")
    date1 = open(inputfiles[fi],"r")


    date1.close()

