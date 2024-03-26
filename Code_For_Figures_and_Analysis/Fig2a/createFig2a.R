library(ggplot2)

dat <- read.table('Plot_Input.txt', header=T, sep='\t')
# JGI GaID	oxygen category	Sample collection date	Depth	Depth_Index	Virunce_Presence

pdf('Plot.pdf', height=3, width=7)
ggplot(dat, aes(x=reorder(Sample.collection.date, date_index), y=reorder(Depth, -Depth_Index), fill=oxygen.category)) + geom_tile(color='white', size=2) + geom_point(aes(color=Virulence_Presence), size=10) + theme_classic() + xlab("Sampling Date") + ylab("Sampling Depth (M)") + scale_fill_manual(values=c('#263d75', '#75aaeb', '#3483e3'), na.value='grey') + scale_color_manual(values=c('#FFFFFF00', '#FFFFFF')) 
dev.off()
