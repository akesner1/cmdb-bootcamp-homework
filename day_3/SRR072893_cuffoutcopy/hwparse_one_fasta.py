#!/usr/bin/env python


"""
Parse a single FASTA record from stdin and print it
"""

import sys     #this lets you read the stdin and stdout 

line = sys.stdin.readline()   #read first line in the file
assert line.startswith( ">" )  # makes sure this is the line we expect
sid = line[1:].rstrip("\r\n")  # take first character off string, and strip new line characters off end of thestring

sequences = []                  # creat a lsit to acuumulate data into
while True:
    line = sys.stdin.readline()  #keep reading lines of the file
    if line.startswith(">"):    
        break                      #if the line begins with a header, stop
    else:
        sequences.append( line.strip() )   #strips all white space from sequence
        
sequence = "".join( sequences )          #joins all things in the list, concatonates the list

print sid, sequence

#  /Users/cmdb/data/day3 $ ./parse_one_fasta.py  < transcripts_15.fa | less -S      do this to check to see if above works