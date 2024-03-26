import os
import sys

for line in open(sys.argv[1]):
    line = line.strip()
    ls = line.split()
    if len(ls) != 4: continue
    ls = ls[:2]
    if ls[0] == 'Query' and ls[1] == 'Target': continue
    print('\t'.join(sorted(ls)))
