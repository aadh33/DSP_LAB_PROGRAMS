import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T = 1  # Symbol duration (or bit period)
Fs = 1000  # Sampling frequency (samples per second)
beta = 1  # Roll-off factor for the raised cosine filter

# Define the raised cosine filter impulse response
def g(t):
    numerator = np.sinc(t) * np.cos(np.pi * beta * t)
    denominator = 1 - (2 * beta * t) ** 2
    return numerator / denominator

# Original binary data sequence
binary_sequence = np.random.randint(0, 2, 50)

# Convert binary sequence to NRZ format (1 -> +1, 0 -> -1)
j = np.array(binary_sequence) * 2 - 1  # NRZ encoding

# Define the time vector for the signal
t = np.arange(-2 * T, (len(j) + 2) * T, 1 / Fs)

# Generate the pulse-shaped signal by convolving NRZ bits with the raised cosine filter
y = sum(j[k] * g(t - k * T) for k in range(len(j)))

# Plot only the eye diagram
plt.figure(figsize=(10, 6))

# Generate the eye diagram
x = np.arange(-T, T, 1 / Fs)
for i in range(2 * Fs, len(y) - 3 * Fs, Fs):
    plt.plot(x, y[i:i + 2 * Fs], 'blue')

plt.title("Eye Diagram")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)

# Display the eye diagram
plt.show()
