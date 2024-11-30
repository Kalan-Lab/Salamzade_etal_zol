import os
import sys

fz_lts_file = 'all_fai_zol_lts.txt'

fz_lts = set([])
with open(fz_lts_file) as of:
    for line in of:
        line = line.strip()
        fz_lts.add(line)

with open(sys.argv[1]) as of:
    for line in of:
        line = line.strip()
        ls = line.split('\t')
        if ls[0] in fz_lts or ls[1] in fz_lts:
            print(line)
