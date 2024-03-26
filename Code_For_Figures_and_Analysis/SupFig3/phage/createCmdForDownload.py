import os
import sys

accs = []
with open('PhamClust_Table.txt') as opct:
    for i, line in enumerate(opct):
        if i == 0: continue
        line = line.strip()
        ls = line.split('\t')
        accs.append(ls[0])

print('ncbi-acc-download -m nucleotide -F fasta -o All_Genomes.fasta ' + ' '.join(accs))
