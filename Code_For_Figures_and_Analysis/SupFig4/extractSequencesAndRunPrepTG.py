import os
import sys
from collections import defaultdict
from Bio import SeqIO

fasta_dir = os.path.abspath('Evolved_FASTAs/') + '/'
with open('epa/genomes_with_ancestral.fa') as oegf:
    for rec in SeqIO.parse(oegf, 'fasta'):
        seq = str(rec.seq).replace('-', '')
        outf = open(fasta_dir + rec.id + '.fasta', 'w')
        outf.write('>' + rec.id + '\n' + seq + '\n')
        outf.close()
        
