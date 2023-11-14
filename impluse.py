import matplotlib.pyplot as plt 
import numpy as np
t= np.arange(-10,10,0.01)

y=np.zeros(len(t))
y[np.isclose(t,0,atol=0.00000001)]=1
plt.plot(t,y,"g")
plt.xlabel('time')
plt.ylabel('Amplitude')
plt.show()

n=np.arange(-5,6)
x=np.zeros_like(n)
x[n==0]=1
plt.stem(n,x)
plt.xticks(n);
plt.xlabel('time')
plt.ylabel('Amplitude')