library(ggplot2)


dat <- read.table('Major_Allele_Freqs.txt', header=T, sep='\t')
dat2 <- read.table('Neg_Selected_Sites.txt', header=T, sep='\t')

pdf('Plot.pdf', height=3,width=7)
ggplot(dat, aes(x=MSA_Position, y=Major_Allele_Frequency)) + geom_segment(data=dat2, aes(x=x, y=y, xend=xend, yend=yend), color='#f5a59a') + geom_line(color='black') + theme_bw() + xlab("Position in MSA") + ylab("") 
dev.off()
