#coding=utf-8
from math import *
from numpy import *
import txt3
n = 32
r = 0.00644304504412
zhi = 0.02
zlo = 0.0
print r,zhi
#zwall_stress
f = open(str(txt3.lj)+'mesh3_5k.stl','w')
print >>f,"solid ascii"
for i in range(0,n):        
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex 0.0 0.0",zlo
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zlo
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zlo
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zlo
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zlo
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zlo
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zlo
    print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zlo
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zlo
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zlo
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zlo
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zlo
    print >>f,"  endloop"
    print >>f," endfacet"
print >>f,"endsolid"
f.close()
#topwall
f = open(str(txt3.lj)+'mesh1_5k.stl','w')
print >>f,"solid ascii"
for i in range(0,n):        
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex 0.0 0.0",zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zhi
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zhi
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
print >>f,"endsolid"
f.close()
#cylwalls
#cylwalls3
nt=12
f = open(str(txt3.lj)+'mesh2_5kf3.stl','w')
print >>f,"solid ascii"
for na in range(1,nt+1):
    for i in range(0,n):
        if i<16:
           print >>f," facet normal",cos(pi/n*(2*i+1)),sin(pi/n*(2*i+1))," 0.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zlo+zhi/nt*(na-1)
           print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zlo+zhi/nt*(na-1)
           print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zhi/nt*na
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal",cos(pi/n*(2*i+1)),sin(pi/n*(2*i+1))," 0.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zhi/nt*na
           print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zhi/nt*na
           print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zlo+zhi/nt*(na-1)
           print >>f,"  endloop"
           print >>f," endfacet"
        else:
             m=i-24   
print >>f,"endsolid"
f.close()
#cylwalls1
f = open(str(txt3.lj)+'mesh2_5kf1.stl','w')
print >>f,"solid ascii"
for na in range(1,nt+1):
    for i in range(0,n):
        if i>15:
           print >>f," facet normal",cos(pi/n*(2*i+1)),sin(pi/n*(2*i+1))," 0.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zlo+zhi/nt*(na-1)
           print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zlo+zhi/nt*(na-1)
           print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zhi/nt*na
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal",cos(pi/n*(2*i+1)),sin(pi/n*(2*i+1))," 0.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zhi/nt*na
           print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zhi/nt*na
           print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zlo+zhi/nt*(na-1)
           print >>f,"  endloop"
           print >>f," endfacet"
print >>f,"endsolid"
f.close()

zhi = 0.00571*2
f = open(str(txt3.lj)+'mesh100_5k.stl','w')
print >>f,"solid ascii"
for i in range(0,n):        
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex 0.0 0.0",zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zhi
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r/2*cos(2*pi/n*i),r/2*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r*cos(2*pi/n*i),r*sin(2*pi/n*i),zhi
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
    print >>f," facet normal 0.0 0.0 1.0"
    print >>f,"  outer loop"
    print >>f,"   vertex",r*cos(2*pi/n*(i+1)),r*sin(2*pi/n*(i+1)),zhi
    print >>f,"   vertex",r/2*cos(2*pi/n*(i+1)),r/2*sin(2*pi/n*(i+1)),zhi
    print >>f,"   vertex",r*cos(pi/n*(2*i+1)),r*sin(pi/n*(2*i+1)),zhi
    print >>f,"  endloop"
    print >>f," endfacet"
print >>f,"endsolid"
f.close()
asdf
