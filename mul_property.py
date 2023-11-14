#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:15:35 2023

@author: mec
"""
import numpy as np

def dft(x,k):
    y=np.zeros(k,dtype='complex')
    for i in range (k):
        s=0
        for m in range (k):
            s+=x[m]*np.exp(complex(-1j)*2*np.pi*m*i*float(1/k))
            y[i]=s
    return y

def idft(x,k):
    y=np.zeros(k,dtype='complex')
    for i in range (k):
        s=0
        for m in range (k):
            s+=x[m]*np.exp(complex(1j)*2*np.pi*m*i*float(1/k))
            y[i]=s*(1/k)
    return y

x1=np.array(input("enter array 1:").split(",")).astype(int)
print(x1)
x2=np.array(input("enter array 2:").split(",")).astype(int)
print(x2)
if len(x1)<len(x2):
    x1=np.pad(x1,(0,len(x2)-len(x1)))
elif len(x1)>len(x2):
    x2=np.pad(x1,(0,len(x1)-len(x2)))
k=len(x1)
#lhs
X=x1*x2
print(dft(X,k))
#rhs
X1=dft(x1,k)
X2=dft(x2,k)
y=dft(X1,k)*dft(X2,k)
Y=idft(y,k)/k
print(Y)

