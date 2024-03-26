library(ggplot2)

dat <- read.table("zol_memory_and_walltime.txt", header=T, sep='\t')

pdf("zol_memory_and_walltime.pdf", height=7, width=5)

ggplot(dat, aes(x=reorder(Method, Order), y=Count)) + ylab("") + xlab("Method") + geom_bar(stat='identity', color='black', fill='#595959') + facet_wrap(~Statistic, scales='free_y', ncol=1) + theme(axis.text.x = element_text(angle = 60, vjust = 1, hjust=1))

dev.off()
