import os
import sys
from collections import defaultdict

fai_info_dir = 'fai_Results/GC_Segment_Processing/GeneCluster_Info/'

ref_hg_hits = defaultdict(set)
for f in os.listdir(fai_info_dir):
    fai_info_file = fai_info_dir + f 
    if not fai_info_file.endswith('.hg_evalues.txt'): continue
    with open(fai_info_file) as ofif:
        for line in ofif:
            line = line.strip()
            ls = line.split('\t')
            hg = ls[3]
            if not hg.startswith('OG_'): continue
            lt = ls[2]
            ref_hg_hits[hg].add(lt)

for hg in ref_hg_hits:
    for i, lt1 in enumerate(sorted(ref_hg_hits[hg])):
        for j, lt2 in enumerate(sorted(ref_hg_hits[hg])):
            if i >= j: continue
            print('\t'.join(sorted([lt1, lt2])))
