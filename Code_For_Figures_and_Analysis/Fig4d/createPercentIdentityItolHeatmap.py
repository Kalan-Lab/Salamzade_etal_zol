import os
import sys
from collections import defaultdict
from ete3 import Tree

match_results = 'Match_to_Names.txt'
fai_resdir = 'fai_Results/GC_Segment_Processing/GeneCluster_Info/'
rep_file = '../Best_Assemblies_per_Species.txt'

ref_to_ef = {}
efs = set([])
ef_to_ref = {}
gca_to_name = {}

with open(match_results) as omr:
    for line in omr:
        line = line.strip()
        ls = line.split('\t')
        ref_to_ef[ls[1]] = ls[2]
        efs.add(ls[2])
        ef_to_ref[ls[2]] = ls[1]

rep_gcas = set([])
with open(rep_file) as orf:
    for line in orf:
        line = line.strip()
        ls = line.split('\t')
        rep_gcas.add(ls[1])
        gca_to_name[ls[1]] = '_'.join(ls[0].split('s__')[1].split()) + '_' + ls[1].split('.')[0]

print('DATASET_HEATMAP')
print('SEPARATOR TAB')
print('COLOR\t#000000')
print('DATASET_LABEL\tepa')
print('FIELD_LABELS\t' + '\t'.join(sorted(efs, reverse=True)))
print('DATA')
for f in os.listdir(fai_resdir):
    gca = '_'.join(f.split('_')[:2])
    if not gca in rep_gcas or not f.endswith('hg_evalues.txt'): continue
    ref_best_bs = defaultdict(float)
    ref_best_pid = defaultdict(float)
    with open(fai_resdir + f) as off:
        for line in off:
            line = line.strip()
            ls = line.split('\t')
            if not ls[3] in ref_to_ef: continue
            bs = float(ls[4])
            pid = float(ls[5])
            if bs >= ref_best_bs[ls[3]]:
                ref_best_bs[ls[3]] = bs
                ref_best_pid[ls[3]] = pid
    row = [gca_to_name[gca]]
    for ef in sorted(efs, reverse=True):
        ref = ef_to_ref[ef]
        if ref in ref_best_bs:
            row.append(str(ref_best_pid[ref]))
        else:
            row.append('0.0')
    print('\t'.join(row))
