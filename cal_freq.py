from __future__ import print_function
from pyspark import SparkConf, SparkContext
import sys
if len(sys.argv)<3:
  print("python cal_freq.py input_dir output_dir")
  quit()
def test2(ln):
    word=ln.split("\t")
    gt=word[9]
    key=word[0]+" "+word[1]+" "+word[3]+" "+word[4]+" "+gt[:3]
    return [key]
  
sc=SparkContext("local", "Simple App")
textFile = sc.textFile(sys.argv[1]+'/*.vcf')
fm=textFile.flatMap(lambda line:test2(line)).map(lambda item: (item, 1)).reduceByKey(lambda a, b: a + b)\
    .sortByKey(ascending=True)
fm.saveAsTextFile(sys.argv[2])
