#!/usr/bin/env bash

# this is the answers to questions in exercise 3

# 1.1 the A01_09 FASTQ file is 41M, the SAM file is 166M, and the BAM file is 47M. SAM file is bigger than FASTQ file because it is an uncompressed text file. BAM is smaller than SAM file because it stores the alignment info in a compressed binary format which reduces file size. 

#1.2 the third sample in the loop code replaced with its value A01_23
# bwa mem -t 4 -R "@RG\tID:A01_23\tSM:A01_23" ../genomes/sacCer3.fa ~/Data/BYxRM/fastq/A01_23.fq.gz > A01_23.sam

2.1 @SQ show the reference chromosomes and their lengths. There are 17 @SQ lines. 

2.2 The first read is in chromosome I at position 28 with 76M CIGAR string which means 76 bases of the read aligns to the reference genome. 

2.3 for example, the read group A01_09 is shown in the header and at the end of each read as RG::Z:A01_09 and this helps keeping tracking which sample each read came from. 

2.4 100% of the reads mapped to the reference genome and this is probably reasonable because the sample is yeast and it was aligned to yeast again as the reference. 

2.5 Several lines of the output show “0” and this is because the reads were single-end, not pairs end that each read does not have a mate and not properly paired reads to another chromosome. 

2.6 A01_09 A01_24 A01_31 A01_39 A01_62 A01_63 wooer to have less colored regions and BY ancestry. A01_11 A01_23 A01_27 A01_35 appear to have more colored region and have RM ancestry. This agrees with the published genotypes at the four markers. 
