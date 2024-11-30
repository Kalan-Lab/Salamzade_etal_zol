library(ggplot2)

dat <- read.table('Mini_Heatmap_Data.txt', header=T, sep='\t')

pdf('Mini_Data_HQ.pdf', height=3, width=5)
ggplot(dat, aes(x=method2, y=method1, label=jaccard, fill=jaccard)) + geom_tile(show.legend=F) + geom_text(size=7) + theme_void() + theme(legend.position='top') + scale_fill_gradient(na.value = "white", low='#f2a0b0', high='#c22350', limits=c(0,1)) + scale_y_discrete(limits=rev) 
dev.off()
