library(ggplot2)

dat <- read.table('timing_plot.txt', header=T, sep='\t')
pdf('timing.pdf', height=5, width=4)
ggplot(dat, aes(x=reorder(method, order), y=time)) + geom_bar(stat='identity', fill='#232423') + scale_y_log10() + xlab("") + ylab("")
dev.off()
