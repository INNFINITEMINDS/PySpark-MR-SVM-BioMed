from pyspark import SparkContext
from pyspark.mllib.classification import SVMWithSGD, SVMModel
from pyspark.mllib.regression import LabeledPoint

if __name__ == "__main__":
    sc = SparkContext(appName="PythonSVMWithSGDExample")

    def parsePoint(line):
        values = [float(x) for x in line.split(' ')]
        return LabeledPoint(values[0], values[1:])

    data = sc.textFile("pheno_exp.svm.fea")
    parsedData = data.map(parsePoint)

    model = SVMWithSGD.train(parsedData, iterations=100)

    # Evaluating the model on training data
    labelsAndPreds = parsedData.map(lambda p: (p.label, model.predict(p.features)))
    trainErr = labelsAndPreds.filter(lambda lp: lp[0] != lp[1]).count() / float(parsedData.count())
    print("Training Error = " + str(trainErr))

    # Save and load model
    #model.save(sc, "target/pythonSVMWithSGDModel")
    #sameModel = SVMModel.load(sc, "target/pythonSVMWithSGDModel")
