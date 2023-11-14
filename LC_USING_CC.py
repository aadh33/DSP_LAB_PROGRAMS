import numpy as np


x1=np.array(input("Enter the seqeunce of x1:").split(",")).astype(int)
x2=np.array(input("Enter the seqeunce of x2:").split(",")).astype(int)

L=len(x1)+len(x2)-1
x1=np.pad(x1,(0,(L-len(x1))))
x2=np.pad(x2,(0,(L-len(x2))))



k=len(x1)
z=x1

for i in range(k-1):
    x1=np.roll(x1,1)

    z=np.concatenate((z,x1))

z=z.reshape(k,k)

z=np.transpose(z)

ans=np.dot(z,x2)
print("The result of linear convolution using circular convolution using matrix method is:",ans)

