from __future__ import print_function
from pyspark import SparkContext
# $example on$
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint
import sys
if len(sys.argv)<2:
 print("Please supply an input file of dense vectors(first column is label)")
 quit()

if __name__ == "__main__":
    sc = SparkContext(appName="PythonSVMWithSGDExample")

    # $example on$
    # Load and parse the data
    def parsePoint(line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[0], values[1:])

    data = sc.textFile(sys.argv[1])
    parsedData = data.map(parsePoint)

    # Build the model
    model = SVMWithSGD.train(parsedData, iterations=100)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda lp: lp[0] != lp[1]).count() / float(parsedData.count())
    print("Training Error = " + str(trainErr))

    # Save and load model
    #model.save(sc, "target/pythonSVMWithSGDModel")
    #sameModel = SVMModel.load(sc, "target/pythonSVMWithSGDModel")
    # $example off$
