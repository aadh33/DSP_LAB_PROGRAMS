import numpy as np
import matplotlib.pyplot as plt

N = 5000000
EbNodB_range = range(0, 15)
ber = []

for EbNodB in EbNodB_range:
    EbNo = 10.0**(EbNodB/10.0)
    
    # BPSK modulation
    x = 2 * (np.random.rand(N) >= 0.5) - 1
    
    # AWGN channel
    noise_std = 1/np.sqrt(2*EbNo)
    y = x + noise_std * np.random.randn(N)
    
    # Demodulation and error counting
    y_d = 2 * (y >= 0) - 1
    errors = np.sum(x != y_d)
    print(errors)
    # Calculate Bit Error Rate (BER) and store
    ber.append(1.0 * errors / N)
print(ber)
# Plotting
plt.semilogy(EbNodB_range, ber, 'bo-')
plt.xlabel('Eb/N0 (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.grid(True)
plt.title('BPSK Modulation with AWGN Channel')
plt.show()
