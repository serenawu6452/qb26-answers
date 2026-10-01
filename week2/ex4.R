setwd("/Users/cmdb/qb26-answers/week2")

library(ggplot2)

af <- read.table("AF.txt", header = FALSE)
colnames(af) <- "AF"

ggplot(af, aes(x = AF)) +
  geom_histogram(bins = 11) +
  labs(
    x = "Allele Frequency",
    y = "Count",
    title = "Allele Frequency Spectrum"
  )

ggsave("AF.png")
getwd()

gt <- read.table("gt_long.txt", header = FALSE)
colnames(gt) <- c("sample", "chrom", "pos", "genotype")

gt$genotype <- as.factor(gt$genotype)

chrII_A01_62 <- subset(gt, sample == "A01_62" & chrom == "chrII")

p2 <- ggplot(chrII_A01_62,
             aes(x = pos, y = sample, color = genotype)) +
  geom_point() +
  labs(
    x = "Position",
    y = "Sample",
    color = "Genotype",
    title = "A01_62 chrII"
  )

p2

# exercise 4.5

A01_62 <- subset(gt, sample == "A01_62")

A3 <- ggplot(A01_62,
             aes(x = pos, y = sample, color = genotype)) +
  geom_point(size = 0.5) +
  facet_grid(. ~ chrom,
             scales = "free_x",
             space = "free_x") +
  labs(
    x = "Position",
    y = "Sample",
    color = "Genotype"
  )

A3

# 4.5 all 10 samples

A4 <- ggplot(gt,
             aes(x = pos, y = sample, color = genotype)) +
  geom_point(size = 0.5) +
  facet_grid(. ~ chrom,
             scales = "free_x",
             space = "free_x") +
  labs(
    x = "Position",
    y = "Sample",
    color = "Genotype"
  )

A4
ggsave("ancestry.png")
