#coding=utf-8
from math import *
from numpy import *
from scipy.optimize import leastsq
import pylab as plt
import txt3,jie,os

directory = 'chgkns/ch8'
for k in range(221,222):
    C = loadtxt(str(txt3.lj)+'mat'+str(directory)+'/load'+str(k)+'.txt')
    xi = C.T[0]
    yi = C.T[8]+C.T[5]+C.T[10]+C.T[16]+C.T[13]+C.T[19]
    zi = -C.T[2]
plt.figure(figsize=(20,12))
ax1 = plt.subplot(211)
plt.plot(xi,yi,'bo',label='m1')
ax1 = plt.subplot(212)
plt.plot(xi,zi,'bo',label='m1')
plt.show()
asd
