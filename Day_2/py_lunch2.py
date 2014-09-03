#!/usr/bin/env python

### since phred scale = -10log (p) and if p = 1, then its a perfect allignment, so AS will be 0
### we will look for number of allignments with AS:i:0
### we will count in column 11 the number that say AS:i:0


accepted_hits_sam = "/Users/cmdb/data/day1/SRR072893_thout/accepted_hits.sam"

f = open( accepted_hits_sam )


for line in f:
    if "AS:i:0":
        count = 0
        for lines in f:
            if lines.strip():
                count +=1
            print count