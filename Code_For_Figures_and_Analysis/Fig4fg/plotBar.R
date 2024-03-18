library(ggplot2)

dat <- read.table("Barchart_input.txt", header=T, sep='\t')

colors <- c('#0070C0', '#BF9000', '#FF0000', '#00B050', '#878a88')
names(colors) <- c('Clade_I', 'Clade_II', 'Clade_III', 'Clade_IV', 'Other')
pdf("GT_OG_Barplot.pdf", height=7, width=10)
ggplot(dat, aes(x=reorder(OG, Total_Count), y=Count, fill=Clade)) + geom_bar(color='black', stat='identity') + coord_flip() + theme_classic() + xlab("") + ylab("") + scale_fill_manual(values=colors) + theme(text = element_text(size = 20)) 
dev.off()
