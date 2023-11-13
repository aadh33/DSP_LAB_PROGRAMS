    # -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:23:29 2023

@author: DELL
"""

from numpy import cos, sin, pi, absolute, arange, zeros
from scipy.signal import hamming,firwin, freqz
from pylab import figure, clf, plot, xlabel, ylabel, xlim, ylim, title, grid, axes, show

N = eval(input('Enter the filter order N='))

[fc1,fc2] = eval(input('Enter the cutoff frequency='))
Fs = eval(input('Enter the sampling frequency='))
FN = 2*fc2    

taps = firwin(N, [fc1/Fs,fc2/Fs], window=('hamming'))

print('FIR Band Pass Filter Coefficients h[n]=',taps)


wn = hamming(N)
print('Normalized digital cut-off frequencies',fc1/Fs,fc2/Fs)
wc1 = (fc1/Fs)*pi
wc2 = (fc2/Fs)*pi
print('Digital cut-off frequencies',wc1,wc2)
K = 0.8 

Tuo = (N-1)/2
hd  = zeros(N)
h   = zeros(N)
for n in range(N):
    if n==Tuo:
        hd[n] = 1-((wc2-wc1)/pi)
        
    else:
        hd[n] = (sin(pi*(n-Tuo))-(sin(wc2*(n-Tuo))-sin(wc1*(n-Tuo))))/(pi*(n-Tuo))
    h[n] = hd[n]*wn[n]
    h[n] = h[n]
print('FIR Low Pass Filter coefficients using formula h[n]=',h)




figure(1)
plot(taps, 'bo-', linewidth=2)
xlabel('Filter taps--------->')
ylabel('Filter coefficients-------->')
title('Filter Coefficients')
grid(True)



figure(2)
clf()

W,H = freqz(taps, worN=8000)
plot((W/max(W)), absolute(H), linewidth=2)
#plot((W/max(W))*Fs,absolute(H), linewidth=2)
#xlabel('Frequency in Hz------->')
xlabel('Normalized Digital Frequency (Wc/pi)--->')
ylabel('Gain')
title('Frequency Response of Band Stop FIR Filter using Built-in Function')
ylim(-0.05, 1.05)
grid(True)

del W
del H


figure(3)
clf()
W,H = freqz(h, worN=8000)
plot((W/max(W)),absolute(H), linewidth=2)

xlabel('Normalized Digital Frequency (Wc/pi)------->')
ylabel('Gain')
title('Frequency Response of Band Stop FIR Filter using Own Formula based')
ylim(-0.05,1.05)
grid(True)
show()