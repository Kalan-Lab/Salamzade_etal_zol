import os
import sys
from ete3 import Tree

map_file = sys.argv[1]
tree_file = sys.argv[2]

gene = {}
color = {}
with open(map_file) as omf:
    for line in omf:
        line = line.strip()
        ls = line.split('\t')
        if ls[0] == 'NA': continue
        gene[ls[0]] = ls[1]
        color[ls[0]] = ls[2]

t = Tree(tree_file)

print('DATASET_COLORSTRIP')
print('SEPARATOR TAB')
print('DATASET_LABEL\tepaName')
print('COLOR\t#000000')
print('DATA')
for leaf in t.traverse('postorder'):
    if leaf.is_leaf:
        og = leaf.name.split('|')[0]
        if og in color:
            print(leaf.name + '\t' + color[og] + '\t' + gene[og])
