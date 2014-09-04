#!/usr/bin/env python

### Make boxplot of top/middle/bottom 1/3rd FPKMs -- for SRR072893, SRR072915
###    	HINT: pass plt.boxplot() a 3-element list
        
        
import pandas as pd

cufflinks_output  = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
cufflinks_output2 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

df  = pd.read_table( cufflinks_output )
df2 = pd.read_table( cufflinks_output2 )


data = [ df["FPKM"], df2["FPKM"] ]

import matplotlib.pyplot as plt

plt.figure()

plt.title("Thirds male cycle vs female cycle 14d")

plt.boxplot(data)

plt.savefig("boxplot 1.png")
