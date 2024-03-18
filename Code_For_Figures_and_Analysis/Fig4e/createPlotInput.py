import os
import sys

with open('T00123.kff') as of:
    for i, line in enumerate(of):
        if i >= 2123 and i <= 2159:
            line = line.strip()
            ls = line.split('\t')
            ef = ls[0].split(':')[1]
            coords = ls[4]
            direction = 0
            if '(' in coords:
                start = coords.split('..')[0].split('(')[1]
                end = coords.split('..')[1].split(')')[0]
                direction = 1
            else:
                start = coords.split('..')[0]
                end = coords.split('..')[1]
            print(ef + '\t' + str(start) + '\t' + str(end) + '\t' + str(direction))
