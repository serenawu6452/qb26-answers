#!/bin/bash

268  bedtools intersect -c -a hg16-kc.bed -b hg16-1mb.bed | wc -l
  269  bedtools intersect -c -b hg16-kc.bed -a hg16-1mb.bed | wc -l
  270  bedtools intersect -c -b hg16-kc.bed -a hg16-1mb.bed | head
  271  bedtools intersect -c -b hg16-kc.bed -a hg16-1mb.bed > hg16-kc-count.bed
  272  ls -l
  273  wc -l hg19-kc.bed
  274  bedtools intersect -v -b hg16-kc.bed -a hg19-1mb.bed | wc -l
  275  wc -l hg16-kc.bed
  276  bedtools intersect -v -b hg19-kc.bed -a hg16-1mb.bed | wc -l
  277  ls -l
 
# there are 80309 genes in hg19. 467 genes are in hg19 but not in hg16 and this is can due to improvement in technology discovering more genome information that add or update the previous genome information. 
# there are 21365 genes in hg16. 200 genes are in hg16 but not in hg19 and this can be because of updating genome annotation between the two version of genome. 
