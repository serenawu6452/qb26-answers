#!/usr/bin/env bash

# this is the answers to questions in exercise 3

# 1.1 the A01_09 FASTQ file is 41M, the SAM file is 166M, and the BAM file is 47M. SAM file is bigger than FASTQ file because it is an uncompressed text file. BAM is smaller than SAM file because it stores the alignment info in a compressed binary format which reduces file size. 

#1.2 the third sample in the loop code replaced with its value A01_23
# bwa mem -t 4 -R "@RG\tID:A01_23\tSM:A01_23" ../genomes/sacCer3.fa ~/Data/BYxRM/fastq/A01_23.fq.gz > A01_23.sam

