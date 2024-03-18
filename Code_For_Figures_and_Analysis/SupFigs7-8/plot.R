library(ggplot2)

dat <- read.table('Correlation_Data_for_Scatterplot.txt', header=T, sep='\t')
# Dereplication_Type_Comparison	Evolutionary_Statistic	Homolog_Group	Value_1	Value_2

png("Correlation_Between_Dereplication_Methods.png", units='in', res=600, height=10, width=20)
ggplot(dat, aes(x=Value_1, y=Value_2)) + geom_point(alpha=0.7) + facet_wrap(Evolutionary_Statistic~Dereplication_Type_Comparison, scales='free', nrow=5) + geom_abline(slope=1, intercept=0) + theme_bw() + xlab("") + ylab("")
dev.off()
