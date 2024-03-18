import os
import sys
from Bio import SeqIO

phage_gbk_dir = os.path.abspath('prepTG_Phage_Genomes/Genomic_Genbanks_Additional/') + '/'
phage_clusters_dir = os.path.abspath('Phage_Clusters') + '/'

with open('PhamClust_Table.txt') as opt:
    for i, line in enumerate(opt):
        if i == 0: continue
        line = line.strip()
        ls = line.split('\t')
        phage = ls[0]
        cluster = ls[2]
        phage_file = phage_gbk_dir + phage + '.gbk'
        print(phage_file)
        assert(os.path.isfile(phage_file))
        cluster_dir = phage_clusters_dir + 'PhamClust_' + cluster + '/'
        if not os.path.isdir(cluster_dir):
            os.system('mkdir ' + cluster_dir)
        os.system('cp ' + phage_file + ' ' + cluster_dir)
