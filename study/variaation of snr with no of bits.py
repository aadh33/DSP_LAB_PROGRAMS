# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:05:14 2024

@author: adith
"""

import numpy as np
import matplotlib.pyplot as plt


bits = np.arange(1,50,1)
snrdB = []
for i in bits:
    snrval = 6.02*i + 1.76
    snrdB.append(snrval)


plt.grid()    
plt.xscale('linear')
plt.yscale('log')
plt.plot(bits,snrdB)
plt.show()