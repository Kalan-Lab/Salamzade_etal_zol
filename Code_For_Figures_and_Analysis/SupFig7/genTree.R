library(ape)

rt <- rtree(30, rooted=F, min=0.01, max=0.15)

write.tree(rt, file='rtree_n100.tre')
