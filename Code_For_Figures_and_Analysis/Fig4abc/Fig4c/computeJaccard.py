import os
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

set1 = set([])
for line in open(file1):
    line = line.rstrip('\n').rstrip('\r')
    set1.add(line)

set2 = set([])
for line in open(file2):
    line = line.rstrip('\n').rstrip('\r')
    set2.add(line)

inter = set1.intersection(set2)
union = set1.union(set2)

jaccard = len(inter)/float(len(union))
print(jaccard)
