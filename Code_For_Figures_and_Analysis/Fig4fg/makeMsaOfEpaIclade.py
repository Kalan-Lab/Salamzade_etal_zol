from pymsaviz import MsaViz, get_msa_testdata
from Bio import SeqIO

msa_file = "epaI_Clade_Con_Seqs_of_OGs.msa.faa"

epaI = ''
OG140 = ''
others = []
with open(msa_file) as omf:
    for rec in SeqIO.parse(omf, 'fasta'):
        if rec.id == 'epaI':
            epaI = str(rec.seq)
        elif rec.id == 'OG_140':
            OG140 = str(rec.seq)
        else:
            others.append(str(rec.seq))

uniq_count = 0
cons_count = 0
conserved_epaI_and_OG140 = []
for i, epaI_bp in enumerate(epaI):
    OG140_bp = OG140[i]
    if epaI_bp != '-' and epaI_bp == OG140_bp:
        conserved_epaI_and_OG140.append(i+1)
        uniq = True
        for oth_seq in others:
            oth_seq_bp = oth_seq[i]
            if oth_seq_bp == epaI_bp:
                uniq = False
        if uniq:
            uniq_count += 1
        else:
            cons_count += 1

print(uniq_count)
print(cons_count+uniq_count)
print(uniq_count/(uniq_count+cons_count))
mv = MsaViz(msa_file, wrap_length=60, show_count=True, color_scheme="Flower")
mv.set_highlight_pos(conserved_epaI_and_OG140)
#mv.set_highlight_pos_by_ident_thr(min_thr=75, max_thr=100)
mv.savefig("epaI_Clade_Consensus_Seqs_MSA.png")
