(qb26) cmdb@QUANTBIO-34 week1 % history | grep bedtools
  311  bedtools intersect -x -a nhlf-active.bed -b nhlf-repressive.bed | wc -l
  312  bedtools intersect -x -a nhlf-active.bed -b nhlf-repressed.bed | wc -l
  313  bedtools intersect -a nhlf-active.bed -b nhlf-repressed.bed | wc -l
  314  bedtools intersect -b nhlf-active.bed -a nhlf-repressed.bed | wc -l
  315  bedtools intersect -v -a nhek-active.bed -b nhlf-active.bed | wc -l
  316  bedtools intersect -a nhek-active.bed -b nhlf-active.bed | wc -l
  317  bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed | wc -l
  318  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 -wa -wb | head -l
  319  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 -wa -wb | head -1
  320  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -F 1 -wa -wb | head -1
  321  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 -F 1 -wa -wb | head -1
  322  bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed | head -1
  323  bedtools intersect -u -a nhek-active.bed -b nhlf-repressed.bed | head -1
  324  bedtools intersect -u -a nhek-repressed.bed -b nhlf-repressed.bed | head -1
