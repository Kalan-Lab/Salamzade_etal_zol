import os
import sys
from collections import defaultdict
from ete3 import Tree

self_blast_results = 'epa_self_blast_results.txt' # 
match_results = 'Match_to_Names.txt' # 
drep_listing_file = 'dereplicated_genomes.listing.txt' # 
fai_resdir = 'GeneCluster_Info/' # Folder within fai_Results/GC_Segment_Processing/
gca_to_name_file = 'Enterococcus_Genomes.txt'

sb_bitscore = defaultdict(float)
ref_to_ef = {}
efs = set([])
ef_to_ref = {}
gca_to_name = {}

with open(self_blast_results) as osbr:
    for line in osbr:
        line = line.strip()
        ls = line.split('\t')
        if ls[0] == ls[1]: 
            sb_bitscore[ls[0]] = float(ls[-2])

with open(match_results) as omr:
    for line in omr:
        line = line.strip()
        ls = line.split('\t')
        ref_to_ef[ls[1]] = ls[2]
        efs.add(ls[2])
        ef_to_ref[ls[2]] = ls[1]

with open(gca_to_name_file) as ogtnf:
    for line in ogtnf:
        line = line.strip()
        ls = line.split('\t')
        gca_to_name[ls[6]] = ls[1]
gca_to_name['GCF_000633635.1'] = 'Enterococcus_crotali_RS_GCF_000633635_1'

drep_gcas = set([])
with open(drep_listing_file) as odlf:
    for line in odlf:
        f = line.split('/')[1].strip()
        drep_gcas.add('_'.join(f.split('_')[:2]))

print('DATASET_HEATMAP')
print('SEPARATOR TAB')
print('COLOR\t#000000')
print('DATASET_LABEL\tepa')
print('FIELD_LABELS\t' + '\t'.join(sorted(efs, reverse=True)))
print('DATA')
for f in os.listdir(fai_resdir):
    gca = '_'.join(f.split('_')[:2])
    if not gca in drep_gcas or not f.endswith('hg_evalues.txt'): continue
    ref_best_bs = defaultdict(float)
    with open(fai_resdir + f) as off:
        for line in off:
            line = line.strip()
            ls = line.split('\t')
            if not ls[3] in ref_to_ef: continue
            bs = float(ls[4])
            if bs >= ref_best_bs[ls[3]]:
                ref_best_bs[ls[3]] = bs
    row = [gca_to_name[gca]]
    for ef in sorted(efs, reverse=True):
        ref = ef_to_ref[ef]
        if ref in ref_best_bs:
            row.append(str(float(ref_best_bs[ref])/float(sb_bitscore[ef])))
        else:
            row.append('0.0')
    print('\t'.join(row))
