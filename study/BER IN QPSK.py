import numpy as np
import matplotlib.pyplot as plt

# Error performance of QPSK
#
N = 500000

EbN0dB_list = np.arange(0, 50)
#Initializes an empty list to store the Bit Error Rate (BER) values for each ( E_b/N_0 ) value.
BER = []

for EbN0dB in EbN0dB_list:
    EbN0 = 10**(EbN0dB/10)
    x = np.random.rand(N) >= 0.5
    noise = 1/np.sqrt(2 * EbN0)
    channel = x + np.random.randn(N) * noise
    received_x = channel >= 0.5
    errors = (x != received_x).sum()
    BER.append(errors/N)

print(BER)
plt.plot(EbN0dB_list, BER, "-", EbN0dB_list, BER, "go")
plt.xscale('linear')
plt.yscale('log')
plt.grid()
plt.xlabel("Eb/N0 in dB")
plt.ylabel("BER")
plt.title("BER in QPSK")
plt.show()

"""
Core Concepts:

QPSK (Quadrature Phase Shift Keying): A digital modulation scheme where two bits are represented by one symbol with four possible phase shifts.
( E_b/N_0 ): The energy per bit to noise power spectral density ratio, a key factor in determining the performance of a digital communication system.

BER (Bit Error Rate): The percentage of bits that have errors relative to the total number of bits sent in a transmission.

Gaussian Noise: A type of statistical noise having a probability density function equal to that of the normal distribution, which is also known as Gaussian distribution.
The code simulates a QPSK communication system’s performance over a range of ( E_b/N_0 ) values by calculating and plotting its BER.
"""
# Creates an array of ( E_b/N_0 ) values in dB, ranging from 0 to 49.
"""
The range of ( E_b/N_0 ) values in dB is chosen up to 50 to provide a 
wide range of signal-to-noise ratios (SNRs) for the simulation. 
This allows us to observe the performance of the QPSK system under 
various noise conditions, from very poor (low ( E_b/N_0 )) to
 very good (high ( E_b/N_0 )).
 In practice, a range up to 50 dB covers most practical
 communication scenarios, from noisy channels to almost noise-free channels.
 It helps in understanding how the BER decreases as the SNR improves, 
 which is a fundamental characteristic of digital communication systems.
"""