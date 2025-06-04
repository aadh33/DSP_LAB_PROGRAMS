import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import sawtooth

# Parameters
sampling_rate = 1000  # Sampling rate in Hz
duration = 1.0       # Duration of the signal in seconds
frequency = 5        # Frequency of the sawtooth wave in Hz

# Time vector using np.arange
t = np.arange(0, duration, 1/sampling_rate)

# Generate sawtooth wave
signal = sawtooth(2 * np.pi * frequency * t)

# Quantization function using np.digitize
def quantize(signal, levels):
    min_val, max_val = signal.min(), signal.max()
    bins = np.linspace(min_val, max_val, levels + 1)
    digitized = np.digitize(signal, bins) - 1
    quantized_signal = bins[digitized] + (bins[1] - bins[0]) / 2
    return quantized_signal

# Function to calculate SNR
def calculate_snr(original_signal, quantized_signal):
    signal_power = np.mean(original_signal**2)
    noise_power = np.mean((original_signal - quantized_signal)**2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# Levels for quantization
levels = [2, 4, 8, 16, 32]
snr_values = []

# Quantize the signal and calculate SNR for each level
for L in levels:
    quantized_signal = quantize(signal, L)
    snr = calculate_snr(signal, quantized_signal)
    snr_values.append(snr)

# Plotting SNR vs Levels
plt.figure(figsize=(10, 6))
plt.plot(levels, snr_values, marker='o')
plt.xscale('log')  # Use logarithmic scale for levels
plt.xlabel('Number of Quantization Levels (L)')
plt.ylabel('SNR (dB)')
plt.title('SNR vs Number of Quantization Levels')
plt.grid(True)
plt.show()
