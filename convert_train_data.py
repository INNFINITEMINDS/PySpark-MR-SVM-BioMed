from __future__ import print_function
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import sys
if len(sys.argv)<3:
  print("python convert_train_data.py raw_training_data output")
  quit()

with open(sys.argv[1],"r") as fl:
  line=fl.readlines()
  lab=line[1].strip("\n").replace('\r','').split("\t")[1:]
exp=[]
for i in range(2,len(line)):
  gene=line[i].strip("\n").split("\t")[1:]
  exp.append(gene)
exp1=np.transpose(exp)
scaler = StandardScaler()
scaler.fit(exp1)
exp2=scaler.transform(exp1)
pca = PCA(n_components=10)
pca.fit(exp2)
exp3=pca.transform(exp2)
with open(sys.argv[2],"w") as of:
  for i in range(len(lab)):
    of.write(lab[i])
    for j in range(len(exp3[i])):
      of.write(" "+str(exp3[i][j]))
    of.write('\n')
