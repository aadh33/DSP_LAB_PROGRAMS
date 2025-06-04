import numpy as np
import matplotlib.pyplot as plt

# Parameters
message_frequency = 10
carrier_frequency = 20
sampling_frequency = 30 * carrier_frequency  # To satisfy Nyquist
A = 1  # Amplitude

# Time vector
t = np.arange(0, 4 / carrier_frequency, 1 / sampling_frequency)

# Generate a cosine message signal with noise+++
message =np.sign( np.cos(2 * np.pi * message_frequency * t) + np.random.normal(scale=0.1, size=len(t)))

# Convert the message signal into binary (-A for negative, 2A for positive)
message_symbols = np.where(message ==1, 2 * A, -A)

# Generate carrier signal
carrier = np.cos(2 * np.pi * carrier_frequency * t)

# Generate BPSK modulated signal
modulated_signal = carrier * message_symbols

# Plotting
plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.plot(t, message, color='blue')
plt.title('Cosine Message Signal with Noise')
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
plt.plot(t, message_symbols, label='BPSK Message Symbols', color='blue')
plt.plot(t, modulated_signal, '--', label='BPSK Modulated Signal', color='red')
plt.plot(t, carrier, '.', label='Carrier Signal', color='green')
plt.title('Overlay of BPSK Signals')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
