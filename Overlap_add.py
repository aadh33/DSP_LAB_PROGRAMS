
import numpy as np
def overlap_add_conv(x,h):
    N=len(h)
    print(N ,'\n')
    L=len(x)+len(h)-1
    print(L,'\n')
    N_fft=2**(int(np.ceil(np.log2(L))))
    print(N_fft ,'\n')
    X=np.fft.fft(np.pad(x,(0,N_fft-len(x))))
    print(X ,'\n')
    H=np.fft.fft(np.pad(h,(0,N_fft-N)))
    print(H,'\n')
    Y=X*H
    print(Y ,'\n')
    y=np.real(np.fft.ifft(Y))
    print(y ,'\n')
    y=y[:L]
    return y
x=np.array(input("Enter x:").split(",")).astype(int)
h=np.array(input("Enter h:").split(",")).astype(int)
print("Using overlap_add:",overlap_add_conv(x,h))
print("Using function:",np.convolve(x,h))


