import os
import sys
from Bio import SeqIO

og_list_file = sys.argv[1]
prot_seq_dir = os.path.abspath(sys.argv[2]) + '/'

ogs = set([])
for line in open(og_list_file):
    line = line.strip()
    ogs.add(line)

for f in os.listdir(prot_seq_dir):
    og = f.split('.faa')[0]
    if not og in ogs: continue
    with open(prot_seq_dir + f) as opf:
        for rec in SeqIO.parse(opf, 'fasta'):
            print('>' + og + '|' + rec.id + '\n' + str(rec.seq)) 
