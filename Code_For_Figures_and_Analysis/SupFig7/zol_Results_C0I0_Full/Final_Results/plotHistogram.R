library(ggplot2)

dat <- read.table("Histogram_Data.txt", header=F, sep='\t')

pdf("Conservation_Histogram.pdf", height=3, width=5)

ggplot(dat, aes(x=V2, fill=V3)) + geom_histogram(color='black') + theme_bw() + scale_fill_manual(values=c('#e6ce8c', '#ba952f'))

dev.off()

