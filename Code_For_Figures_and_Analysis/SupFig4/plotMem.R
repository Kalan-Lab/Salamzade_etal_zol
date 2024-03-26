library(ggplot2)

dat <- read.table('Memory_Data.txt', header=T, sep='\t')

pdf('Memory.pdf', height=4, width=4)
ggplot(dat, aes(x=reorder(Method, Ord), y=Value)) + geom_bar(stat='identity', color='#000000', fill='#595959') + xlab("") + ylab("Max Memory (in GB)") + theme(axis.text.x = element_text(angle = 45, vjust = 1, hjust=1))
dev.off()



