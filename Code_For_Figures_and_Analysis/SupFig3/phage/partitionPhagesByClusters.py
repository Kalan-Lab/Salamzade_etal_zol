import os
import sys
from collections import defaultdict

phamclust_file = 'PhamClust_Table.txt'

with open(phamclust_file) as opcf:
    for i, line in enumerate(opcf):
        line = line.strip()
        ls = line.split('\t')
        if i == 0: continue
        

