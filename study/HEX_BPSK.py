# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 11:56:57 2024

@author: adith
"""

# -*- coding: utf-8 -*-

# BPSK WITH PHASE:

import numpy as np
import matplotlib.pyplot as plt

# Convert hexadecimal to binary
hex_num = 'D6D2'
binary = bin(int(hex_num, 16))[2:]

# Ensure the binary string has length multiple of 4 (each hex digit is 4 bits)
binary = binary.zfill(len(hex_num) * 4)

# Function to generate cosine wave
def cosineWave(f, overSamplingRate, nCycles, phase):
    fs = overSamplingRate * f
    t = np.arange(0, nCycles * 1/f, 1/fs)
    g = np.cos(2 * np.pi * f * t + phase)
    return g

# Parameters
fm = 10  # Modulation frequency (bits per second)
fc = 30  # Carrier frequency (Hz)
overSamplingRate = 20
fs = overSamplingRate * fc  # Sampling rate

# Define modulation signals for '0' and '1'
mod_0 = cosineWave(fc, overSamplingRate, fc/fm, 2*np.pi/3)
mod_1 = cosineWave(fc, overSamplingRate, fc/fm, 5*np.pi/18)

# Generate modulated signal
modulated_signal = []
for bit in binary:
    if bit == '0':
        modulated_signal.extend(mod_0)
    elif bit == '1':
        modulated_signal.extend(mod_1)

# Time vector
t = np.arange(0, len(binary) * 1/fm, 1/fs)

# Plot modulated signal
plt.figure(figsize=(14, 6))
plt.plot(t, modulated_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title(f"BPSK Modulated Signal for Hexadecimal {hex_num}")
plt.grid(True)
plt.show()
