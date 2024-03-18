import os
import sys

slclust_results = sys.argv[1]
for line in open(slclust_results):
    line = line.strip()
    ls = line.split()
    for i, v1 in enumerate(sorted(ls)):
        for j, v2 in enumerate(sorted(ls)):
            if i >= j: continue
            print('\t'.join(sorted([v1, v2])))
