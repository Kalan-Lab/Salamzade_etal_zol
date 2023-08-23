library(ggplot2)

dat <- read.table('Plotting_Input.txt', header=T, sep='\t')
# Dereplication_Type_Comparison	Evolutionary_Statistic	Homolog_Group	Value_1	Value_2

pdf("Correlation_Between_Dereplication_Methods.pdf", height=10, width=20)
ggplot(dat, aes(x=Value_1, y=Value_2)) + geom_point(alpha=0.7) + facet_wrap(Evolutionary_Statistic~Dereplication_Type_Comparison, scales='free', nrow=5) + geom_abline(slope=1, intercept=0) + theme_bw() + xlab("") + ylab("")# + scale_x_log10() + scale_y_log10()
dev.off()
