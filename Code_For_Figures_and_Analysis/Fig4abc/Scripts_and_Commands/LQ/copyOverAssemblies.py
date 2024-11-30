import os
import sys

reps = set([])
rep_to_species = {}
with open('Worst_Assemblies_per_Species.txt') as orf:
    for line in orf:
        line = line.strip()
        ls = line.split('\t')
        reps.add(ls[1].split('.')[0])
        rep_to_species[ls[1].split('.')[0]] = '_'.join(ls[0].split(';s__')[1].split() + [ls[1].split('.')[0]])

gen_dir = 'Download_All_Genomes/'
res_dir = 'Species_Rep_Genomes/'
for f in os.listdir(gen_dir):
    gca = f.split('.')[0]
    if gca in reps:
        os.system('cp ' + gen_dir + f + ' ' + res_dir + rep_to_species[gca] + '.fasta')
