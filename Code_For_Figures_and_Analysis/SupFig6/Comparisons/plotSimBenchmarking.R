library(ggplot2)

dat <- read.table("Comparison_Counts.txt", header=T, sep='\t') 

pdf("Simulation_Based_Comparisons.pdf", height=3, width=5.5)
ggplot(dat, aes(x=reorder(Method, Order), y=Count)) + geom_bar(stat='identity', color='black', fill='#595959') + facet_wrap(~Statistic, scales='free', nrow=1) + xlab("Method")
dev.off()
