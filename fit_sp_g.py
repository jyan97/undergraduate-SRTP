#coding=utf-8
from math import *
from numpy import *
from scipy.optimize import leastsq
import pylab as plt
from matplotlib.pyplot import plot,savefig 
import txt3

yl=[]
yq=[]
zl=[0.0510329,0.0510986,0.0511543,0.0512,0.051228602581,0.0512511846921,0.0512582622379,0.0512653397837,0.05126758573505,0.0512698316864,0.0512708011946]
for kn in range(1,12):
    print '----------------------------START-----------------------------------'
    pf = []
    pa1 = []
    pa2 = []
    pm1 = []
    pm2 = []
    pr1 = []
    pr2 = []
    pwxc = []
    ppower = []
    bpp = []
    ppp = []
    ppp1 = []
    ppp2 = []
    ppp3 = []
    ppp4 = []
    ppp5 = []
    ppp6 = []
    ypp = []
    directory = 'spgkns/sp'+str(kn)
    #directory = 'chgkns/ch'+str(kn)
    print directory
    pk = []
    kk = 0
    for k in range(1,301):
          C = loadtxt(str(txt3.lj)+'mat'+str(directory)+'/load'+str(k)+'.txt')
          xi = C.T[0]
          yi = C.T[1]+C.T[4]+C.T[7]+C.T[12]+C.T[15]+C.T[18]#yi = C.T[4]+C.T[7](z)+C.T[12]+C.T[18](x)#yi = C.T[1]+C.T[4]+C.T[7]+C.T[12]+C.T[15]+C.T[18]#sp
          #yi = C.T[8]+C.T[5]+C.T[10]+C.T[16]+C.T[13]+C.T[19]#yi = C.T[1]+C.T[5](z)+C.T[10]+C.T[16](y)+C.T[13]+C.T[19](x)#ch
          zi = -C.T[2]
          bpi = C.T[5,1]/(1000*zl[kn-1]**2)
          ppi = mean(C.T[20])*0.0512/zl[kn-1]#mean(C.T[5,1])/(1000*0.0256**2*4)
          ppi1 = -mean(C.T[21])/(0.0512*0.0512*zl[kn-1])
          ppi2 = -mean(C.T[22])/(0.0512*0.0512*zl[kn-1])
          ppi3 = -mean(C.T[23])/(0.0512*0.0512*zl[kn-1])
          ppi4 = -mean(C.T[24])/(0.0512*0.0512*zl[kn-1])
          ppi5 = -mean(C.T[25])/(0.0512*0.0512*zl[kn-1])
          ppi6 = -mean(C.T[26])/(0.0512*0.0512*zl[kn-1])
          yp = abs((abs(ppi1)-abs(ppi2)))/abs(ppi1)
          N=len(xi)
          fs=1/(xi[2]-xi[1])
          n=arange(N)
          f=n*fs/N
          nn=int(10000*N/fs)
          f=f[1:nn]
          newy=fft.fft(yi,N)
          mag=list(abs(newy))[1:nn]
          frequency=f[mag.index(max(mag))]

          newy2=fft.fft(zi,N)
          mag2=list(abs(newy2))[1:nn]
          frequency1=f[mag2.index(max(mag2))]
#-------------------------------------------------------------------------
#这一模块为求初始的振幅和位相
          h1=yi[1]#t=0时力的大小
          h2=zi[1]#t=0时加速度的大小
          n1=(max(yi)-min(yi))/2#取力的最大值，作为力的初始振幅值
          n2=(max(zi)-min(zi))/2#取加速度的最大值，作为加速度的初始振幅值
          k1=(max(yi)+min(yi))/2
          k2=(max(zi)+min(zi))/2
          if abs((h1-k1)/n1) > 1:
             p1=acos(int((h1-k1)/n1))
          else:
             p1=acos((h1-k1)/n1)#力的位相的初始值          
          if abs((h2-k2)/n2) > 1:
             p2=acos(int((h2-k2)/n2))
          else:
             p2=acos((h2-k2)/n2)#加速度位相的初始值
    
          w=2*pi*frequency#角频率的初始值    
          w1=2*pi*frequency1
          m0=0#空铝杯的质量
          abc0=[n1,w,p1,k1]
          par0=[n2,w1,p2,k2]
#-------------------------------------------------------------------------
#该模块的程序为拟合正弦函数
          def func(x,p):
              r1,s1,t1,u1 = p
              return r1*cos(s1*x+t1)+u1
    
          def residuals(p,y,x):
              return y-func(x,p)

          def func2(x,p):
              r2,s2,t2,u2 = p
              return r2*cos(s2*x+t2)+u2

          def residuals2(p,y,x):
              return y-func2(x,p)

          plsq1 = leastsq(residuals,abc0,args=(yi,xi))
          plsq2 = leastsq(residuals2,par0,args=(zi,xi))

          a1 = plsq1[0][0]
          b1 = plsq1[0][1]
          c1 = plsq1[0][2]    
          d1 = plsq1[0][3]
          rsquare1 = sqrt(sum((func(xi,plsq1[0])-sum(yi)/len(yi))**2)/sum((yi-sum(yi)/len(yi))**2))

          a2 = plsq2[0][0]
          b2 = plsq2[0][1]
          c2 = plsq2[0][2]
          d2 = plsq2[0][3]
          rsquare2 = sqrt(sum((func2(xi,plsq2[0])-sum(zi)/len(zi))**2)/sum((zi-sum(zi)/len(zi))**2))
#-------------------------------------------------------------------------
#该模块为求位相，力，加速度，有效质量的实数部分和虚数部分
          wx1=180*c1/pi
          wx2=180*c2/pi
          if  a1>=0:
              a1=a1
              c1=c1
              wx1=wx1
          else:
              a1=abs(a1)
              c1=c1+pi
              wx1=wx1+180

          if  a2>=0:
              a2=a2
              c2=c2
              wx2=wx2     
          else:
              a2=abs(a2)
              c2=c2+pi
              wx2=wx2+180 
       
          if  abs(wx1)<=360:
              wx1=wx1
              if   wx1<-180:
                   wx1=wx1+360    
              elif wx1>180:
                   wx1=wx1-360
              else:
                   wx1=wx1
          else:
              if   wx1<=0:
                   wx1=wx1%-360
                   if   wx1>=-180:    
                        wx1=wx1
                   else:
                        wx1=wx1+360
              else:
                   wx1=wx1%360
                   if   wx1<=180:
                        wx1=wx1
                   else:
                        wx1=wx1-360
          if  abs(wx2)<=360:
              wx2=wx2
              if   wx2<-180:
                   wx2=wx2+360
              elif wx2>180:
                   wx2=wx2-360
              else:
                   wx2=wx2       
          else:
              if   wx2<=0:
                   wx2=wx2%-360
                   if   wx2>=-180:
                        wx2=wx2
                   else:
                        wx2=wx2+360
              else:
                   wx2=wx2%360
                   if   wx2<=180:
                        wx2=wx2
                   else:
                        wx2=wx2-360
          wxc=wx1-wx2
          if  abs(wxc)<=360:
              wxc=wxc
              if   wxc<-180:
                   wxc=wxc+360
              elif wxc>180:
                   wxc=wxc-360
              else:
                   wxc=wxc    
          else:
              if   wxc<=0:
                   wxc=wxc%-360
                   if  wxc>=-180:
                       wxc=wxc
                   else:
                       wxc=wxc+360
              else:
                   wxc=wxc%360
                   if  wxc<=180:
                       wxc=wxc
                   else:
                       wxc=wxc-360

          m1=a1*cos(c1-c2)/a2-m0
          m2=-a1*sin(c1-c2)/a2

          power=a1*a2*sin(c2-c1)/(2*b2)
          b1=abs(b1)
          print k,b1/(2*pi),a1,a2,m1,m2,rsquare1,rsquare2,wxc,power,bpi,ppi
          if rsquare1>0:
             pf.append(b1/(2*pi))
             pa1.append(a1)
             pa2.append(a2)
             pm1.append(m1)
             pm2.append(m2)
             pr1.append(rsquare1)
             pr2.append(rsquare2)
             pwxc.append(wxc)
             ppower.append(power)
             bpp.append(bpi)
             ppp.append(ppi)
             ppp1.append(ppi1)
             ppp2.append(ppi2)
             ppp3.append(ppi3)
             ppp4.append(ppi4)
             ppp5.append(ppi5)
             ppp6.append(ppi6)
             ypp.append(yp)
             pk.append(0.1*k)
             kk=kk+1         

    f = open(str(txt3.lj)+'data2/'+str(directory)+'pp.txt','w')
    for n in range(kk):   
        print >>f,pk[n],pf[n],pa1[n],pa2[n],pm1[n],pm2[n],pr1[n],pr2[n],pwxc[n],ppower[n],bpp[n],ppp[n],ppp1[n],ppp2[n],ppp3[n],ppp4[n],ppp5[n],ppp6[n],ypp[n]
    #    print >>f,pk[kk-n-1],pf[kk-n-1],pa1[kk-n-1],pa2[kk-n-1],pm1[kk-n-1],pm2[kk-n-1],pr1[kk-n-1],pr2[kk-n-1],pwxc[kk-n-1],ppower[kk-n-1]
    f.close

    plt.figure(figsize=(20,12))
    ax1 = plt.subplot(431)
    ax2 = plt.subplot(432)
    ax3 = plt.subplot(433)
    ax4 = plt.subplot(434)
    ax5 = plt.subplot(435)
    ax6 = plt.subplot(436)
    ax7 = plt.subplot(437)
    ax8 = plt.subplot(438)
    ax9 = plt.subplot(439)
    ax10 = plt.subplot(4,3,10)
    ax11 = plt.subplot(4,3,11)
    ax12 = plt.subplot(4,3,12)
    plt.sca(ax1) 
    plt.title('The effective mass')
    plt.xlabel(u'frequency')
    plt.ylabel(u'm')
    plt.plot(pk,pm1,'r*-',label='m1')
    plt.plot(pk,pm2,'bo-',label='m2')
    plt.legend(bbox_to_anchor=(0.9,1), loc=2, borderaxespad=0.)

    plt.sca(ax2)
    plt.title('Force amplitude')
    plt.xlabel(u'frequency')
    plt.ylabel(u'force')
    plt.plot(pk,pa1,'bo-')

    plt.sca(ax3)
    plt.title('The acceleration amplitude')
    plt.xlabel(u'frequency')
    plt.ylabel(u'acceleration')
    plot3 = plt.plot(pk,pa2,'bo')

    plt.sca(ax4)
    plt.title('Goodness of fit')
    plt.xlabel(u'frequency')
    plt.ylabel(u'rsquare')
    plt.plot(pk,pr1,'r*-',label='rsquare1')
    plt.plot(pk,pr2,'bo-',label='rsquare2')
    plt.legend(bbox_to_anchor=(0.9,0.8), loc=2, borderaxespad=0.)

    plt.sca(ax5)
    plt.title('Phase contrast')
    plt.xlabel(u'frequency')
    plt.ylabel(u'wxc')
    plt.plot(pk,pwxc,'bo-')

    plt.sca(ax6)
    plt.title('Energy dissipation')
    plt.xlabel(u'frequency')
    plt.ylabel(u'power')
    plt.plot(pk,ppower,'bo-')
    plt.sca(ax7) 
    plt.xlabel(u'x')
    plt.plot(pk,ppp1,'bo-')
    plt.sca(ax8) 
    plt.xlabel(u'y')
    plt.plot(pk,ppp2,'bo-')

    plt.sca(ax9) 
    plt.xlabel(u'z')
    plt.plot(pk,ppp3,'bo-')

    plt.sca(ax10) 
    plt.xlabel(u'xy')
    plt.plot(pk,ppp4,'bo-')
    plt.sca(ax11) 
    plt.xlabel(u'xz')
    plt.plot(pk,ppp5,'bo-')
    plt.sca(ax12) 
    plt.xlabel(u'yz')
    plt.plot(pk,ppp6,'bo-')
    #plt.plot(ppp,ypp,'bo-')
    savefig(str(txt3.lj)+'data2/'+str(directory)+'pp.png')
    plt.show()
    yl.append(mean(ypp))
    yq.append(mean(ppp))
fyq = open(str(txt3.lj)+'data2/spgyl.txt','w')
for zn in range(len(yq)): 
    print >>fyq,yq[zn],yl[zn]
fyq.close
plt.figure(2)
plt.plot(yq,yl,'bo-')
savefig(str(txt3.lj)+'data2/spgyl.png')
plt.show()
adf
