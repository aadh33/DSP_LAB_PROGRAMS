#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 11:02:41 2023

@author: mec
"""

import numpy as np
import matplotlib.pyplot as plt
import cmath

x=np.array(input("enter the sequence:").split(",")).astype(int)
k=len(x)
k_array=np.arange(0,k,1)

y= np.ones(k, dtype="complex")
for i in range(k):
    sum=0
    for m in range(k):
        sum+=x[m]*np.exp(complex(-1j)*2*np.pi*i*m*float(1/k))
        y[i]=sum
print("The DFT of the input seq is: \n",y)
mag_y=[abs(k) for k in y]
plt.stem(k_array,mag_y)
plt.xlabel("Value of K")
plt.ylabel("phase")
plt.show()
phase_y=[cmath.phase(k)for k in y]
plt.stem(k_array,phase_y)
plt.xlabel("Value of K")
plt.ylabel("phase")
plt.show()
