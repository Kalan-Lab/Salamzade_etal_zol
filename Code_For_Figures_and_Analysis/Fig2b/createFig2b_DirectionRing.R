# Libraries
library(ggplot2)

dat <- read.table('data.txt', header=T, sep='\t')
# HG      SC      Conservation    MedianLength    Order   Direction       Annotation

dat$MedianLength <- dat$MedianLength

p <- ggplot(dat, aes(x=Order, y=100, fill=Direction)) + geom_bar(stat='identity') +   theme_minimal() +
  theme(
    axis.text = element_blank(),
    axis.title = element_blank(),
    panel.grid = element_blank(),
    plot.margin = unit(rep(-2,4), "cm")     # This remove unnecessary margin around plot
  ) +
  ylim(-2000, 2300) +
  coord_polar(start = 0) + scale_fill_manual(values=c('#c48dd6', '#684773'), na.value='white')
pdf("plot_dir.pdf", height=10, width=10)
print(p)
dev.off()
