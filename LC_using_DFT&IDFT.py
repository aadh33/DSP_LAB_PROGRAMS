import numpy as np


x1=np.array(input("Enter the seqeunce of x1:").split(",")).astype(int)
x2=np.array(input("Enter the seqeunce of x2:").split(",")).astype(int)

x11=x1
x22=x2

L=len(x1)+len(x2)-1

x1=np.pad(x1,(0,(L-len(x1))))
x2=np.pad(x2,(0,(L-len(x2))))

X1=np.fft.fft(x1)
X2=np.fft.fft(x2)

y=(np.fft.ifft(X1*X2))


print("The result of linear convolution using circular convolution from dft and idft is:",y)
print("The result of linear convolution using in-built python function is:",np.convolve(x11,x22))

