#Experiment-1 Error Perfomance of BPSK
import numpy as np 
import matplotlib.pyplot as plt 
message_frequency = 10 
carrier_frequency = 20 
sampling_frequency = 30 * carrier_frequency # To satisfy Nyquist
#Creates an array of time points
t = np.arange(0, 4/carrier_frequency, 1/sampling_frequency) 
#Generates a cosine wave as the message signal, adds Gaussian noise to it, and then converts it into a binary signal using the sign function
message = np.sign(np.cos(2 * np.pi * message_frequency * t) + 
np.random.normal(scale = 0.01, size = len(t))) 
#Generates a cosine wave as the carrier signal.
carrier = np.cos(2 * np.pi * sampling_frequency/carrier_frequency * t) 
#Multiplies the carrier signal with the message signal to generate the BPSK modulated signal.
modulated_signal = carrier * message 
plt.figure(figsize=(8, 6)) 
plt.subplot(3, 1, 1) 
plt.plot(t, message) 
plt.subplot(3, 1, 2) 
plt.plot(t, carrier) 
plt.subplot(3, 1, 3) 
plt.plot(t, modulated_signal)
plt.show() 

plt.plot(t, message) 
plt.plot(t, modulated_signal, "--") 
plt.plot(t, carrier, ".") 
plt.show()



#Number of bits to simulate, which provides a good balance between accuracy and computational efficiency.
N = 500000
#An array of Eb/N0 values in dB to simulate over.
EbN0dB_list = np.arange(0, 50)
#An empty list to store the calculated BER values for each Eb/N0.
BER = []

for i in range(len(EbN0dB_list)):
    EbN0dB = EbN0dB_list[i]
    EbN0 = 10**(EbN0dB/10)
#Random BPSK Signal Generation    
    x = np.random.choice([-1, 1], size=N)
    noise = 1/np.sqrt(2 * EbN0)
    channel = x + np.random.randn(N) * noise
    received_x = np.sign(channel)
#Counts the number of bit errors.    
    errors = (x != received_x).sum()
    BER.append(errors/N)

plt.plot(EbN0dB_list, BER, "-")
plt.axis([0, 14, 1e-7, 0.1])
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
