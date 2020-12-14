#coding=utf-8
from math import *
from numpy import *
import txt3

n = 32
r = 0.0256#ssts0.006
zhi = 0.125#ssts0.025
zlo = 0.0
nt=12
print r,zhi
#zwall_stress
f = open(str(txt3.lj)+'mesh3ssts.stl','w')
print >>f,"solid ascii"
for i in range(0,n):
    if i<8:
       m=i
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex 0.0 0.0",zlo
       print >>f,"   vertex",r/2,r/2*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"   vertex",r,r*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"   vertex",r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"   vertex",r/2,r/2*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r,r*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",r/2,r/2*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
    elif 7<i<16:
       m=i-8
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex 0.0 0.0",zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),r/2,zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),r/2,zlo
       print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),r,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),r,zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),r,zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),r,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),r,zlo
       print >>f,"  endloop"
       print >>f," endfacet"        
    elif 15<i<24:
       m=i-16
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex 0.0 0.0",zlo
       print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"   vertex",-r,r*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"   vertex",-r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",-r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",-r,r*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",-r/2,r/2*tan(2*pi/n*m-pi/4),zlo
       print >>f,"   vertex",-r,r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),zlo
       print >>f,"  endloop"
       print >>f," endfacet"
    else:
       m=i-24
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex 0.0 0.0",zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),-r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),-r/2,zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),-r/2,zlo
       print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),-r,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),-r,zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r/2*tan(2*pi/n*(m+1)-pi/4),-r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),-r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),-r,zlo
       print >>f,"  endloop"
       print >>f," endfacet"
       print >>f," facet normal 0.0 0.0 -1.0"
       print >>f,"  outer loop"
       print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),-r,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4),-r/2,zlo
       print >>f,"   vertex",r/2*tan(2*pi/n*m-pi/4)+r/2*tan(2*pi/n*(m+1)-pi/4),-r,zlo
       print >>f,"  endloop"
       print >>f," endfacet" 
print >>f,"endsolid"
f.close()
#topwall
f = open(str(txt3.lj)+'mesh1ssts.stl','w')
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
#cylwalls1,zuo
f = open(str(txt3.lj)+'mesh2sstsf1.stl','w')
print >>f,"solid ascii"
for na in range(1,nt+1):
    for i in range(0,n):
        if i<8:
           m=i
        elif 7<i<16:
             m=i-8
             print >>f," facet normal -1.0 0.0 0.0"
             print >>f,"  outer loop"
             print >>f,"   vertex",-r,r*tan(2*pi/n*m-pi/4),zlo+zhi/nt*(na-1)
             print >>f,"   vertex",-r,r*tan(2*pi/n*(m+1)-pi/4),zlo+zhi/nt*(na-1)
             print >>f,"   vertex",-r,r*tan(2*pi/n*(m+1)-pi/4),zhi/nt*na
             print >>f,"  endloop"
             print >>f," endfacet"
             print >>f," facet normal -1.0 0.0 0.0"
             print >>f,"  outer loop"
             print >>f,"   vertex",-r,r*tan(2*pi/n*m-pi/4),zhi/nt*na
             print >>f,"   vertex",-r,r*tan(2*pi/n*(m+1)-pi/4),zhi/nt*na
             print >>f,"   vertex",-r,r*tan(2*pi/n*m-pi/4),zlo+zhi/nt*(na-1)
             print >>f,"  endloop"
             print >>f," endfacet"        
        elif 15<i<24:
             m=i-16
        else:
             m=i-24
print >>f,"endsolid"
f.close()
#cylwalls3,you
f = open(str(txt3.lj)+'mesh2sstsf3.stl','w')
print >>f,"solid ascii"
for na in range(1,nt+1):
    for i in range(0,n):
        if i<8:
           m=i
           print >>f," facet normal 1.0 0.0 0.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r,r*tan(2*pi/n*m-pi/4),zlo+zhi/nt*(na-1)
           print >>f,"   vertex",r,r*tan(2*pi/n*(m+1)-pi/4),zlo+zhi/nt*(na-1)
           print >>f,"   vertex",r,r*tan(2*pi/n*(m+1)-pi/4),zhi/nt*na
           print >>f,"  endloop"
           print >>f," endfacet"
           print >>f," facet normal 1.0 0.0 0.0"
           print >>f,"  outer loop"
           print >>f,"   vertex",r,r*tan(2*pi/n*m-pi/4),zhi/nt*na
           print >>f,"   vertex",r,r*tan(2*pi/n*(m+1)-pi/4),zhi/nt*na
           print >>f,"   vertex",r,r*tan(2*pi/n*m-pi/4),zlo+zhi/nt*(na-1)
           print >>f,"  endloop"
           print >>f," endfacet"
        elif 7<i<16:
             m=i-8      
        elif 15<i<24:
             m=i-16
        else:
             m=i-24

print >>f,"endsolid"
f.close()
#cylwalls2,hou
f = open(str(txt3.lj)+'mesh2sstsf2.stl','w')
print >>f,"solid ascii"
for na in range(1,nt+1):
    for i in range(0,n):
        if i<8:
           m=i
        elif 7<i<16:
             m=i-8       
        elif 15<i<24:
             m=i-16 
        else:
             m=i-24
             print >>f," facet normal 0.0 -1.0 0.0"
             print >>f,"  outer loop"
             print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),-r,zlo+zhi/nt*(na-1)
             print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),-r,zlo+zhi/nt*(na-1)
             print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),-r,zhi/nt*na
             print >>f,"  endloop"
             print >>f," endfacet"
             print >>f," facet normal 0.0 -1.0 0.0"
             print >>f,"  outer loop"
             print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),-r,zhi/nt*na
             print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),-r,zhi/nt*na
             print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),-r,zlo+zhi/nt*(na-1)
             print >>f,"  endloop"
             print >>f," endfacet" 
print >>f,"endsolid"
f.close()
#cylwalls4,qian
f = open(str(txt3.lj)+'mesh2sstsf4.stl','w')
print >>f,"solid ascii"
for na in range(1,nt+1):
    for i in range(0,n):
        if i<8:
           m=i
        elif 7<i<16:
             m=i-8       
        elif 15<i<24:
             m=i-16
             print >>f," facet normal 0.0 1.0 0.0"
             print >>f,"  outer loop"
             print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),r,zlo+zhi/nt*(na-1)
             print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),r,zlo+zhi/nt*(na-1)
             print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),r,zhi/nt*na
             print >>f,"  endloop"
             print >>f," endfacet"
             print >>f," facet normal 0.0 1.0 0.0"
             print >>f,"  outer loop"
             print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),r,zhi/nt*na
             print >>f,"   vertex",r*tan(2*pi/n*(m+1)-pi/4),r,zhi/nt*na
             print >>f,"   vertex",r*tan(2*pi/n*m-pi/4),r,zlo+zhi/nt*(na-1)
             print >>f,"  endloop"
             print >>f," endfacet"  
        else:
             m=i-24
print >>f,"endsolid"
f.close()
#100
zhi = 2*r
print r,zhi
f = open(str(txt3.lj)+'mesh100ssts.stl','w')
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
asdfg
