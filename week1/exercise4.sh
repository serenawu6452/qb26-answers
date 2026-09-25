#!/bin/bash 
384  bedtools intersect -c -a hg19-kc.bed -b snps-chr1.bed | wc -l
  385  bedtools intersect -c -b hg19-kc.bed -a snps-chr1.bed | wc -l
  386  bedtools intersect -c -a hg19-kc.bed -b snps-chr1.bed | sort -k5,5nr | head
#I think ENST00000490107.6_7 in chr1 has the most SNPs probably because its range is long cover from 245912648 to 246670581.  

 387  bedtools sample -i snps-chr1.bed -n 20 -seed 42 | wc -l
  388  bedtools sample -i snps-chr1.bed -n 20 -seed 42 | \\nbedtools sort -i - | \\nbedtools closest -d -t first -a - -b <(bedtools sort -i hg19-kc.bed)
  389  bedtools sample -i snps-chr1.bed -n 20 -seed 42 | \\nbedtools sort -i - | \\nbedtools closest -d -t first -a - -b <(bedtools sort -i hg19-kc.bed) | \\nawk '$NF == 0' | wc -l
# 15 SNPs are inside of a gene.

  390  bedtools sample -i snps-chr1.bed -n 20 -seed 42 | \\nbedtools sort -i - | \\nbedtools closest -d -t first -a - -b <(bedtools sort -i hg19-kc.bed) | \\nawk '$NF > 0 {print $NF}' | sort -n
  391  bedtools sample -i snps-chr1.bed -n 20 -seed 42 | \\nbedtools sort -i - | \\nbedtools closest -d -t first -a - -b <(bedtools sort -i hg19-kc.bed) | \\nawk '$NF > 0 {print $NF}' | sort -n | awk 'NR==1{min=$1} {max=$1} END{print min, max}'
# the range of distances from the ones outside a gene from 1664 to  22944. 
