library(ggplot2)
library(cowplot)

fulltime <- read.table("full_timing_for_hq.txt", header=T, sep='\t')
hqdat <- read.table("HQ_Counts.txt", header=T, sep='\t')
lqdat <- read.table("LQ_Counts.txt", header=T, sep='\t')

pdf("fig4_bench.pdf", height=3, width=10)

g1 <- ggplot(fulltime, aes(x=reorder(Method, Order), y=Time)) + geom_bar(stat='identity', color='#000000', fill='#595959') + scale_y_log10() + xlab("") + ylab("Time (in seconds)")
g2 <- ggplot(hqdat, aes(x=reorder(Category, Order), y=Count)) + geom_bar(stat='identity', color='#000000', fill='#595959') + scale_y_log10() + xlab("") + ylab("Ortholog group\npairs shared")  + theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))
g3 <- ggplot(lqdat, aes(x=reorder(Category, Order), y=Count)) + geom_bar(stat='identity', color='#000000', fill='#595959') + scale_y_log10() + xlab("") + ylab("Ortholog group\npairs shared") + theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))

plot_grid(g1, g2, g3, nrow=1, align='h')
dev.off()
