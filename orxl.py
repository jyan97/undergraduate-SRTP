﻿#coding=utf-8
from math import *
from numpy import *
import txt3,jie,os


y=[[0]*11*12]*300
for k in range(1,12):
      C = loadtxt(str(txt3.lj)+'data2/sp17kn/sp'+str(k)+'pp.txt')
      y[-13+k*13] = C.T[0]
      y[-12+k*13] = C.T[1]
      y[-11+k*13] = C.T[2]
      y[-10+k*13] = C.T[3]
      y[-9+k*13] = C.T[4]
      y[-8+k*13] = C.T[5]
      y[-7+k*13] = C.T[6]
      y[-6+k*13] = C.T[7]
      y[-5+k*13] = C.T[8]
      y[-4+k*13] = C.T[9]
      y[-3+k*13] = C.T[10]
      y[-2+k*13] = C.T[11]
      y[-1+k*13] = C.T[18]
      print 'sp'+str(k)+'pp.txt'
f = open(str(txt3.lj)+'data2/datsp17pp.txt','w')
for n in range(300):
   print >>f,y[0][n],y[1][n],y[2][n],y[3][n],y[4][n],y[5][n],y[6][n],y[7][n],y[8][n],y[9][n],y[10][n],y[11][n],y[12][n],y[13][n],y[14][n],y[15][n],y[16][n],y[17][n],y[18][n],y[19][n],y[20][n],y[21][n],y[22][n],y[23][n],y[24][n],y[25][n],y[26][n],y[27][n],y[28][n],y[29][n],y[30][n],y[31][n],y[32][n],y[33][n],y[34][n],y[35][n],y[36][n],y[37][n],y[38][n],y[39][n],y[40][n],y[41][n],y[42][n],y[43][n],y[44][n],y[45][n],y[46][n],y[47][n],y[48][n],y[49][n],y[50][n],y[51][n],y[52][n],y[53][n],y[54][n],y[55][n],y[56][n],y[57][n],y[58][n],y[59][n],y[60][n],y[61][n],y[62][n],y[63][n],y[64][n],y[65][n],y[66][n],y[67][n],y[68][n],y[69][n],y[70][n],y[71][n],y[72][n],y[73][n],y[74][n],y[75][n],y[76][n],y[77][n],y[78][n],y[79][n],y[80][n],y[81][n],y[82][n],y[83][n],y[84][n],y[85][n],y[86][n],y[87][n],y[88][n],y[89][n],y[90][n],y[91][n],y[92][n],y[93][n],y[94][n],y[95][n],y[96][n],y[97][n],y[98][n],y[99][n],y[100][n],y[101][n],y[102][n],y[103][n],y[104][n],y[105][n],y[106][n],y[107][n],y[108][n],y[109][n],y[110][n],y[111][n],y[112][n],y[113][n],y[114][n],y[115][n],y[116][n],y[117][n],y[118][n],y[119][n],y[120][n],y[121][n],y[122][n],y[123][n],y[124][n],y[125][n],y[126][n],y[127][n],y[128][n],y[129][n],y[130][n],y[131][n],y[132][n],y[133][n],y[134][n],y[135][n],y[136][n],y[137][n],y[138][n],y[139][n],y[140][n],y[141][n],y[142][n]
f.close
asd
