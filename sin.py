#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:59:05 2023

@author: mec
"""
import matplotlib.pyplot as plt 
import numpy as np
#sampling rate=sr
sr=44100.0
#sampling interval=ts
ts=1.0/sr
t=np.arange(0,1,ts)
#frequency of the signal
my_freq=float(input("enter the frequency:"))
y=np.sin(2*np.pi*my_freq*t)
plt.figure(figsize=(6,4))
plt.title('frequency='+str(my_freq)+'hz')
plt.plot(t,y,'c')
plt.ylabel('amplitude')
plt.xlabel('time(sec)')
plt.show()