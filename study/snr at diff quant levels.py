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


# Quantize to 2, 4, and 8 levels
quantized_signal_2 = quantize(signal, 2)
quantized_signal_4 = quantize(signal, 4)
quantized_signal_8 = quantize(signal, 8)

p_signal = np.mean(signal**2)
p_noise_2 = np.mean((signal - quantized_signal_2)**2)
p_noise_4 = np.mean((signal - quantized_signal_4)**2)
p_noise_8 = np.mean((signal - quantized_signal_8)**2)

snr_2 = p_signal / p_noise_2
snr_4 = p_signal / p_noise_4
snr_8 = p_signal / p_noise_8

snr_db_2 = 10 * np.log10(snr_2)
snr_db_4 = 10 * np.log10(snr_4)
snr_db_8 = 10 * np.log10(snr_8)

# Plot SNR values
plt.figure(figsize=(8, 6))
plt.plot([2, 4, 8], [snr_db_2, snr_db_4, snr_db_8], marker='o', color='b', label='SNR (dB)')
plt.xlabel('Quantization Levels')
plt.ylabel('SNR')
plt.title('SNR for Different Quantization Levels')
plt.grid(True)
plt.legend()

plt.show()