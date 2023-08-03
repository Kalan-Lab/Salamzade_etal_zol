library(ggplot2)
library(gggenes)

args = commandArgs(trailingOnly=TRUE)

input.data <- read.table("Data.txt", sep='\t', header=T)

pdf("Fig3b.pdf", height=3, width=5)
ggplot(input.data, aes(x=Category, y=Count, fill=Category)) + geom_bar(stat='identity', position='dodge', color='black', show.legend=F) + theme_classic() + scale_fill_brewer(palette='set2') + xlab("") + ylab("") + ylim(0, 220) + geom_hline(yintercept=216, linetype=2, color='red')
dev.off()
