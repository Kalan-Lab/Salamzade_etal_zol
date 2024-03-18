import os
import sys
from collections import defaultdict

gt_og_file = 'GT_OGs.txt'
gt_og_name_file = 'OG_to_Name.txt'
cons_rep_file = 'Consolidated_Report.tsv'
clade_dir = 'Clade_Listings/'

gca_to_clade = defaultdict(lambda: 'Other')
for cl in os.listdir(clade_dir):
    with open(clade_dir + cl) as ocf:
        for line in ocf:
            line = line.strip()
            gca = '_'.join(line.split('|')[0].split('_')[-2:])
            gca_to_clade[gca] = cl.split('.txt')[0]

og_to_name = defaultdict(lambda: '')
with open(gt_og_name_file) as ogonf:
    for line in ogonf:
        line = line.strip()
        ls = line.split('\t')
        og_to_name[ls[0]] = '|' + ls[1] 

og_gcas = defaultdict(set)
with open(cons_rep_file) as ocrf:
    for i, line in enumerate(ocrf):
        if i == 0: continue
        line = line.strip()
        ls = line.split('\t')
        og = ls[0]
        gcs = ls[-2]
        for gc in gcs.split(';'):
            gc = gc.strip()
            gca = '_'.join(gc.split('|')[0].split('_')[:2]).split('.')[0]
            og_gcas[og].add(gca)

print('OG\tClade\tCount\tTotal_Count')
with open(gt_og_file) as ogof:
    for line in ogof:
        line = line.strip()
        name = line + og_to_name[line]
        clade_counts = defaultdict(int)
        for gca in og_gcas[line]:
            clade = gca_to_clade[gca]
            clade_counts[clade] += 1
        for clade in clade_counts:
            print(name + '\t' + clade + '\t' + str(clade_counts[clade]) + '\t' + str(sum(clade_counts.values())))
