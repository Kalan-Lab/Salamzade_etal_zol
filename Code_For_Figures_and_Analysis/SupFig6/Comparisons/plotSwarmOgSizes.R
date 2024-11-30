library(ggplot2)
library(ggbeeswarm)
dat <- read.table("OG_Sizes.txt", header=T, sep='\t')

pdf('OG_Sizes.pdf', height=5, width=15)
# method\tog\tog_lts\tsingle_copy'
ggplot(dat, aes(x=method, y=og_lts, color=single_copy)) + geom_beeswarm(cex=0.5, alpha=1, show.legend=F) + theme_classic(base_size=20) + scale_y_log10() + geom_hline(yintercept=31, linetype=2, color='black') + scale_color_manual(values=c('#eb4034', '#696969')) + xlab("") + ylab("")
dev.off()
