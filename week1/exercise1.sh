(qb26) cmdb@QUANTBIO-34 week1 % history | grep hg19
  316  bedtools intersect -c -a hg19-kc.bed -b hg19-1mb.bed
  317  bedtools intersect -c -a hg19-kc.bed -b hg19-1mb.bed | wc -l
  318  wc -l hg19-kc.bed
  319  wc -l hg19-1mb.bed
  320  bedtools intersect -c -b hg19-kc.bed -a hg19-1mb.bed | wc -l
  321  bedtools intersect -c -b hg19-kc.bed -a hg19-1mb.bed | head
  323  bedtools intersect -c -b hg19-kc.bed -a hg19-1mb.bed >  hg19-kc-count.be
  326  bedtools intersect -c -b hg19-kc.bed -a hg19-1mb.bed >  hg19-kc-count.bed
  328  rm hg19-kc-count.be


