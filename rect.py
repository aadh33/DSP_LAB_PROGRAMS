

import matplotlib.pyplot as plt 
import numpy as np
t= np.arange(-10,10,0.01)
T=float(input("Enter width: "))

y=np.zeros(len(t))
y[np.all([(t>=-T/2),(t<=T/2)],axis=0)]=1
print(y) 
plt.plot(t,y)
plt.show()

n=np.arange(-5,6)
x=np.zeros_like(n)
x[(n>=0)&(n<=4)]=1
plt.stem(n,x)
plt.xticks(n);