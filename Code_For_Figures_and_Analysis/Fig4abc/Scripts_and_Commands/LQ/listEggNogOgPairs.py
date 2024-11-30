import os
import sys
from collections import defaultdict

eggnog_annot_file  = sys.argv[1]
level = sys.argv[2]

og_lts = defaultdict(set)
with open(eggnog_annot_file) as oeaf:
    for line in oeaf:
        if line.startswith('#'): continue
        line = line.strip()
        ls = line.split('\t')
        lt = ls[0]
        ogs = ls[4]
        og = None
        if level == 'resolute':
            if '|Enterococcaceae' in ogs.split(',')[-1]:
                og = ogs.split(',')[-1]
        elif level == 'coarse':
            if '|root' in ogs.split(',')[0]:
                og = ogs.split(',')[0]
        if og != None:
            og_lts[og].add(lt)

for og in og_lts:
    for i, lt1 in enumerate(sorted(og_lts[og])):
        for j, lt2 in enumerate(sorted(og_lts[og])):
            if i >= j: continue
            print(lt1 + '\t' + lt2)

