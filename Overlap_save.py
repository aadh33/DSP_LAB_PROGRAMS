import numpy as np

def overlap_save_convolution(x,h,N):
    M=len(h)
    L=N-M+1
    x_pad=np.concatenate((x,np.zeros(N-1)))
    h_pad=np.concatenate((h,np.zeros(N-M)))
    y=np.zeros(len(x)+M-1)
    for i in range(0,len(x),L):
        x_seg=x_pad[i:i+N]
        X=np.fft.fft(x_seg)
        H=np.fft.fft(h_pad,N)
        Y=X*H
        y_seg=np.fft.ifft(Y)
        y[i:i+N]+=np.real(y_seg)
    return y
    
x=np.array(input("Enter sequence x:").split(",")).astype(int)
h=np.array(input("Enter sequence h:").split(",")).astype(int)
N=len(x)+len(h)-1
result=overlap_save_convolution(x,h,N)
print(result)
print(np.convolve(x,h))

