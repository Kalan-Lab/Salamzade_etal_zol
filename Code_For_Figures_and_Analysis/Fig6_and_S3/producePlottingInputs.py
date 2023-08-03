import os
import sys
from collections import defaultdict
import math

"""
0	Homolog Group (HG) ID
1	HG is Single Copy?
2	Proportion of Total Gene Clusters with HG
3	HG Median Length (bp)
4	HG Consensus Order
5	HG Consensus Direction
6	Tajima's D
7	Proportion of Filtered Codon Alignment is Segregating Sites
8	Entropy
9	Upstream Region Entropy
10	Median Beta-RD-gc
11	Max Beta-RD-gc
12	Proportion of sites which are highly ambiguous in codon alignment
13	Proportion of sites which are highly ambiguous in trimmed codon alignment
14	Median GC
15	Median GC Skew
16	GARD Partitions Based on Recombination Breakpoints
17	Number of Sites Identified as Under Positive or Negative Selection by FUBAR
18	Average delta(Beta, Alpha) by FUBAR across sites
19	Proportion of Sites Under Selection which are Positive
20	Custom Annotation (E-value)
"""

def processResults(infile):
    dict_info = defaultdict(lambda: defaultdict(lambda: 'NA'))
    all_hgs = set([])
    with open(infile) as oif:
        for i, line in enumerate(oif):
            if i == 0: continue
            line = line.strip()
            ls = line.split('\t')
            hg = ls[20].split()[0]
            sc, cons, _, _, _, tajd, ssp, ent, ups_ent, med_brd, max_brd, _, _, _, _, _, sels, avg_delt, prop_pos = ls[1:20]
            if float(cons) < 0.25: continue
            if sc == 'False': continue
            all_hgs.add(hg)
            dict_info['single_copy'][hg] = sc
            dict_info['conservation'][hg] = cons
            dict_info['tajimas_d'][hg] = tajd
            dict_info['seg_sites_prop'][hg] = ssp
            dict_info['entropy'][hg] = ent
            dict_info['upstream_entropy'][hg] = ups_ent
            dict_info['median_betard'][hg] = med_brd
            dict_info['max_betard'][hg] = max_brd
            dict_info['selected_sites'][hg] = sels
            dict_info['avg_delta'][hg] = avg_delt
            dict_info['prop_pos'][hg] = prop_pos
    return([dict_info, all_hgs])

no_drep_file = 'Without_Dereplication.txt'
gc_drep_file = 'GeneCluster_Dereplication.txt'
gw_drep_file = 'GenomeWide_Dereplication.txt'

wo_drep_dict, wo_hgs = processResults(no_drep_file)
gc_drep_dict, gc_hgs = processResults(gc_drep_file)
gw_drep_dict, gw_hgs = processResults(gw_drep_file)

all_hgs = list(set(wo_hgs.union(gc_hgs).union(gw_hgs)))

stats = ['conservation', 'tajimas_d', 'seg_sites_prop', 'entropy', 'median_betard', 'max_betard', 'selected_sites', 'avg_delta', 'prop_pos'] 
stats_names = ['Conservation', 'Tajimas D', 'Proportion Seg. Sites (log10; PC of 1e-5)', 'Entropy (log10 PC of 1e-5)', 'Median BetaRDgc', 'Max BetaRDgc', 'FUBAR Sel. Sites', 'FUBAR Avg. Detla', 'FUBAR Prop. Pos Sel.']
stat_ids = [1, 6, 5, 2, 3, 4, 7, 9, 8]
take_log = [False, False, True, True, False, False, False, False, False]
take_log_base = [0, 0, 10, 10, 0, 0, 0, 0, 0]

dicts = [gc_drep_dict, gw_drep_dict, wo_drep_dict]
dicts_names = ['GC Drep', 'GW Drep', 'No Drep']

print('Dereplication_Type_Comparison\tEvolutionary_Statistic\tHomolog_Group\tValue_1\tValue_2')
for i, d1 in enumerate(dicts):
    d1_name = dicts_names[i]
    for j, d2 in enumerate(dicts):
        if i >= j: continue
        d2_name = dicts_names[j]
        for k, s in enumerate(stats):
            for hg in all_hgs:
                d1s = d1[s][hg]
                d2s = d2[s][hg]
                if take_log[k]:
                    try:
                        d1s = str(math.log(float(d1s)+1e-5, take_log_base[k]))
                    except:
                        d1s = 'NA'
                    try:
                        d2s = str(math.log(float(d2s)+1e-5, take_log_base[k]))
                    except:
                        d2s = 'NA'
                print(d1_name + ' vs. ' + d2_name + '\t' + str(stat_ids[k]) + '. ' + stats_names[k] + '\t' + hg.split('|')[0] + '\t' + d1s + '\t' + d2s)
