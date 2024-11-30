import os
import sys
from pymsaviz import MsaViz
from Bio import SeqIO
from collections import defaultdict

of_msa_faa = 'OG0000005.msa.fa'

lts = set([])
lt_seq = {}
with open(of_msa_faa) as of:
    for rec in SeqIO.parse(of, 'fasta'):
        lts.add(rec.id)
        lt_seq[rec.id] = str(rec.seq)

default_og_lts = defaultdict(set)
with open('../comparisons/og_listings/zol_default.txt') as of:
    for line in of:
        line = line.strip()
        ls = line.split('\t')
        if ls[0] in lts:
            default_og_lts[ls[1]].add(ls[0])

outf = open('OG0000005.reordered.msa.fa', 'w') 
for og in default_og_lts:
    for lt in default_og_lts[og]:
        outf.write('>' + lt + '|' + og + '\n' + lt_seq[lt] + '\n')
outf.close()

mv = MsaViz('OG0000005.reordered.msa.fa', wrap_length=10000, show_count=False, color_scheme='Flower')
mv.savefig("msa_plot.png")

