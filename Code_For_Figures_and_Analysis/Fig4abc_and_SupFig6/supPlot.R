library(ggplot2)
library(cowplot)

timedat <- read.table("timing_data_for_hq.txt", header=T, sep='\t')
memdat <- read.table("max_memory_for_hq.txt", header=T, sep='\t')
dudat <- read.table("final_diskspace_usage.txt", header=T, sep='\t')

pdf("SupFigures.pdf", height=3, width=10)
g1 <- ggplot(timedat, aes(x=reorder(Method, Order), y=Time, fill=Step)) + geom_bar(stat='identity', color='#000000', position = position_fill(reverse = TRUE)) + scale_fill_brewer(palette='Spectral') + xlab("") + ylab("Relative time required")
g2 <- ggplot(memdat, aes(x=reorder(Method, Order), y=Memory)) + geom_bar(stat='identity', color='#000000', fill='#595959') + xlab("") + ylab("Memory (in GB)")
g3 <- ggplot(dudat, aes(x=reorder(Method, Order), y=DiskUsage)) + geom_bar(stat='identity', color='#000000', fill='#595959') + xlab("") + ylab("Disk usage (in MB)") 

plot_grid(g1, g2, g3, nrow=1, rel_widths=c(5, 3, 3), align='h')
dev.off()
