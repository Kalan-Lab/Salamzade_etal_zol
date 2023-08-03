library(gggenes)
library(ggplot2)

colors <- c('#bc76c2', '#DC555E', '#a18560', '#FDBF72', '#FEEDA2', '#F1F9A9', '#BEE5A0', '#78C9A6', '#4796C0', '#6152A4')
names(colors) <- c('EF2167', 'epaX', 'EF2176', 'epaO', 'epaN', 'epaI', 'epaD', 'epaC', 'epaB', 'epaA')

dat <- read.table('plot_input.txt', header=T, sep='\t')

pdf('epa_schematic.pdf', height=3, width=7)
ggplot(dat, aes(xmin = start, xmax = end, y = 'X', fill = label, forward=direction)) +
  geom_gene_arrow() + theme_genes() + 
  scale_fill_manual(values=colors, na.value='#dbdbdb')
dev.off()
