import numpy as np
x=np.array(input("Enter the sequence:").split(",")).astype(complex)
def dif_fft(x):
    N=len(x)
    if N<=1:
        return x
    even=dif_fft(x[0::2])
    odd=dif_fft(x[1::2])
    T=[np.exp(-2j*np.pi*k/N) for k in range(N//2)]
    return[even[k]+T[k] * odd[k] for k in range (N//2)]+[even[k]-T[k] * odd[k] for k in range(N//2)]
def dif_ifft(X):
    N=len(X)
    if N<=1:
        return X
    even=dif_ifft(X[0::2])
    odd=dif_ifft(X[1::2])
    T=[np.exp(2j*np.pi*k/N) for k in range (N//2)]
    return[(even[k]+T[k]*odd[k])/2 for k in range (N//2)]+[(even[k]-T[k]*odd[k])/2 for k in range(N//2)]
X_dif_fft=dif_fft(x)
x_dif_ifft=dif_ifft(X_dif_fft)
print("DIF-FFT:",X_dif_fft)
print("DIF-IFFT:",x_dif_ifft)




