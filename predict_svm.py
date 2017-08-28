from __future__ import print_function
from pyspark import SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.linalg import Vectors
import sys
if len(sys.argv)<3:
 print("python svm_dens_test.py input_dense_vector_file model_directory")
 quit()

if __name__ == "__main__":
    sc = SparkContext(appName="PythonSVMWithSGD")
    def denseFea(line):
        word=line.split(' ')
        values = [float(x) for x in word[1:]]
        return (word[0],Vectors.dense(values))
    sameModel = SVMModel.load(sc, sys.argv[2])
    ndata = sc.textFile(sys.argv[1])
    nparsedData = ndata.map(denseFea)
    # Predict on new data
    nPreds = nparsedData.map(lambda p: (p[0],sameModel.predict(p[1])))
    for x in nPreds.collect():
      print(x)
