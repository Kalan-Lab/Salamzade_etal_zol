import os
import sys
from ete3 import Tree

t = Tree(sys.argv[1])

print('DATASET_COLORSTRIP')
print('SEPARATOR TAB')
print('DATASET_LABEL\tspecies_track')
print('COLOR\t#000000')
print('DATA')
for node in t.traverse('postorder'):
    if not node.is_leaf(): continue
    printlist = [node.name]
    if 'faecium' in node.name.split('|')[-1]:
        printlist.append('#BF9000')
        printlist.append('E. faecium')
    elif 'faecalis' in node.name.split('|')[-1]:
        printlist.append('#0070C0')
        printlist.append('E. faecalis')
    print('\t'.join(printlist))
