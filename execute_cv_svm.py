from __future__ import print_function
import sys
import os
import subprocess

if len(sys.argv)<3:
  print("python execute_cv_svm.py cv_datasets_folder model_folder")
  quit()
if not os.path.exists(sys.argv[2]):
  os.makedirs(sys.argv[2])
cmd=[]
cmd.append('ls')
cmd.append(sys.argv[1])
process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
out, err = process.communicate()
word=out.strip("\n").split("\n")
max_n=0
for temp in word:
  temp1=temp.split(".")
  if int(temp1[0])>max_n:
    max_n=int(temp1[0])
n_cv=max_n+1
print(str(n_cv)+" fold cross validation found!")
for i in range(n_cv):
  os.system("python train_svm.py "+sys.argv[1]+"/"+str(i)+".train "+sys.argv[2]+"/"+str(i)+" 100")
  os.system("python test_svm.py "+sys.argv[1]+"/"+str(i)+".test "+sys.argv[2]+"/"+str(i))
