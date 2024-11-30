import os
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]
comp = sys.argv[3]

set1 = set([])
for line in open(file1):
    line = line.rstrip('\n').rstrip('\r')
    set1.add(line)

set2 = set([])
for line in open(file2):
    line = line.rstrip('\n').rstrip('\r')
    set2.add(line)

if comp == 'symmetric':
    print('\n'.join(sorted(set1.symmetric_difference(set2))))
elif comp == 'intersect' or comp == 'intersection':
    print('\n'.join(sorted(set1.intersection(set2))))
elif comp == 'difference':
    print('\n'.join(sorted(set1.difference(set2))))
elif comp == 'union' or comp == 'join':
    print('\n'.join(sorted(set1.union(set2))))
elif comp == 'opp_difference':
    print('\n'.join(sorted(set2.difference(set1))))
