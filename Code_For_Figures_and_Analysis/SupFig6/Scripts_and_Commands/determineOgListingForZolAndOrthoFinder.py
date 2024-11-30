import os
import sys
from collections import defaultdict

og_mat_file = sys.argv[1]
fai_info_dir = 'fai_Results/GC_Segment_Processing/GeneCluster_Info/'

lt_to_tog = defaultdict(lambda: 'NA')
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
            lt_to_tog[lt] = hg

with open(og_mat_file) as of:
    for i, line in enumerate(of):
        if i == 0: continue
        line = line.strip()
        ls = line.split('\t')
        og = ls[0]
        genes = set([])
        for gs in ls[1:]:
            for g in gs.split(', '):
                g = g.strip()
                if g != '':
                    if '|' in g:
                        genes.add(g.split('|')[1])
                    else:
                        genes.add(g)
        for g in genes:
            print(g + '\t' + og + '\t' + lt_to_tog[g])
