import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
frequency = 5  # Frequency of the sine wave in Hz
sampling_rate_nyquist = 2 * frequency  # Nyquist rate
sampling_rate_under = 1.5 * frequency  # Under-sampling (less than Nyquist rate)
sampling_rate_over = 4 * frequency  # Over-sampling (more than Nyquist rate)
t = np.linspace(0, 2, 1000)  # Time vector for two seconds

# Generate the sine wave
sine_wave = np.sin(2 * np.pi * frequency * t)

# Sample the sine wave at different rates
samples_nyquist = np.sin(2 * np.pi * frequency * np.arange(0, 2, 1/sampling_rate_nyquist))
samples_under = np.sin(2 * np.pi * frequency * np.arange(0, 2, 1/sampling_rate_under))
samples_over = np.sin(2 * np.pi * frequency * np.arange(0, 2, 1/sampling_rate_over))

# Plotting the original and sampled sine waves
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.stem(np.arange(0, 2, 1/sampling_rate_nyquist), samples_nyquist, 'r', markerfmt='ro', label='Nyquist Rate Samples')
plt.legend()
plt.title('Sampling at Nyquist Rate')

plt.subplot(3, 1, 2)
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.stem(np.arange(0, 2, 1/sampling_rate_under), samples_under, 'g', markerfmt='go', label='Under-sampling Rate Samples')
plt.legend()
plt.title('Under-sampling')

plt.subplot(3, 1, 3)
plt.plot(t, sine_wave, label='Original Sine Wave')
plt.stem(np.arange(0, 2, 1/sampling_rate_over), samples_over, 'b', markerfmt='bo', label='Over-sampling Rate Samples')
plt.legend()
plt.title('Over-sampling')

plt.xlabel('Time [s]')
plt.tight_layout()
plt.show()
