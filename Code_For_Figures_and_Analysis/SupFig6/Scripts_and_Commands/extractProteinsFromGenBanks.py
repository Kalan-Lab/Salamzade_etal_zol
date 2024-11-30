import os
import sys
from Bio import SeqIO

gbk_dir = os.path.abspath(sys.argv[1]) + '/'
faa_dir = os.path.abspath(sys.argv[2]) + '/'

for f in os.listdir(gbk_dir):
    gbk_file = gbk_dir + f
    outf = open(faa_dir + '.gbk'.join(f.split('.gbk')[:-1]) + '.faa', 'w')
    with open(gbk_file) as ogbf:
        for rec in SeqIO.parse(ogbf, 'genbank'):
            for feat in rec.features:
                if not feat.type == 'CDS': continue
                outf.write('>' + feat.qualifiers.get('locus_tag')[0] + '\n' + str(feat.qualifiers.get('translation')[0]) + '\n')
    outf.close()
