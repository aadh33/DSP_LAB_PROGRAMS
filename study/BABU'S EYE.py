import numpy as np
import matplotlib.pyplot as plt

# Define parameters
T = 1  # Symbol duration (or bit period)
Fs = 1000 # Sampling frequency (samples per second)
beta = 0.2  # Roll-off factor for the raised cosine filter

# Define the raised cosine filter impulse response
g = lambda t: np.sinc(t) * np.cos(np.pi * beta * t) / (1 - (2 * beta * t) ** 2)

# Original binary data sequence
binary_sequence =  np.random.randint(0, 2, 50)

# Convert binary sequence to NRZ format (1 -> +1, 0 -> -1)
j = np.array(binary_sequence) * 2 - 1  # NRZ encoding
print(j)

# Define the time vector for the signal
t = np.arange(-2 * T, (len(j) + 2) * T, 1 / Fs)

# Generate the pulse-shaped signal by convolving NRZ bits with the raised cosine filter
y = sum(j[k] * g(t - k * T) for k in range(len(j)))

# Create a 2x2 grid of subplots
fig, ax = plt.subplots(2, 2)

# Plot the original binary message as a step function
ax[0][0].step(np.arange(len(binary_sequence)), binary_sequence)
ax[0][0].set_title("Binary message")

# Plot the impulse response of the raised cosine filter
t = np.arange(-5, 5, 0.01)
ax[1][0].plot(t, g(t))
ax[1][0].set_title("Impulse response rc")

# Plot the pulse-shaped signal
ax[0][1].plot(y)
ax[0][1].set_title("Pulse shaped Signal")

# Generate the eye diagram
x = np.arange(-T, T, 1 / Fs)
for i in range(2 * Fs, len(y) - 3 * Fs, Fs):
    ax[1][1].plot(x, y[i:i + 2 * Fs], 'blue')

ax[1][1].set_title("Eye diagram")

# Display all plots
plt.show()
