library(ggplot2)
library(viridis)

dat <- read.table('Correlation_Data.txt', header=T, sep='\t')
# Dereplication_Type_Comparison   Evolutionary_Statistic  r

pdf("Correlation_Heatmap.pdf", height=7, width=5)
ggplot(dat, aes(x=Dereplication_Type_Comparison, y=reorder(Evolutionary_Statistic, -Statistic_Order), fill=r, label=as.factor(r))) + geom_tile(color='white', linewidth=2) + geom_text(color='white') + scale_fill_viridis(option='magma', direction=-1, limits=c(0,1)) + theme_classic() + theme(axis.text.x = element_text(angle = 45, vjust =1, hjust=1))
dev.off()
