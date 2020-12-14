#coding=utf-8
from math import *
from numpy import *
import txt3,jie,os

ll=[0.0510329,0.0510986,0.0511543,0.0512,0.051228602581,0.0512511846921,0.0512582622379,0.0512653397837,0.05126758573505,0.0512698316864,0.0512708011946]
p=[]
q=[]
for k in range(1,12):
    C = loadtxt(str(txt3.lj)+'data2/ch17kn/ch'+str(k)+'pp.txt')
    f = C.T[1]
    power = list(C.T[9])
    pre = mean(C.T[10,0])
    maxpower=max(power[10:300])
    maxfre=f[power.index(maxpower)]
    kn=power.index(maxpower)
    print 'file'+str(k),kn
    for n in range(kn-10*k-10,kn):
        if power[n]>0.5*maxpower:
           y1=power[n]
           y2=power[n-1]
           x1=f[power.inde                                                                                                                                                                                                                                                               x(y1)]
           x2=f[power.index(y2)]
           fx1=0.5*maxpower*(x1-x2)/(y1-y2)+x1-y1*(x1-x2)/(y1-y2)
           print fx1,n
           break
    for n in range(kn,kn+10*k+10):
        if power[n]<0.5*maxpower:
           y3=power[n]
           y4=power[n-1]
           x3=f[power.index(y3)]
           x4=f[power.index(y4)]
           fx2=0.5*maxpower*(x3-x4)/(y3-y4)+x3-y3*(x3-x4)/(y3-y4)
           print fx2,n
           break
    p.append(pre)
    q.append((fx2-fx1)/maxfre)
f = open(str(txt3.lj)+'data2/Qch.txt','w')
for n in range(len(p)):   
    print >>f,p[n],q[n]
f.close
ads

