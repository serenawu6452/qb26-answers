crossovers <- read.table("crossovers.txt")
colnames(crossovers) <- c("sample", "crossovers")

png("crossovers.png")

hist(crossovers$crossovers,
     xlab = "Number of crossovers",
     main = "Crossovers per segregant")

dev.off()

