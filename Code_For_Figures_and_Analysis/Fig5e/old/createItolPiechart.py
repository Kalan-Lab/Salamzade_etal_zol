import os
import sys
from collections import defaultdict
from ete3 import Tree

og_cats_file = sys.argv[1]
t = Tree(sys.argv[2])

names = []
colors = []
og_to_name = {}
with open(og_cats_file) as ocf:
    for line in ocf:
        line = line.strip()
        if line.startswith('#'): continue
        ls = line.split('\t')
        names.append(ls[1])
        colors.append(ls[2])
        og_to_name[ls[0]] = ls[1]

print('DATASET_PIECHART')
print('SEPARATOR TAB')
print('DATASET_LABEL\tZol OGs')
print('COLOR\t#000000')
print('FIELD_LABELS\t' + '\t'.join(names))
print('FIELD_COLORS\t' + '\t'.join(colors))
print('DATA')

for node in t.traverse('postorder'):
    if node.is_leaf():
        og = node.name.split('|')[0]
        printlist = [node.name, '1', '1']
        flag = False
        for n in names:
            if og in og_to_name and og_to_name[og] == n:
                printlist.append('1')
                flag = True
            else:
                printlist.append('0')
        if flag:
            print('\t'.join(printlist))
