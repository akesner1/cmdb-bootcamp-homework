#!/usr/bin/env python

import sys
import pandas as pd


header_file = "/Users/cmdb/cmdb-bootcamp-homework/Day_4/chromo_header_lines.txt"

file = open( header_file )



stripts = []
for line in file:
    if line.startswith(">"):
        x = line[1:].rstrip("\r\n")
        stripts.append( x )
        
for things in stripts:
    names = things.split()
    #print names[0],"\t","length"
    fix_length = things.split()
    close = fix_length[2].split("..")
    print names[0], "\t", close[1].strip(";")


