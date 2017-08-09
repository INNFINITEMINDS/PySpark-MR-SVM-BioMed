# Python-Spark-MapReduce-ML
A compile of Python scripts for applying Spark MapReduce and Machine Learning algorithms. The first application case is a MapReduce framework to compute allele frequencies from a large number of individual VCF files. 

1) sim_vcf.py

Generate a simulated merged vcf file according to number of SNPs and samples. Exponential distribution is used to generate guiding minor allele frequency (MAF) for each SNP. Genotypes are generated according to the MAFs. The SNPs with only one genotype across all samples are not written to the output VCF. 

2) divide_vcf.py

Divide the merged vcf file generated in step 1 into individual vcf files in a specified folder.

3) cal_freq.py

Pyspark code to read in individual vcf files and count the occurrence of any genotype at each SNP locus, and output genotype frequencies according to sorted SNP positions for possible downstream analyses such as computing allele frequencies and discovering rare mutations.
