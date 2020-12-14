#coding=utf-8
from math import *
from numpy import *
import txt3,jie,os

ll=[0.0510329,0.0510986,0.0511543,0.0512,0.051228602581,0.0512511846921,0.0512582622379,0.0512653397837,0.05126758573505,0.0512698316864,0.0512708011946]
r1=0.001
r2=0.0014
md=19300
f = open(str(txt3.lj)+'data2/md.txt','w')
for n in range(11):
    v=0.0512*0.0512*ll[n]
    m=4.0/3.0*pi*(r1*r1*r1*9777+r2*r2*r2*3563)*md
    md1=4.0/3.0*pi*(r1*r1*r1*9777+r2*r2*r2*3563)*md/v
    print >>f,md1,ll[n],m
f.close
asd
