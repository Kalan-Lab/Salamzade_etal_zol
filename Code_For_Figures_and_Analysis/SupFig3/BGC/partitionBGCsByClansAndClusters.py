import os
import sys
from collections import defaultdict

clan_file = 'BiG-SCAPE_Results/network_files/2024-03-10_01-55-22_hybrids_glocal/mix/mix_clustering_c0.30.tsv'
bgc_dir = os.path.abspath('mibig_gbk_3.1') + '/'
gen_cluster_dir = os.path.abspath('Cluster_BGCs/') + '/'

cluster_counts = defaultdict(int)
with open(clan_file) as ocf:
    for i, line in enumerate(ocf):
        if i == 0: continue
        line = line.strip()
        bgc, cluster = line.split('\t')
        cluster_counts[cluster] += 1

with open(clan_file) as ocf:
    for i, line in enumerate(ocf):
        if i == 0: continue
        line = line.strip()
        bgc, cluster = line.split('\t')
        if cluster_counts[cluster] < 2: continue
        clus_dir = gen_cluster_dir + 'GCF_' + cluster + '/'
        if not os.path.isdir(clus_dir):
            os.system('mkdir ' + clus_dir)
        bgc_file = bgc_dir + bgc + '.gbk' 
        assert(os.path.isfile(bgc_file))
        os.system('cp ' + bgc_file + ' ' + clus_dir)
