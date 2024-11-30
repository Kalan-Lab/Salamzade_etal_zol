import os
import sys
from collections import defaultdict

zol_dom_table = sys.argv[1]
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

pc_lts = defaultdict(set)
with open(zol_dom_table) as ozdt:
    for i, line in enumerate(ozdt):
        if i == 0: continue
        line = line.strip('\n')
        ls = line.split('\t')
        pc = ls[4]
        doms = ls[-2]
        for dom in doms.split('; '):
            lt = dom.split('|')[1]
            pc_lts[pc].add(lt)

for pc in pc_lts:
    for lt in pc_lts[pc]:
        print(lt + '\t' + pc + '\t' + lt_to_tog[lt])
