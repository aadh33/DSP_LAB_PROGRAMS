# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:37:23 2024

@author: adith
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
message_frequency = 10
carrier_frequency = 20
sampling_frequency = 30 * carrier_frequency  # To satisfy Nyquist
A = 1  # Amplitude

# Time vector
t = np.arange(0, 4 / carrier_frequency, 1 / sampling_frequency)

# Generate a random binary message
message_bits = np.random.randint(0, 2, int(len(t) / (sampling_frequency / carrier_frequency)))
message = np.repeat(message_bits, int(sampling_frequency / carrier_frequency))

# Map bits to BPSK symbols (-A for 0, 2A for 1)
message_symbols = np.where(message == 1, -A, 2 * A)

# Generate carrier signal
carrier = np.cos(2 * np.pi * carrier_frequency * t)

# Generate BPSK modulated signal
modulated_signal = carrier * message_symbols

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message_symbols, color='blue')
plt.title('BPSK Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, carrier, color='green')
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, color='red')
plt.title('BPSK Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Overlay plot
plt.figure(figsize=(10, 4))
plt.plot(t, message_symbols, label='Message Signal', color='blue')
plt.plot(t, modulated_signal, '--', label='BPSK Modulated Signal', color='red')
plt.plot(t, carrier, '.', label='Carrier Signal', color='green')
plt.title('Overlay of BPSK Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
