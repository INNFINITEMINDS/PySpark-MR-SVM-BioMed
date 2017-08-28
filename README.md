# Python-Spark-MapReduce-ML
A compile of Python scripts for applying Spark MapReduce and Machine Learning algorithms. 

1. The first application case is a MapReduce framework to compute allele frequencies from a large number of individual VCF files. 

a) sim_vcf.py

Generate a simulated merged vcf file according to number of SNPs and samples. Exponential distribution is used to generate guiding minor allele frequency (MAF) for each SNP. Genotypes are generated according to the MAFs. The SNPs with only one genotype across all samples are not written to the output VCF. 

b) divide_vcf.py

Divide the merged vcf file generated in step 1 into individual vcf files in a specified folder.

c) cal_freq.py

Pyspark code to read in individual vcf files and count the occurrence of any genotype at each SNP locus, and output genotype frequencies according to sorted SNP positions for possible downstream analyses such as computing allele frequencies and discovering rare mutations.

2. The second applicaiton case is an SVM machine learning model to classify tumor and normal samples from microarray data. Because the gene number (>10000) is much higher than the sample number (102). Dimmension reduction is required to avoid overfitting.

a) raw_div_dataset.py

Divide a data file (format:1st row: sample IDs, 2nd row: sample class, 1st column: feature Ids, others: feature values) like "pheno_exp.txt" into training and prediction data files according to a partition ratio. 

b) convert_train_data.py

Convert the training data into labeledpoint features with scaling and PCA implemented.

c) convert_pred_data.py 

Convert the prediciton data into dense vector features using the scaling and PCA rules established on the training data.

d) cv_div_dataset.py

Generate cross-validation files for validation of models.

e) execute_cv_svm.py

Iteratively run SVM models on the cross-validation datasets.

f) train_svm.py

Train a SVM model with SGD using labeledpoint (dense vector required) data.

g) test_svm.py

Test an SVM model on testing data (labeledpoint data with dense vector).

h) predict_svm.py

Make predictions using an SVM model on dense vector data (1st column contains IDs)

