import os
import sys

infile = sys.argv[1]

with open(infile) as oif:
    for i, line in enumerate(oif):
        if i == 0: continue
        line = line.strip('\n')
        ls = line.split('\t')
        #if ls[0] != 'OG_33': continue
        genes = set([])
        for gs in ls[1:]:
            for g in gs.split(', '):
                g = g.strip() 
                if g != '':
                    if '|' in g:
                        genes.add(g.split('|')[1])
                    else:
                        genes.add(g)
        for j, g1 in enumerate(sorted(genes)):
            for k, g2 in enumerate(sorted(genes)):
                if j >= k: continue
                print(g1 + '\t' + g2)

