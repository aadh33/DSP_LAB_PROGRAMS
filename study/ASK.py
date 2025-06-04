# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:51:07 2024

@author: adith
"""
import numpy as np
import matplotlib.pyplot as plt

# Parameters
message_frequency = 10  # Frequency of the message signal
carrier_frequency = 20  # Frequency of the carrier signal
sampling_frequency =100 # Sampling frequency
A = 1  # Amplitude for '1' in ASK
duration = 1  # Duration in seconds

# Time vector
t = np.arange(0, duration, 1 / sampling_frequency)

# Generate a binary message signal
message_bits = np.random.randint(0, 2, int(duration * message_frequency))

message_signal = np.repeat(message_bits, int(sampling_frequency / message_frequency))

# Map binary to ASK symbols (0 to 0, 1 to A)
ask_signal = message_signal * A

# Generate carrier signal
carrier = np.cos(2 * np.pi * carrier_frequency * t)

# Generate ASK modulated signal
modulated_signal = carrier * ask_signal

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, ask_signal, color='blue')
plt.title('ASK Message Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 2)
plt.plot(t, carrier, color='green')
plt.title('Carrier Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, color='red')
plt.title('ASK Modulated Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# Overlay plot
plt.figure(figsize=(10, 4))
plt.plot(t, ask_signal, label='ASK Message Signal', color='blue')
plt.plot(t, modulated_signal, '--', label='ASK Modulated Signal', color='red')
plt.plot(t, carrier, '.', label='Carrier Signal', color='green')
plt.title('Overlay of ASK Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()

