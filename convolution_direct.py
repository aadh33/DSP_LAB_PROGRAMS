

import numpy as np

x=np.array(input("Enter the elements of the input sequence:").split(",")).astype(int)
h=np.array(input("Enter the elements of the impulse response:").split(",")).astype(int)
xn=x
hn=h
total=len(x)+len(h)-1
y=np.zeros(total)
if len(x)<len(h):
    (x,h)=(h,x)
if len(x)!=len(h):
    if len(x)>len(h):
        z=np.zeros(len(x)-len(h)).astype(int)
        h=np.concatenate((h,z))
size=len(x)
for i in range(total):
    sum=0
    for j in range(size):
        w=i-j
        if(w<0) or (w>size-1):
            sum+=0
        else:
            sum+=x[j]*h[w]
    y[i]=sum
print("The output sequence(using mathematical function)is:",y.astype(int))
print("The output sequence (using numpy.convolve)is:",np.convolve(xn,hn))
   