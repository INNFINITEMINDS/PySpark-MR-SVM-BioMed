# Python-Spark-MapReduce-ML
A compile of Python scripts for applying Spark MapReduce and Machine Learning algorithms. The first application case is a MapReduce framework to compute allele frequencies from a large number of individual VCF files. 

1) sim_vcf.py

Generate a bunch of simulated vcf files, according to number of SNPs and samples. Exponential distribution is used to generate guiding minor allele frequency for each SNP. The SNPs with only one genotype across all samples are not written to the output. 
