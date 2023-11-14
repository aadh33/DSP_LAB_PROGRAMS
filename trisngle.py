#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 11:23:17 2023

@author: mec
"""

import matplotlib.pyplot as plt 
import numpy as np
a=np.arange(6)
b=np.arange(4,-1,-1)
x=np.concatenate([a,b])
plt.plot(x)
plt.xticks(np.arange(11));



a=np.arange(6)
b=np.arange(4,-1,-1)
x=np.concatenate([a,b])

plt.stem(x)
plt.xticks(np.arange(11));