
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
        y=np.append(y,sum)
y.shape(k,k)
print(y)       
        
tw=np.dot(y,x)
print("the dft is  \n",y)

print(np.fft.fft(x))
        
print("The DFT of the input seq is:",y)
mag_y=[abs(k) for k in y]
plt.stem(k_array,mag_y)
plt.xlabel("Vlue of K")
plt.ylabel("phase")
plt.show()


phase_y=[cmath.phase(k)for k in y]
plt.stem(k_array,phase_y)
plt.xlabel("Value of K")
plt.ylabel("phase")
plt.show()
