# Libraries
library(ggplot2)

dat <- read.table('Data.txt', header=T, sep='\t')
# HG      SC      Conservation    MedianLength    Order   Direction       Annotation

dat$MedianLength <- dat$MedianLength

p <- ggplot(dat, aes(x=Order, y=MedianLength, fill=Conservation)) + geom_bar(stat='identity') +   theme_minimal() +
  theme(
    axis.text = element_blank(),
    axis.title = element_blank(),
    panel.grid = element_blank(),
    plot.margin = unit(rep(-2,4), "cm")     # This remove unnecessary margin around plot
  ) +
  ylim(-2000, 2300) +
  coord_polar(start = 0) +  scale_fill_gradient(low='#c2c1c0', high='#383837')
pdf("plot.pdf", height=10, width=10)
print(p)
dev.off()
