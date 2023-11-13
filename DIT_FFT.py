import numpy as np
x=np.array(input("Enter the sequence:").split(",")).astype(complex)
def dit_fft(x):
    N=len(x)
    if N<=1:
        return x
    even=dit_fft(x[0::2])
    odd=dit_fft(x[1::2])
    T=[np.exp(-2j*np.pi*k/N)*odd[k] for k in range(N//2)]
    return[even[k]+T[k] for k in range (N//2)]+[even[k]-T[k] for k in range(N//2)]
def dit_ifft(X):
    N=len(X)
    if N<=1:
        return X
    even=dit_ifft(X[0::2])
    odd=dit_ifft(X[1::2])
    T=[np.exp(2j*np.pi*k/N)*odd[k] for k in range (N//2)]
    return[(even[k]+T[k])/2 for k in range (N//2)]+[(even[k]-T[k])/2 for k in range(N//2)]
X_dit_fft=dit_fft(x)
x_dit_ifft=dit_ifft(X_dit_fft)
print("DIT-FFT:",X_dit_fft)
print("DIT-IFFT:",x_dit_ifft)


