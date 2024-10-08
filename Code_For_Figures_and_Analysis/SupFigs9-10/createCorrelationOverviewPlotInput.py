import os
import sys
from collections import defaultdict
import scipy
import math
import pandas as pd
import numpy as np

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

def concordance_correlation_coefficient(y_true, y_pred):
    """
    Concordance correlation coefficient.
    Function taken from https://rowannicholls.github.io/python/statistics/agreement/concordance_correlation_coefficient.html
    """
    # Raw data
    dct = {
        'y_true': y_true,
        'y_pred': y_pred
    }
    df = pd.DataFrame(dct)
    # Remove NaNs
    df = df.dropna()
    # Pearson product-moment correlation coefficients
    y_true = df['y_true']
    y_pred = df['y_pred']
    cor = np.corrcoef(y_true, y_pred)[0][1]
    # Means
    mean_true = np.mean(y_true)
    mean_pred = np.mean(y_pred)
    # Population variances
    var_true = np.var(y_true)
    var_pred = np.var(y_pred)
    # Population standard deviations
    sd_true = np.std(y_true)
    sd_pred = np.std(y_pred)
    # Calculate CCC
    numerator = 2 * cor * sd_true * sd_pred
    denominator = var_true + var_pred + (mean_true - mean_pred)**2

    return numerator / denominator

def ccc(x,y):
    ''' Concordance Correlation Coefficient'''
    sxy = np.sum((x - x.mean())*(y - y.mean()))/x.shape[0]
    rhoc = 2*sxy / (np.var(x) + np.var(y) + (x.mean() - y.mean())**2)
    return rhoc

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
dr_drep_file = 'Derep99I99C_and_Reinflation.txt'
gc1_drep_file = 'Derep99I99C.txt'
gc2_drep_file = 'Derep97I95C.txt'
gw_drep_file = 'GW_dRep.txt'

wo_drep_dict, wo_hgs = processResults(no_drep_file)
dr_drep_dict, dr_hgs = processResults(dr_drep_file)
gc1_drep_dict, gc1_hgs = processResults(gc1_drep_file)
gc2_drep_dict, gc2_hgs = processResults(gc2_drep_file)
gw_drep_dict, gw_hgs = processResults(gw_drep_file)

all_hgs = list(set(wo_hgs.union(gc1_hgs).union(gw_hgs).union(gc2_hgs).union(dr_hgs)))

stats = ['conservation', 'tajimas_d', 'seg_sites_prop', 'entropy', 'median_betard', 'max_betard', 'selected_sites', 'avg_delta', 'prop_pos'] 
stats_names = ['Conservation', 'Tajimas D', 'Proportion Seg. Sites', 'Entropy', 'Median BetaRDgc', 'Max BetaRDgc', 'FUBAR Sel. Sites', 'FUBAR Avg. Detla', 'FUBAR Prop. Pos Sel.']
stat_ids = [1, 6, 5, 2, 3, 4, 7, 9, 8]
take_log = [False, False, True, True, False, False, False, False, False]

dicts = [gc1_drep_dict, gw_drep_dict, gc2_drep_dict, wo_drep_dict, dr_drep_dict]
dicts_names = ['GC_99I99C_Derep', 'GW_Derep', 'GC_97I95C_Derep', 'No_Derep', 'Derep_and_Reinflate']

print('Dereplication_Type_Comparison\tEvolutionary_Statistic\tStatistic_Order\tr')
for i, d1 in enumerate(dicts):
    d1_name = dicts_names[i]
    for j, d2 in enumerate(dicts):
        if i >= j: continue
        d2_name = dicts_names[j]
        for k, s in enumerate(stats):
            d1_vals = []
            d2_vals = []
            for hg in all_hgs:
                if d1[s][hg] != 'NA' and d2[s][hg] != 'NA':
                    d1v = float(d1[s][hg])
                    d2v = float(d2[s][hg])
                    if take_log[k]:
                        d1v = math.log(d1v+1e-5, 10)
                        d2v = math.log(d2v+1e-5, 10)
                    d1_vals.append(d1v)
                    d2_vals.append(d2v)
            ccc_val = concordance_correlation_coefficient(d1_vals, d2_vals)
            print(d1_name + ' vs. ' + d2_name + '\t' + s + '\t' + str(stat_ids[k]) + '\t' + str(round(ccc_val, 2)))
