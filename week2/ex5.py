#!/usr/bin/env python3

samples = []

for line in open("gt_long.txt"):
    sample = line.split()[0]
    if sample not in samples:
        samples.append(sample)


out = open("crossovers.txt", "w")

for sample in samples:

    crossovers = 0
    current = None
    candidate = None
    count = 0
    last_chr = None

    for line in open("gt_long.txt"):
        s, chrom, pos, gt = line.split()

        if s != sample:
            continue

        if chrom != last_chr:
            last_chr = chrom
            current = gt
            candidate = None
            count = 0
            continue

        if gt == current:
            candidate = None
            count = 0

        # possible ancestry switch
        else:
            if gt == candidate:
                count += 1
            else:
                candidate = gt
                count = 1

            if count == 5:
                crossovers += 1
                current = candidate
                candidate = None
                count = 0

    out.write(sample + "\t" + str(crossovers) + "\n")

out.close()

