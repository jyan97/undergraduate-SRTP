#coding=utf-8
from math import *
from numpy import *
from scipy.optimize import leastsq
import pylab as plt
from matplotlib.pyplot import plot,savefig 
import txt3

sza=[]
szp=[]
szw=[]
for k in range(4,12):
      C = loadtxt(str(txt3.lj)+'data2/chgkns/ch'+str(k)+'pp.txt')
      m1 = list(C.T[4])
      n=m1.index(max(m1))
      ag = C.T[0,n]
      pre = mean(C.T[11,0:20])
      power = C.T[9,n-1]
      sza.append(ag)
      szp.append(pre)
      szw.append(power)
fyq = open(str(txt3.lj)+'data2/chap.txt','w')
for zn in range(7):      
    print >>fyq,szp[zn],sza[zn],szw[zn]
fyq.close
plt.figure(figsize=(20,12))
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)
plt.sca(ax1) 
plt.plot(szp,sza,'bo-')
plt.sca(ax2) 
plt.plot(szp,szw,'bo-')
savefig(str(txt3.lj)+'data2/chap.png')
plt.show()
adp
