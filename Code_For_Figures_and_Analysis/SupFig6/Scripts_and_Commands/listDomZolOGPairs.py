import os
import sys
from collections import defaultdict

zol_dom_table = sys.argv[1]

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
    for j, lt1 in enumerate(sorted(pc_lts[pc])):
            for k, lt2 in enumerate(sorted(pc_lts[pc])):
                if j >= k: continue
                print(lt1 + '\t' + lt2)
