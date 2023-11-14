#toeplitz_method

import numpy as np
x=np.array(input("Enter the elements of the input sequence:").split(",")).astype(int)
h=np.array(input("Enter the elements of the impulse response:").split(",")).astype(int)


hn=h
row=len(x)
column=len(x)+len(h)-1
if len(h)<column:
    z=np.zeros(column-len(h))
    h=np.concatenate((h,z))
toeplitz=h
for i in range(row-1):
    h=np.roll(h,1)
    toeplitz=np.concatenate((toeplitz,h))
toeplitz.shape=(row,column)
toeplitz=np.transpose(toeplitz)
print(toeplitz)
print("The output sequence(using toeplitz matrix)is:",np.dot(toeplitz,x).astype(int))
print("The output sequence (using numpy.convolve)is:",np.convolve(x,hn))
