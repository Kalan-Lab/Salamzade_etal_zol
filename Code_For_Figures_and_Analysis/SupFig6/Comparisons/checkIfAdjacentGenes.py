import os
import sys
from collections import defaultdict

fai_info_dir = '../fai_Results/GC_Segment_Processing/GeneCluster_Info/'

lt_to_hg_val = defaultdict(list)
for f in os.listdir(fai_info_dir):
    fai_info_file = fai_info_dir + f
    if not fai_info_file.endswith('.hg_evalues.txt'): continue
    with open(fai_info_file) as ofif:
        for line in ofif:
            line = line.strip()
            ls = line.split('\t')
            hg = ls[3]
            lt = ls[2]
            if not hg.startswith('OG_'): continue
            hg_val = int(hg.split('_')[1])
            lt_to_hg_val[lt].append(hg_val)
            if hg_val == 2052:
                lt_to_hg_val[lt].append(2064)

with open(sys.argv[1]) as of:
    for line in of:
        line = line.strip()
        ls = line.split('\t')
        lt1, lt2 = ls
        are_adjacent = False
        for o1 in lt_to_hg_val[lt1]:
            for o2 in lt_to_hg_val[lt2]:
                diff_val = abs(o1-o2)
                assert(diff_val != 0)
                if diff_val <= 3:
                    are_adjacent = True

        if not are_adjacent:
            print(line)

