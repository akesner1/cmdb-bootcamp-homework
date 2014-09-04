#!/usr/bin/env python

### Make boxplot of top/middle/bottom 1/3rd FPKMs -- for SRR072893, SRR072915
###    	HINT: pass plt.boxplot() a 3-element list
        
        
import pandas as pd

cufflinks_output  = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

f = open(cufflinks_output)
f2 = open(cufflinks_output2)

df  = pd.read_table( cufflinks_output )
df2 = pd.read_table( cufflinks_output2 )


### Below will generate the number of rows that comprise a third of the total number, given the file(s) listed above

nlf = 0
while True:
    line = f.readline()
    if line == "":
        break
    nlf = nlf + 1
# now nlf is number of lines (ie nlf) in f (or SRR07893)    5201
third_num_rowsf = [nlf / 3]
###print "third_num_rowsf is %s" %(third_num_rowsf) ###YESSSS
###print type(third_num_rowsf)  # is a list

nlf2 = 0
while True:
    line = f2.readline()
    if line == "":
        break
    nlf2 = nlf2 + 1
third_num_rowsf2 = [nlf / 3]
####print "third_num_rowsf2 is %s" %(third_num_rowsf2) ###YESSSS

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

### Below is building a sorted list of the FPKM data for each file
total_male_FPKM = df["FPKM"]
###print total_male_FPKM

total_female_FPKM = df2["FPKM"]
###print total_female_FPKM

total_male_sort = sorted(total_male_FPKM)
###print total_male_sort

total_female_sort = sorted(total_female_FPKM)



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###below is how i want to do it so i could potentially use any file and split it up regardless of how many lines... the concept is to split the total sorted list above into thirds using the "third" number generated in the counting code... however, this 'count' / 3, is stored as a variable that is type 'list'. so the slicing below doesnt workl because it needs two integers!

#male_bot = total_male_sort[1:third_num_rowsf]
#male_mid = total_male_sort[(third_num_rowsf + 1) :(2 * third_num_rowsf]
#male_top =total_male_sort[2 * third_num_rowsf + 1: ]

#female_bot = total_female_sort[1:third_num_rowsf2]
#female_mid = total_female_sort[(third_num_rowsf2 + 1) :(2 * third_num_rowsf2]
#female_top =total_female_sort[2 * third_num_rowsf2 + 1: ]



### below is last ditch effort to split them up into thirds by entering numbers manually for the 'third-ranges'
male_bot = total_male_sort[1:5201]
male_mid = total_male_sort[5202:10403]
male_top =total_male_sort[10403:]

female_bot = total_female_sort[1:5201]
female_mid = total_female_sort[5202:10403]
female_top =total_female_sort[10403:]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

###below works to plot the data
data = [ "M_Bot" : male_bot, "M_Mid" : male_mid, "M_Top" : male_top, "F_Bot" : female_bot, "F_Mid" : female_mid, "F_Top" : female_top ]

import matplotlib.pyplot as plt

plt.figure()

plt.title("Thirds male cycle vs female cycle 14d")

#top = 5000
#bottom = 0
#plt.ylim(bottom, top)

plt.boxplot(data)

plt.axis([0, 7, 0, 4000])

plt.savefig("boxplot_mf_topmidbot4.png")