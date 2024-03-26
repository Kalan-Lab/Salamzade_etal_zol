library(ggplot2)

dat <- read.table('Plotting_Input.txt', header=T, sep='\t')

annot.colors <- c('#c21938', '#e34b67', '#6ea6d4', '#8fb9db', '#3b77a8')
names(annot.colors) <- c('Critical for BGC expression', 'KO prevents production of any leporin metabolites', 'KO only prevents production of leporin A', 'KO only prevents production of leporin A & B', 'Non-essential for BGC expression')
pdf('Plotting_Input.pdf', height=4, width=8)
ggplot(dat, aes(x=reorder(GeneName, Upstream_Entropy), y=Upstream_Entropy, fill=Importance)) + geom_bar(stat='identity', color='black') + scale_fill_manual(values=annot.colors) + theme_classic() + theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) + xlab("") + ylab("")
dev.off()
