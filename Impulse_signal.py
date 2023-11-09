import numpy as np
import matplotlib.pyplot as plt


def discrete_impulse(n):
    return np.where(n == 0, 1, 0)

# Generate time vector for discrete time
n_discrete = np.arange(-5, 6)

# Generate the discrete impulse signal
impulse_discrete = discrete_impulse(n_discrete)

# Plot discrete impulse signal
plt.figure()
plt.stem(n_discrete, impulse_discrete, use_line_collection=True)
plt.title('Discrete-time Impulse Signal')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()


