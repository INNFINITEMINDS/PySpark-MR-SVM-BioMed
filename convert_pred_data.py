from __future__ import print_function
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import sys
if len(sys.argv)<3:
  print("python convert_pred_data.py raw_training_data raw_prediction_data output")
  quit()
#read in training dataset
with open(sys.argv[1],"r") as fl1:
  line1=fl1.readlines()
t_exp=[]
for i in range(2,len(line1)):
  gene1=line1[i].strip("\n").split("\t")[1:]
  t_exp.append(gene1)
t_exp1=np.transpose(t_exp)
#read in predicted dataset
with open(sys.argv[2],"r") as fl2:
  line2=fl2.readlines()
lab=line2[0].strip("\n").split("\t")[1:]
n_exp=[]
for i in range(2,len(line2)):
  gene2=line2[i].strip("\n").split("\t")[1:]
  n_exp.append(gene2)
n_exp1=np.transpose(n_exp)
#normalize training data then adjust prediction data
scaler = StandardScaler()
scaler.fit(t_exp1)
t_exp2=scaler.transform(t_exp1)
n_exp2=scaler.transform(n_exp1)
pca = PCA(n_components=10)
pca.fit(t_exp2)
n_exp3=pca.transform(n_exp2)
with open(sys.argv[3],"w") as of:
  for i in range(len(lab)):
    of.write(lab[i])
    for j in range(len(n_exp3[i])):
      of.write(" "+str(n_exp3[i][j]))
    of.write('\n')

