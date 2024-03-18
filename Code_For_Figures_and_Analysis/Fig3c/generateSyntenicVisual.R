library(ggplot2)
library(gggenes)

args = commandArgs(trailingOnly=TRUE)
input.file <- args[1]
height <- 3 #as.numeric(args[2])
width <- 7 #as.numeric(args[3])
pdf.file <- args[2]

input.data <- read.table(file=input.file, sep='\t', header=T)
# 	pif_handle.write('\t'.join(['HG', 'Start', 'End', 'Direction', 'SC', 'Metric']) + '\n')

pdf(pdf.file, height=height, width=width)
ggplot(input.data, aes(xmin=Start, xmax = End, y = "", forward = Direction, label=SC)) +
  geom_gene_arrow(aes(fill=Metric)) + theme_classic() +
  scale_fill_gradient(low='#f2c233', high='#5a3263', breaks =c(0.0, 0.25, 0.5, 0.75, 1.0),
                      labels=c("0.00", "", "0.50", "", "1.00"), limits=c(0,1), na.value='grey50', guide='colourbar',
                      aesthetics='fill') +
  geom_gene_label(align='centre', min.size=5) + theme(legend.position="bottom")
dev.off()
