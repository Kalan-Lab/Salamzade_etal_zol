library(ggplot2)
library(gggenes)

args = commandArgs(trailingOnly=TRUE)
input.file <- args[1]
pdf.file <- args[2]

input.data <- read.table("Fig3b_Data.txt", sep='\t', header=T)

pdf("Fig3b.pdf", height=3, width=5)
ggplot(input.data, aes(x=Category, y=Count, fill=as.factor(Clustering))) + geom_bar(stat='identity', color='black', show.legend=F) + theme_classic() + scale_fill_manual(values=c('#818281', '#494a49')) + xlab("") + ylab("") + ylim(0, 220) + geom_hline(yintercept=216, linetype=2, color='#ab1a3e') + geom_hline(yintercept=11, linetype=2, color='#f7658a') + coord_flip()
dev.off()
