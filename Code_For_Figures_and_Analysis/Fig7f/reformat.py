import os
import sys

for line in open('OG_103.tree_leafs.txt'):
    line = line.strip()
    ls = line.split('|')
    print(ls[0].split('_fai-gene-cluster')[0] + '\t' + ls[2])
