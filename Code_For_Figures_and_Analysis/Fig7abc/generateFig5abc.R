library(ggplot2)
library(gggenes)
library(cowplot)

cons.data <- read.table("Conservation_Track.txt", sep='\t', header=T)
tajd.data <- read.table("Tajimas_D_Track.txt", sep='\t', header=T)
entr.data <- read.table("Entropy_Track.txt", sep='\t', header=T)

# 	pif_handle.write('\t'.join(['HG', 'Start', 'End', 'Direction', 'SC', 'Metric']) + '\n')



pdf("Fig5abc.pdf", height=10, width=10)
g1 <- ggplot(cons.data, aes(xmin=Start, xmax = End, y = "", forward = Direction, label=SC)) +
  geom_gene_arrow(aes(fill=Metric)) + theme_void() +
  scale_fill_gradient(low='#FFFFFF', high='#000000', breaks =c(0.00, 0.25, 0.50, 0.75, 1.00),
                      labels=c("0.00", "0.25", "0.50", "0.75", "1.00"), limits=c(0,1), na.value='red', guide='colourbar',
                      aesthetics='fill') + theme(legend.position='bottom') + 
  geom_gene_label(align='centre', min.size=5) 

g2 <- ggplot(tajd.data, aes(xmin=Start, xmax=End, ymin=0, ymax=1, fill=Metric)) + geom_rect(show.legend=F) + theme_void() + 
       scale_fill_gradient2(low='#e05c74', mid="#f2f2f2", high='#2087b3', breaks =c(-3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0),
                      labels=c("", "-2", "", "0", "", "2", ""), limits=c(-3,3), na.value='grey50', guide='colourbar',
                      aesthetics='fill') 	


g3 <- ggplot(entr.data, aes(xmin=Start, xmax=End, ymin=0, ymax=1, fill=Metric)) + geom_rect() + theme_void() +
       scale_fill_gradient(low='#c5debf', high='#298a12', breaks =c(0.00, 0.05, 0.10, 0.15, 0.2),
                      labels=c("0.00", "0.05", "0.10", "0.15", "0.20"), limits=c(0,0.2), na.value='grey50', guide='colourbar',
                      aesthetics='fill') + theme(legend.position="bottom")
plot_grid(g1, g2, g3, rel_heights=c(2, 0.1, 0.22), align='v', axis='lr', ncol=1)

dev.off()
