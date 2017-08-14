from __future__ import print_function
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

with open("pheno_exp.txt","r") as fl:
  line=fl.readlines()
  lab=line[1].strip("\n").replace('\r','').split("\t")[1:]
exp=[]
for i in range(2,len(line)):
  gene=line[i].strip("\n").split("\t")[1:]
  exp.append(gene)
exp_n=StandardScaler().fit_transform(exp)
pca = PCA(n_components=10)
pca.fit(exp_n)
exp_rd=pca.components_
with open("pheno_exp.svm.fea","w") as of:
  for i in range(len(lab)):
    of.write(lab[i])
    for j in range(len(exp_rd)):
      of.write(" "+str(exp_rd[j][i]))
    of.write('\n')
