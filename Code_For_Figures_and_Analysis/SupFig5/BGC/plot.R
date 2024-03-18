library(ggplot2)

dat <- read.table("MIBiG-BiG-SCAPE_Statistic_Values.Transformed.txt", header=T, sep='\t')

pdf("MIBiG-BiG-SCAPE_Statistic_Values.Transformed.pdf", height=7, width=3)
ggplot(dat, aes(x=Value)) + geom_histogram(color='black') + theme_bw() + facet_wrap(~Statistic, ncol=1, labeller=label_wrap_gen(), scales='free')
dev.off()
