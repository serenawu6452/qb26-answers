#!/usr/bin/env python3

vcf_file = "variants/biallelic.vcf"

AF_out = open("AF.txt", "w")
gt_out = open("gt_long.txt", "w")

for line in open(vcf_file):

    if line.startswith("#CHROM"):
        fields = line.rstrip("\n").split("\t")
        sample_ids = fields[9:]
        continue

    if line.startswith("#"):
        continue

    fields = line.rstrip("\n").split("\t")

    chrom = fields[0]
    pos = fields[1]

    if chrom == "chrM":
        continue

    info = fields[7]

    for entry in info.split(";"):
        key_value = entry.split("=")

        if key_value[0] == "AF":
            AF_out.write(key_value[1] + "\n")

    for i in range(len(sample_ids)):

        sample = sample_ids[i]
        sample_data = fields[9 + i]

        genotype = sample_data.split(":")[0]

        if genotype == "0" or genotype == "1":
            gt_out.write(sample + "\t" + chrom + "\t" + pos + "\t" + genotype + "\n")

AF_out.close()
gt_out.close()
