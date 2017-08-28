from __future__ import print_function
import sys
import numpy as np
from sklearn.utils import resample
if len(sys.argv)<4:
  print("python raw_div_dataset.py input_file output_prefix train_ratio")
  quit()
with open(sys.argv[1],'r') as fl:
  line=fl.readlines()
word=line[0].strip("\n").split("\t")
id=range(1,len(word))
nid=resample(id,replace=False)
of1=sys.argv[2]+".train"
of2=sys.argv[2]+".predict"
r=float(sys.argv[3])
c=len(id)*r
with open(of1,'w') as fl1:
  with open(of2,'w') as fl2:
    for i in range(len(line)):
      word=line[i].strip("\n").split("\t")
      fl1.write(word[0])
      fl2.write(word[0])
      for j in range(len(word)-1):
        if j<c:
          fl1.write('\t'+word[nid[j]])
        else:
          fl2.write('\t'+word[nid[j]])
      fl1.write('\n')
      fl2.write('\n')
        

