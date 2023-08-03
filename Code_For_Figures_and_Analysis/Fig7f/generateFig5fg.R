library(ggplot2)

dat <- read.table("Conservation_Input.txt", header=T, sep='\t')

pdf("Plot.pdf", height=3, width=2.5)
ggplot(dat, aes(x=species, y=conservation, fill=as.factor(copycount))) + geom_bar(stat='identity', show.legend=F) + theme_classic() + scale_fill_manual(values=c('#919091', '#474747'))
dev.off()
