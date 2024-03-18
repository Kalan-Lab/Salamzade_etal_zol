import os
import sys
from collections import defaultdict

best_gca_for_species = defaultdict(lambda: [None, 0])
with open('bac120_metadata_r207.tsv') as obf:
    for i, line in enumerate(obf):
        if i == 0: continue
        line = line.strip('\n')
        ls = line.split('\t')
        tax = ls[16]
        if not ';g__Enterococcus' in tax: continue
        scaff_n50 = int(ls[44])
        gca = ls[54]
        if best_gca_for_species[tax][1] < scaff_n50:
            best_gca_for_species[tax] = [gca, scaff_n50]

for sp in best_gca_for_species:
    print(sp + '\t' + str(best_gca_for_species[sp][0]) + '\t' + str(best_gca_for_species[sp][1]))
