#coding=utf-8
from math import *
from numpy import *
import txt3
n = 32
r = 0.0256#ssts0.006
zlo = 0.0
zl=[0.0510329,0.0510986,0.0511543,0.0512,0.051228602581,0.0512511846921,0.0512582622379,0.0512653397837,0.05126758573505,0.0512698316864,0.0512708011946]
for ns in range(1,12):
    nt=ns-1
#    zhi = 2*r*(1+(-0.224848+1.62184765*ns-0.30659*ns*ns+0.027893*ns*ns*ns-0.0010143290*ns*ns*ns*ns)*0.0005)#2*r+(ns-1)*2*r*0.006/12#2*r+(ns-9)*2*r*0.03/10+9*2*r*0.03/10#1,0.0005
    zhi = zl[nt]
    f = open(str(txt3.lj)+'mesh1002sstsdt'+str(ns)+'.stl','w')
    print zhi
    print ns,r,zhi,'mesh100ssts'+str(ns)+'.stl'
    print >>f,"solid ascii"
    for i in range(0,n):
        if i<8:
           m=i
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex 0.0 0.0",zhi
           print >>f,"   vertex",r/2,r/2*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"   vertex",r,r*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"   vertex",r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"   vertex",r/2,r/2*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r,r*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",r/2,r/2*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
        elif 7<i<16:
           m=i-8
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex 0.0 0.0",zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),r/2,zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),r/2,zhi
           print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),r,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),r,zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),r,zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),r,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),r,zhi
           print >>f,"  endloop"
           print >>f," endfacet"        
        elif 15<i<24:
           m=i-16
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex 0.0 0.0",zhi
           print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"   vertex",-r,r*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"   vertex",-r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",-r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",-r,r*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*m-pi/4),zhi
           print >>f,"   vertex",-r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zhi
           print >>f,"  endloop"
           print >>f," endfacet"
        else:
           m=i-24
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex 0.0 0.0",zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),-r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),-r/2,zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),-r/2,zhi
           print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),-r,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),-r,zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),-r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),-r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),-r,zhi
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 0.0 0.0 -1.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),-r,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),-r/2,zhi
           print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),-r,zhi
           print >>f,"  endloop"
           print >>f," endfacet" 
    print >>f,"endsolid"
    f.close()
asd
ya2
0.006507058543


