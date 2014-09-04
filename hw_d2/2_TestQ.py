#!/usr/bin/env python


import pandas as pd


for thing in ( 905, 906, 907, 908, 909, 911, 913, 915 ):
    file = "Users/cmdb/data/results/SRR072%s_clout"  % (thing)
    pdfile = pd.read_table(file)
    pdgenes = pdfile["Sxl"]
pdgenes.to_.csv("Slx_metadata.csv")    