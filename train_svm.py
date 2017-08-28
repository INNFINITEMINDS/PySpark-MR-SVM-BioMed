from __future__ import print_function
from pyspark import SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
import sys

if len(sys.argv)<3:
  print("python train_svm.py input_dens output_model_dir #_iterations(default:100)")
  quit()
n_ite=100
if len(sys.argv)==4:
  n_ite=int(sys.argv[3])

if __name__ == "__main__":
    sc = SparkContext(appName="PythonSVMWithSGDE")

    def parsePoint(line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[0], values[1:])

    data = sc.textFile(sys.argv[1])
    parsedData = data.map(parsePoint)

    model = SVMWithSGD.train(parsedData, iterations=n_ite)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda lp: lp[0] != lp[1]).count() / float(parsedData.count())
    print("Training Error = " + str(trainErr))

    # Save model
    model.save(sc, sys.argv[2])
