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

tre = sys.argv[1]

t = Tree(tre)
for node in t.traverse('postorder'):
    if not node.is_leaf(): continue
    gca = '_'.join(node.name.split('_')[:2])
    node.name = node.name + '|' + gca_to_sp[gca]

t.write(format=1, outfile=sys.argv[2])
