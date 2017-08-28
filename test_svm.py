from __future__ import print_function
from pyspark import SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
import sys
if len(sys.argv)<3:
 print("python test_svm.py input_dense_vector_file model_directory")
 quit()

if __name__ == "__main__":
    sc = SparkContext(appName="PythonSVMWithSGD")
    def parsePoint(line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[0], values[1:])
    sameModel = SVMModel.load(sc, sys.argv[2])
    ndata = sc.textFile(sys.argv[1])
    nparsedData = ndata.map(parsePoint)
    # Evaluating the model on training data
    nlabelsAndPreds = nparsedData.map(lambda p: (p.label, sameModel.predict(p.features)))
    trainAcc = nlabelsAndPreds.filter(lambda lp: lp[0] == lp[1]).count() / float(nparsedData.count())
    print("Model accuracy = " + str(trainAcc))
   
