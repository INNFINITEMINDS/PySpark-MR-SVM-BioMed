from __future__ import print_function
import os
import sys
if len(sys.argv)<2:
  print("python divide_vcf.py input_vcf output_dir")  
  quit()
with open(sys.argv[1],'r') as fl:
  header=fl.readline().strip('\n')
  word=header.split('\t')
  #print(len(word))
for i in range(1,len(word)-8):
  cmd='cut -f 1,2,3,4,5,6,7,8,9,'+str(9+i)+' '+sys.argv[1]+' >'+sys.argv[2]+'/'+str(i)+'.vcf'
  os.system(cmd)
