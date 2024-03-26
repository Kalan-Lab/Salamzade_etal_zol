import os
import sys

with open('Consolidated_Report.tsv') as ocrf:
    for i, line in enumerate(ocrf):
        line = line.strip()
        ls = line.split('\t')
        if i == 0: continue
        ref_in_og = False
        if 'Ref_Epa_from_V583_fai-gene-cluster-1' in line:
            ref_in_og = True
        og = ls[0]
        cons = ls[2]
        print(og + '\t' + cons + '\t' + str(ref_in_og))
