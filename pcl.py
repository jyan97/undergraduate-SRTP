#coding=utf-8
from math import *
from numpy import *
import txt3,jie,os

portion1 = 8
portion = 0.5#jie.p
for nn in range(1,12):
    directory = 'spgkns/sp'+str(nn)
    print directory
    path = str(txt3.lj)
    title = 'mat'+str(directory)
    new_path = os.path.join(path, title)
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
    for k in range(1,301):
          a = 0
          file = open(str(txt3.lj)+str(directory)+'/'+str(k)+'.txt')
          f = open(str(txt3.lj)+'mat'+str(directory)+'/load'+str(k)+'.txt','w+t')
          #setline = int(ceil(100000/k*portion))+1#setline = int(ceil(1000000/820.284524133*portion))+1#
          setline = int(ceil(1000000/500*portion))+1
          while 1:
              lines = file.readlines()
              if not lines:
                  break
              for line in lines[setline:]:
                  word = line.split()
                  print >>f,float(word[0].strip()),float(word[1].strip()),float(word[2].strip()),float(word[3].strip()),float(word[4].strip()),float(word[5].strip()),float(word[6].strip()),float(word[7].strip()),float(word[8].strip()),float(word[9].strip()),float(word[10].strip()),float(word[11].strip()),float(word[12].strip()),float(word[13].strip()),float(word[14].strip()),float(word[15].strip()),float(word[16].strip()),float(word[17].strip()),float(word[18].strip()),float(word[19].strip()),float(word[20].strip()),float(word[21].strip()),float(word[22].strip()),float(word[23].strip()),float(word[24].strip()),float(word[25].strip()),float(word[26].strip())#
                  a = a+1
              print '文件load%d.txt'%k,'行数为%d'%a 
          f.close()
          file.close()
asdf

