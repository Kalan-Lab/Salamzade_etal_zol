import os
import sys

indir = os.path.abspath(sys.argv[1]) + '/'

print('Cluster_ID\tStatistic\tValue')
for clust in os.listdir(indir):
    stats_file = indir + clust + '/Parameter_Recommendations_for_fai.txt'
    if not os.path.isfile(stats_file): continue
    with open(stats_file) as osf:
        for i, line in enumerate(osf):
            line = line.strip()
            ls = line.split('\t')
            if i >= 8 and i <= 12:
                print('\t'.join([clust, ls[0], ls[1]]))

