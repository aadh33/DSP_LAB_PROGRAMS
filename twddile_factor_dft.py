#twiddle factor

import numpy as np
import matplotlib.pyplot as plt
import cmath

def plot_ifft(k_array,y):
    #plot
    mag_y=[abs(k) for k in y]
    plt.stem(k_array,mag_y)
    plt.title("Magnitude plot")
    plt.xlabel("value of k")
    plt.ylabel("|x[k]|")
    plt.show()
    #phase
    phase_y=[cmath.phase(k) for k in y]
    plt.stem(k_array,phase_y)
    plt.title("phase plot")
    plt.xlabel("value of k")
    plt.ylabel("<x[k]")
    plt.show()
    
    
x=np.array(input("Sequence: ").split(',')).astype(complex)
k=len(x)
k_array=np.arange(0,k,1)
twiddle=np.ones(k,dtype="complex")
for i in range(k):
    for j in range (k):
        num=np.exp(complex(-1j)*2*np.pi*i*j*float(1/k))
        twiddle=np.append(twiddle,num)
twiddle.shape=(k,k)
print(twiddle)
y=(np.dot(twiddle,x))*(1/k)



print("\n\nIDFT(twiddle) :", y)
print("\nUsing Numpy : ",np.fft.ifft(x))
plot_ifft(k_array,y)

