import os
import sys
import math

data_file = sys.argv[1]

with open(data_file) as odf:
    for i, line in enumerate(odf):
        if i == 0: 
            print(line.strip())
            continue
        line = line.strip()
        ls = line.split('\t')
        if ls[1] == 'Maximum of maximum E-values observed for any OG':
            ls[1] = 'Maximum of maximum E-values observed for any OG (log10)'
            ls[2] = str(math.log(float(ls[2]), 10))
        elif ls[1] == 'Maximum of near-core OG E-values observed:':
            ls[1] = 'Maximum of near-core OG E-values observed (log10):'
            ls[2] = str(math.log(float(ls[2]), 10))
        print('\t'.join(ls))
