library(tidyverse)
search()
header <- c("chr", "start", "end", "count")
df_kc <- read_tsv("hg19-kc-count.bed", col_names = header)
setwd("/Users/cmdb/qb26-answers/week1") 
ggplot(df_kc, aes(x = start, y = count)) +
  geom_line() +
  facet_wrap(~chr, scales = "free")
  ggsave( "exercise1.png" )
  