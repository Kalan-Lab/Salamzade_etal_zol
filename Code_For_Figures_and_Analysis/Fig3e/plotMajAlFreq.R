library(ggplot2)

args = commandArgs(trailingOnly=TRUE)

data_file <- args[1]
pdf_file <- args[2]

dat <- read.table(data_file, header=T, sep='\t')

pdf(pdf_file, height=2,width=5)
ggplot(dat, aes(x=MSA_Position, y=Major_Allele_Frequency)) + geom_line() + theme_bw() + xlab("Position in MSA") + ylab("Major Allele\nFrequency")
dev.off()
