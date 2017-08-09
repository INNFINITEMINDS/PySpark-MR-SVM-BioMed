from __future__ import print_function
import sys
import random
import numpy as np
if(len(sys.argv)<3):
  print("python sim_vcf.py #snps #samples output")
  quit()
nt=['A','C','G','T']
fmt=['0/0','0/1','1/1']
maf0=np.random.exponential(0.5,3*int(sys.argv[1]))/5
#print(maf0)
ct=0
maf1=[]
for x in maf0:
  if x<=0.5:
    if ct>=int(sys.argv[1]):
      break
    maf1.append(x)
    ct=ct+1
with open(sys.argv[3],'w') as fl:
  fl.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT')
  for i in range(int(sys.argv[2])):
    fl.write('\ts'+str(i+1))
  fl.write('\n')
  i=1
  for y in maf1:
    gt=np.random.choice(nt,2,replace=False)
    chr=np.random.choice(22,1)+1
    pos=np.random.choice(1000000,1)+1
    oline=str(chr[0])+'\t'+str(pos[0])+'\trs'+str(i)+'\t'+gt[0]+'\t'+gt[1]\
      +'\t.\t.\t.\t.'
    allgt=set()
    for j in range(int(sys.argv[2])):
      code=0
      for k in range(2):
        r=random.uniform(0,1)
        if r<y:
          code=code+1
      oline=oline+'\t'+fmt[code-1]
      allgt.add(code)
    #print(allgt)
    if len(allgt)>1:
      fl.write(oline+'\n')
    i=i+1

