# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:05:43 2024

@author: adith
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:53:53 2024

@author: adith
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Parameters
fs = 1000          # Sampling rate in Hz
duration = 1.0     # Duration of the signal in seconds
frequency = 5      # Frequency of the sawtooth wave in Hz

# Time vector using np.arange
t = np.arange(0, duration, 0.001)

# Generate sawtooth wave
signal = sawtooth(2 * np.pi * frequency * t)

# Sampling
ts = np.arange(0, duration, 1/fs)
samp = sawtooth(2 * np.pi * frequency * ts)

# Quantization function using np.digitize
def quantize(signal, levels):
    min_val, max_val = min(signal), max(signal)
    bins = np.linspace(min_val, max_val, levels +1)
    digitized = np.digitize(signal, bins) - 1
    quantized_signal = bins[digitized] + (bins[1] - bins[0]) / 2
    return quantized_signal

# Quantize to 2, 4, and 8 levels
quantized_signal_2 = quantize(signal, 2)
quantized_signal_4 = quantize(signal, 4)
quantized_signal_8 = quantize(signal, 8)

# Plotting
plt.figure(figsize=(15, 12))

plt.subplot(5, 1, 1)
plt.plot(t, signal, label='Original Sawtooth Wave')
plt.title('Original Sawtooth Wave')
plt.legend()

plt.subplot(5, 1, 2)
plt.plot(t, quantized_signal_2, label='Quantized to 2 levels', color='r')
plt.title('Quantized to 2 levels')
plt.legend()

plt.subplot(5, 1, 3)
plt.plot(t, quantized_signal_4, label='Quantized to 4 levels', color='g')
plt.title('Quantized to 4 levels')
plt.legend()

plt.subplot(5, 1, 4)
plt.plot(t, quantized_signal_8, label='Quantized to 8 levels', color='b')
plt.title('Quantized to 8 levels')
plt.legend()

plt.subplot(5, 1, 5)
plt.plot(ts, samp, 'o-', color='r', label='Sampled Sawtooth Wave')
plt.title('Sampled Sawtooth Wave')
plt.legend()

plt.tight_layout()
plt.show()
