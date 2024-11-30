import os
import sys
from Bio import SeqIO

with open(sys.argv[1]) as of:
    for rec in SeqIO.parse(of, 'fasta'):
        seq = str(rec.seq)
        tot_bp = 0
        gap_bp = 0
        for bp in seq:
            bp = bp.upper()
            tot_bp += 1
            if bp == '-' or bp == 'X':
                gap_bp += 1
        gap_prop = float(gap_bp)/float(tot_bp)
        if gap_prop < 0.20:
            print('>' + rec.description + '\n' + str(rec.seq))
