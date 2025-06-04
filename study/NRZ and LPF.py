import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Parameters
binary_sequence = [1, 0, 0, 1, 0, 1, 1, 0, 1, 0]
bit_duration = 1  # duration of each bit in seconds
sampling_rate = 1000  # samples per second (Hz)
snr_dB = 10  # signal-to-noise ratio in dB
cutoff_freq = 10  # cutoff frequency of the LPF in Hz

# Step 1: Generate NRZ Unipolar Signal
nrz_signal = np.repeat(binary_sequence, bit_duration * sampling_rate)

# Step 2: Add AWGN Noise
snr_linear = 10**(snr_dB / 10)
signal_power = np.mean(nrz_signal**2)
noise_power = signal_power / snr_linear
noise = np.sqrt(noise_power) * np.random.normal(size=len(nrz_signal))
noisy_signal = nrz_signal + noise

# Step 3: Low Pass Filter using Butterworth filter
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

filtered_signal = butter_lowpass_filter(noisy_signal, cutoff_freq, sampling_rate)

# Plot the signals
time = np.arange(len(nrz_signal)) / sampling_rate

plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(time, nrz_signal, label='NRZ Unipolar Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('NRZ Unipolar Signal')
plt.grid()

plt.subplot(3, 1, 2)
plt.plot(time, noisy_signal, label='Noisy Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Noisy Signal (AWGN)')
plt.grid()

plt.subplot(3, 1, 3)
plt.plot(time, filtered_signal, label='Filtered Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Filtered Signal (Butterworth LPF)')
plt.grid()

plt.tight_layout()
plt.show()
