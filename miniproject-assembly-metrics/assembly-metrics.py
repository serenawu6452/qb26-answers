#!/usr/bin/env python3

import sys
import fasta

file = open( sys.argv[1] )
genomes = fasta.FASTAReader( file )

count = 0
total_length = 0
for ident, sequence in genomes:
    count = count +1 
    total_length += len(sequence)
average_length = total_length / count 

print (count, total_length, average_length)
file.close()
