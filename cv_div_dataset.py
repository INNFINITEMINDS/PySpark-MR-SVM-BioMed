from __future__ import print_function
import sys
import numpy as np
import os
from sklearn.utils import resample
if len(sys.argv)<4:
  print("python cv_div_dataset.py input_file output_dir fold")
  quit()
with open(sys.argv[1],'r') as fl:
  line=fl.readlines()
n=len(line)
print(n)
nline=resample(line,replace=False)
nfold=int(sys.argv[3])
unit=int(n/nfold)
if n%nfold>0:
  unit=unit+1
if not os.path.exists(sys.argv[2]):
  os.makedirs(sys.argv[2])
for i in range(nfold):
  dir1=sys.argv[2]+'/'+str(i)+'.train'
  dir2=sys.argv[2]+'/'+str(i)+'.test'
  with open(dir1,'w') as ftn:
    with open(dir2,'w') as fts:
      t_sta=i*unit
      t_end=(i+1)*unit
      if t_end>n:
        t_end=n
      for j in range(n):
        if j>=t_sta and j<t_end:
          fts.write(nline[j])
        else:
          ftn.write(nline[j])
  

