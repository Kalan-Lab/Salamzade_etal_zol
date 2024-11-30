import os
import sys
from collections import defaultdict

og_list_dir = 'og_listings/'

name = {'zol_default.txt': 'Z1', 'zol_c0i0.txt': 'Z2', 'zol_cdo.txt': 'Z3', 'zol_dom_c0i0.txt': 'Z4', 'orthofinder.txt': 'ZOF'}
print('method\tog\tog_lts\tsingle_copy')
for f in os.listdir(og_list_dir):
    if f in name:
        method = name[f]
        og_lts =  defaultdict(set)
        og_gs = defaultdict(set)
        with open(og_list_dir + f) as of:
            for line in of:
                line = line.strip()
                ls = line.split('\t')
                lt,og,tog = ls
                og_lts[og].add(lt)
                og_gs[og].add(lt.split('_')[0])
        for og in og_lts:
            if len(og_lts[og]) == 1: continue
            single_copy = 'False'
            if len(og_lts[og]) == len(og_gs[og]):
                single_copy = 'True'
            print(method + '\t' + og + '\t' +str(len(og_lts[og])) + '\t' + single_copy)
