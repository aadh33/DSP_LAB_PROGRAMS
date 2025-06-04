# Monte Carlo Simulation
import numpy as np
import matplotlib.pyplot as plt

#Number of bits to simulate, which provides a good balance between accuracy and computational efficiency.
N = 500000
#An array of Eb/N0 values in dB to simulate over.
EbN0dB_list = np.arange(0, 50)
#An empty list to store the calculated BER values for each Eb/N0.
BER = []

for i in range(len(EbN0dB_list)):
    EbN0dB = EbN0dB_list[i]
    EbN0 = 10**(EbN0dB/10)
#Random BPSK Generation    
    x = 2 * (np.random.rand(N) >= 0.5) - 1
    noise = 1/np.sqrt(2 * EbN0)
    channel = x + np.random.randn(N) * noise
    received_x = 2 * (channel >= 0) - 1  # Corrected threshold from 0.5 to 0
#Adding the errors    
    errors = (x != received_x).sum()
    BER.append(errors/N)
    
    
    
plt.plot(EbN0dB_list, BER, "-", EbN0dB_list, BER, "go")
plt.axis([0, 14, 1e-6, 0.1])
#This sets the x-axis range from 0 to 14 dB for Eb/N0. 
#It’s a common range for plotting BER curves because it typically covers the range of interest where changes in BER are most noticeable
#This sets the y-axis range from (10^{-7}) to (0.1) for BER. The lower limit is set to (10^{-7}) because BER values lower than this are often considered excellent and may not be distinguishable on a log scale. The upper limit is set to (0.1) because BER values higher than this are generally considered poor, and the system would not be functioning effectively.
#These ranges are chosen to provide a clear view of the BER performance over a practical range of signal-to-noise ratios, which is useful for analyzing and optimizing communication systems.
plt.xscale('linear')
plt.yscale('log')
plt.grid()
plt.xlabel("Eb/N0 in dB")
plt.ylabel("BER")
plt.title("BER in BPSK")
plt.show()
