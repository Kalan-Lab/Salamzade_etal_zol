import os
import sys
from Bio import SeqIO
from collections import defaultdict
from operator import itemgetter

msa_file = sys.argv[1]

seqs = []
with open(msa_file) as omf:
    for rec in SeqIO.parse(omf, 'fasta'):
        seqs.append(list(str(rec.seq).upper()))

print('MSA_Position\tMajor_Allele_Frequency')
for pos, alstup in enumerate(zip(*seqs)):
    als = list(alstup)
    al_counts = defaultdict(int)
    nongap_als = 0
    for al in als:
        if al in set(['A', 'C', 'G', 'T']):
            al_counts[al] += 1
            nongap_als += 1
    for i, al in enumerate(sorted(al_counts.items(), key=itemgetter(1), reverse=True)):
        if i == 0:
            major_al_freq = al[1]/float(nongap_als)
    print(str(pos+1) + '\t' + str(major_al_freq))
