#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:10:11 2023

@author: mec

"""
import matplotlib.pyplot as plt 
import numpy as np
n=np.arange(-5,6)
x=np.zeros_like(n)
x[(n>=-3)&(n<=3)]=-1
x[(n>=0)&(n<=3)]=1
plt.subplot(1,2,1)
plt.plot(n,x)
plt.xticks(n);


n=np.arange(-5,6)
x=np.zeros_like(n)
x[(n>=-3)&(n<=3)]=-1
x[(n>=0)&(n<=3)]=1
plt.subplot(1,2,2)
plt.stem(n,x)
plt.xticks(n);