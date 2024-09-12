import os
import sys

valid_lt = set([])
with open('True_Orthologs_based_on_Fai.txt') as olf:
    for line in olf:
        line = line.strip()
        ls = line.split('\t')
        valid_lt.add(ls[0])
        valid_lt.add(ls[1])

with open(sys.argv[1]) as of:
    for line in of:
        line = line.strip()
        ls = line.split('\t')
        if ls[0] in valid_lt and ls[1] in valid_lt:
            print(line)
