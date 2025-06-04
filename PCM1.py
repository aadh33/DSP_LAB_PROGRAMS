import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# Message signal generation
fm = 100
dc_offset = 2
t = np.arange(0, 5/fm, 0.0001)
x = np.sin(2 * pi * fm * t) + dc_offset

plt.figure(figsize=(8, 6))
plt.plot(t, x)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Message Signal")
plt.grid(True)
plt.show()

# Sampling
fs = 30 * fm
t = np.arange(0, 5/fm, 1/fs)
xSampled = np.sin(2 * pi * fm * t) + dc_offset

plt.plot(t, xSampled, "bo-")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Sampled Message Signal")
plt.grid(True)
plt.show()

# SNR Calculation
max_bits = 10
snr_eqn_dB = np.zeros(max_bits)
for L in range(1, max_bits + 1):
    quantizationLevels = np.linspace(min(xSampled), max(xSampled), 2**L)
    step_size = (max(xSampled) - min(xSampled)) / (2**L)

    # Quantization
    xQuantized = np.zeros_like(xSampled)
    for i, sample in enumerate(xSampled):
        closest_level = min(quantizationLevels, key=lambda x: abs(x - sample))
        xQuantized[i] = closest_level

    # Calculate SNR
    quantizationNoise = xQuantized - xSampled
    snr_eqn_dB[L-1] = 20 * np.log10(np.sqrt(12) * (max(xSampled) - min(xSampled)) / (2 * step_size))

# Plot SNR vs. Number of Bits per Symbol
plt.plot(range(1, max_bits + 1), snr_eqn_dB, "r*-")
plt.xlabel("Number of Bits per symbol")
plt.ylabel("SNR in dB")
plt.title("SNR vs. Number of Bits per Symbol")
plt.grid(True)
plt.show()
