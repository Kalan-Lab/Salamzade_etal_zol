library(ggplot2)

dat <- read.table('Search_Data_with_v1.3.20.txt', header=T, sep='\t')

colors <- c('#ABDDA4', '#E6F598', '#F46D43')
names(colors) <- c('cblaster extract_clusters', 'cblaster search', 'fai')

pdf('Search_Data_RR.pdf', height=4, width=5)
ggplot(dat, aes(x=reorder(Method, Ord), y=Value, fill=Category)) + geom_bar(stat='identity', color='#000000') + xlab("") + ylab("Time (in seconds)") + theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1)) + scale_fill_manual(values=colors)
dev.off()



