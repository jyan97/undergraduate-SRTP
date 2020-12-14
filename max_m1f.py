#coding=utf-8
from math import *
from numpy import *
from scipy.optimize import leastsq
import pylab as plt
from matplotlib.pyplot import plot,savefig 
import txt3

pforce = []
pm1 = []
pm2 = []
ppower = []
ppre = []
name='sp17kn/sp'
nnn=[]
ff = open(str(txt3.lj)+'data2/spmaxm1f'+'.txt','w')
for nn in range(1,12):
    C = loadtxt(str(txt3.lj)+'data2/'+str(name)+str(nn)+'pp.txt')
    f = C.T[1]
    force = list(C.T[2])
    m1 = list(C.T[4])
    m2 = list(C.T[5])
    power = list(C.T[9])
    pre = mean(C.T[10,10])
    pforce.append(f[force.index(max(force))])
    pm1.append(f[m1.index(max(m1))])
    pm2.append(f[m2.index(max(m2))])
    ppower.append(f[power.index(max(power))])
    nnn.append(nn)
    ppre.append(pre)


    force1=list(pforce)
    mm1=list(pm1)
    mm2=list(pm2)
    pp=list(ppower)
#    print >>ff,'max_fre_force:',force1[0],'max_force:',max(force)
#    print >>ff,'max_fre_m1:',mm1[0],'max_m1:',max(m1)
#    print >>ff,'max_fre_m2:',mm2[0],'max_m2:',max(m2)
#    print >>ff,'max_fre_power:',pp[0],'max_power:',max(power)
    print name
    print 'max_fre_force:',force1[nn-1],'max_force:',max(force)
    print 'max_fre_m1:',mm1[nn-1],'max_m1:',max(m1)
    print 'max_fre_m2:',mm2[nn-1],'max_m2:',max(m2)
    print 'max_fre_power:',pp[nn-1],'max_power:',max(power)
    print >>ff,ppre[nn-1],mm1[nn-1]
ff.close

asdf
