import numpy as np
import matplotlib.pyplot as plt


# Parameters
num_symbols = 10 #Number of bits (symbols) to transmit.
sps = 8  # Samples per symbol
bits = np.random.randint(0, 2, num_symbols)  # Random bit sequence

# Generate pulse train
x = np.array([])
for bit in bits:
    pulse = np.zeros(sps)
    pulse[0] = bit * 2 - 1  # Convert bit to +1 or -1
    x = np.concatenate((x, pulse)) # Append the pulse to the signal

# Plot the pulse train
plt.figure(0)
plt.plot(x, '.-')
plt.title("Pulse Train")
plt.grid(True)
plt.show()

# Create raised-cosine filter
num_taps = 101 # Length of the filter.
beta = 0.35 #Roll-off factor that determines the shape of the filter.
Ts = sps  # Symbol period in terms of samples
t = np.arange(-50, 51)  # Time vector for filter

# Calculate raised-cosine filter coefficients
h = (1 / Ts) * np.sinc(t / Ts) * np.cos(np.pi * beta * t / Ts) / (1 - (2 * beta * t / Ts)**2)

# Handle division by zero at t = 0
h[np.isnan(h)] = np.pi / 4  # This value comes from the limit of the formula as t approaches 0
#whenever you encounter an impossible calculation (like dividing by zero), just use 0.785 instead.”
# Plot the raised-cosine filter
plt.figure(1)
plt.plot(t, h, '.')
plt.title("Raised-Cosine Filter")
plt.grid(True)
plt.show()

# Apply pulse shaping
x_shaped = np.convolve(x, h, mode='same')  # Convolve and keep the same length

# Plot the shaped signal
plt.figure(2)
plt.plot(x_shaped, '.-')
for i in range(num_symbols):
    plt.plot([i * sps + num_taps // 2, i * sps + num_taps // 2], [0, x_shaped[i * sps + num_taps // 2]], 'r-')
plt.title("Shaped Signal with Sample Points")
plt.grid(True)
plt.show()
