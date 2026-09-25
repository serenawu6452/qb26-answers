(qb26) cmdb@QUANTBIO-34 week1 % history | grep bedtools
  311  bedtools intersect -x -a nhlf-active.bed -b nhlf-repressive.bed | wc -l
  312  bedtools intersect -x -a nhlf-active.bed -b nhlf-repressed.bed | wc -l
  313  bedtools intersect -a nhlf-active.bed -b nhlf-repressed.bed | wc -l
  314  bedtools intersect -b nhlf-active.bed -a nhlf-repressed.bed | wc -l
  315  bedtools intersect -v -a nhek-active.bed -b nhlf-active.bed | wc -l
  316  bedtools intersect -a nhek-active.bed -b nhlf-active.bed | wc -l
  317  bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed | wc -l
# there are 12174 regions that are active in NHEK and NHLF, and 2405 regions that are active in NHEK but not active in NHLF. But 12174 + 2405 = 14579 which does not match the total number of 14013. To address this problem, we change --v to -u to only report one feature per overlap. This  give us new output number 11608 which add up and can equal to 14013. 

 318  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 -wa -wb | head -l
  319  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 -wa -wb | head -1
  320  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -F 1 -wa -wb | head -1
  321  bedtools intersect -a nhek-active.bed -b nhlf-active.bed -f 1 -F 1 -wa -wb | head -1
#for the overlap options, -f 1 means all of the NHEK region has to overlap, -F 1 means all of the NHLF region has to overlap, and -f 1 -F 1 means both regions have to fully overlap.

  322  bedtools intersect -u -a nhek-active.bed -b nhlf-active.bed | head -1
  323  bedtools intersect -u -a nhek-active.bed -b nhlf-repressed.bed | head -1
  324  bedtools intersect -u -a nhek-repressed.bed -b nhlf-repressed.bed | head -1
#the active-active region showed many active promoter and enhancer; the active-repressed region showed NHEK as active and NHLF as repressed, and the repressed-repressed region showed both NHEK and NHLF as repressed. the same region can have different chromatin states in different cell type
