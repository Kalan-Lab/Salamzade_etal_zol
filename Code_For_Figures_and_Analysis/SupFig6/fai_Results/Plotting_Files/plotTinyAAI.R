library(ggplot2)
library(gridExtra)
info.file <- "/workspace/local/rauf/zol/update_manuscript_apps/Enterococcus_Epa/Comparisons/CoreSimul/fai_Results/Plotting_Files/Tiny_AAI_Plot_Data.txt"
pdf_file <- "/workspace/local/rauf/zol/update_manuscript_apps/Enterococcus_Epa/Comparisons/CoreSimul/fai_Results/Final_Results/Candidate_Homologous_Gene_Clusters.Tiny_AAI_Plot.pdf"

info.dat <- read.table(info.file, header=T, sep="\t")

pdf(pdf_file, height=10, width=10)
ggplot(info.dat, aes(x=AAI, y=Prop_Genes_Found, color=Mean_Syntenic_Correlation)) + 
geom_point(alpha=0.7) + theme_bw() + scale_color_gradient(low="#e6ffbd", high="#1754b0") + 
guides(color=guide_legend("Syntenic
Correlation
to
Query")) + 
xlab("Average Amino-Acid Identity") + ylab("Proportion of Query Proteins with Match")
dev.off()
