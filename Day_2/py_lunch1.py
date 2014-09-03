#!/usr/bin/env python

accepted_hits_sam = "/Users/cmdb/data/day1/SRR072893_thout/accepted_hits.sam"

f = open( accepted_hits_sam )

nl = 0
while True:          
    line = f.readline()          #f.readline is reading a line from f which is our file above
    if line == "":
        break
    else:
        nl = nl + 1
print nl