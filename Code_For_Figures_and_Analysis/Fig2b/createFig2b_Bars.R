# Libraries
library(ggplot2)

dat <- read.table('data.txt', header=T, sep='\t')
# HG      SC      Conservation    MedianLength    Order   Direction       Annotation

p <- ggplot(dat, aes(x=Order, y=Conservation)) + geom_bar(stat='identity', fill='black') +   theme_minimal() +
  theme(
    axis.text = element_blank(),
    axis.title = element_blank(),
    panel.grid = element_blank(),
    plot.margin = unit(rep(-2,4), "cm")     # This remove unnecessary margin around plot
  ) +
  ylim(-10,10) +
  coord_polar(start = 0)
#+ scale_fill_manual(values=c('#c48dd6', '#684773'), na.value='white') +  #+ scale_fill_gradient(low='#c2c1c0', high='#383837')
pdf("plot.pdf", height=10, width=10)
print(p)
dev.off()
