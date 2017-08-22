# Python-Spark-MapReduce-ML
A compile of Python scripts for applying Spark MapReduce and Machine Learning algorithms. 

1. The first application case is a MapReduce framework to compute allele frequencies from a large number of individual VCF files. 

a) sim_vcf.py

Generate a simulated merged vcf file according to number of SNPs and samples. Exponential distribution is used to generate guiding minor allele frequency (MAF) for each SNP. Genotypes are generated according to the MAFs. The SNPs with only one genotype across all samples are not written to the output VCF. 

b) divide_vcf.py

Divide the merged vcf file generated in step 1 into individual vcf files in a specified folder.

c) cal_freq.py

Pyspark code to read in individual vcf files and count the occurrence of any genotype at each SNP locus, and output genotype frequencies according to sorted SNP positions for possible downstream analyses such as computing allele frequencies and discovering rare mutations.

2. The second applicaiton case is an SVM machine learning model to distinguish between cancer and normal samples from microarray data. Because the gene number (>10000) is much higher than the sample number (102). Dimmension reduction is required to avoid overfitting.

a) ml_pca.py

Read in the raw data file "pheno_exp.txt". Normalize the raw data, conduct PCA and output the first 10 components as a matrix, with first column being the label and others being features.

b) ml_svm.py

Take in the output of step a and train the SVM model using PySpark.

3. Common utility programs

a) cv_div_dataset.py

Generate cross-validation files for validation of models.

b) svm_dens_vec.py

SVM model using a dense vector input file.
