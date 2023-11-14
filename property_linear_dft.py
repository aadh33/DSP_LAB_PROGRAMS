import numpy as np
#import matplotlib.pyplot as plt 
def dft(x,k):
    y=np.zeros(k,dtype='complex')
    for i in range (k):
        s=0
        for m in range (k):
            s+=x[m]*np.exp(complex(-1j)*2*np.pi*m*i*float(1/k))
            y[i]=s
    return y

def idft(x,k):
    y=np.zeros(k,dtype='complex')
    for i in range (k):
        s=0
        for m in range (k):
            s+=x[m]*np.exp(complex(1j)*2*np.pi*m*i*float(1/k))
            y[i]=s*(1/k)
    return y

#linearity
x1=np.array(input("enter array 1:").split(",")).astype(int)
print(x1)
x2=np.array(input("enter array 2:").split(",")).astype(int)
a=int(input("enter element to 1:"))
b=int(input("enter element to b:"))
if len(x1)<len(x2):
    x1=np.pad(x1,(0,len(x2)-len(x1)))
elif len(x2)>len(x1):
    x1=np.pad(x1,(0,len(x1)-len(x2)))
k=len(x1)
#lhs
X1=a*x1
X2=b*x2
X=X1+X2
print(dft(X,k))
#rhs
y1=a*dft(x1,k)
y2=b*dft(x2,k)
Y=y1+y2
print(Y)


