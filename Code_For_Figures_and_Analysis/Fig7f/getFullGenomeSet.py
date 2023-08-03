import os
import sys
from ete3 import Tree

species_listing = '/home/salamzade/Other/Enterococcus_lsaBGC/Download_Genomes/Enterococcus_Genomes.txt'

gca_to_sp = {}
with open(species_listing) as osl:
    for line in osl:
        line = line.strip()
        ls = line.split('\t')
        gca = ls[6]
        sp = ls[3]
        gca_to_sp[gca] = sp

pdir = '../../zol_Efaecium_and_Efaecalis_reinflated/CDS_Protein/'
for f in os.listdir(pdir):
    g = f.split('_fai-gene-cluster')[0]
    gca = '_'.join(g.split('_')[:2]).replace('GCF_', 'GCA_')
    if gca_to_sp[gca] == 'Enterococcus_B_faecium':
        print(g)
