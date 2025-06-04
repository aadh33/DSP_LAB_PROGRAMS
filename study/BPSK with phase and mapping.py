# -*- coding: utf-8 -*-

# BPSK WITH PHASE

import numpy as np
import matplotlib.pyplot as plt

# Convert decimal to BCD and then to binary
decimal_number = 123
A = 1
binary = ''.join(format(int(digit), '04b') for digit in str(decimal_number))
print("Binary representation (BCD) of", decimal_number, ":", binary)

# Convert binary string to message symbols
message_symbols = np.array([int(bit) for bit in binary])
message_symbols = np.where(message_symbols == 1, 2 * A, -A)
print("Message symbols:", message_symbols)

# Function to generate cosine wave
def cosineWave(f, overSamplingRate, nCycles, phase):
    fs = overSamplingRate * f
    t = np.arange(0, nCycles * 1/f, 1/fs)
    g = np.cos(2 * np.pi * f * t + phase)
    return list(g)

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
for symbol in message_symbols:
    if symbol == -A:
        modulated_signal.extend(mod_0)
    elif symbol == 2 * A:
        modulated_signal.extend(mod_1)

# Time vector
t = np.arange(0, len(binary) * 1/fm, 1/fs)

# Plot modulated signal
plt.figure(figsize=(14, 6))
plt.plot(t, modulated_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("BPSK Modulated Signal for BCD 123")
plt.grid(True)
plt.show()

