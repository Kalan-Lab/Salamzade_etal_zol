import os
import sys
from collections import defaultdict

check_dir = os.path.abspath(sys.argv[1]) + '/'

with open('PopB_GCs.txt') as opf:
    for line in opf:
        line = line.strip()
        assert(os.path.isfile(check_dir + line))
