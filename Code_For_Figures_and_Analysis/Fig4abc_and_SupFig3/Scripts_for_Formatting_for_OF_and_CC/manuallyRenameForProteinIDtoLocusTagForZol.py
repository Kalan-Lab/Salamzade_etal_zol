import os
import sys
from Bio import SeqIO
import copy
from collections import defaultdict

cblaster_gbk_dir = os.path.abspath(sys.argv[1]) + '/'
updated_gbk_dir = os.path.abspath(sys.argv[2]) + '/'

sp_gbks = defaultdict(set)
for f in os.listdir(cblaster_gbk_dir):
    og_gbk = cblaster_gbk_dir + f
    sp = None
    with open(og_gbk) as ogg:
        for rec in SeqIO.parse(ogg, 'genbank'):
           sp = rec.description.split('species ')[1]
    sp_gbks[sp].add(og_gbk)

for sp in sp_gbks:
    up_gbk = open(updated_gbk_dir + sp + '.gbk', 'w')
    for og_gbk in sp_gbks[sp]:
        with open(og_gbk) as ogg:
            for rec in SeqIO.parse(ogg, 'genbank'):
                up_rec = copy.deepcopy(rec)
                for feat in up_rec.features:
                    if feat.type == 'CDS':
                        protein_id = feat.qualifiers.get('protein_id')[0]
                        feat.qualifiers['locus_tag'] = protein_id
            SeqIO.write(up_rec, up_gbk, 'genbank')
    up_gbk.close()
