import matplotlib.pyplot as plt
import numpy as np

def get_filter(name, T, rolloff=None):
    def rc(t, beta):
        # Handle the case where denominator becomes zero
        with np.errstate(divide='ignore', invalid='ignore'):
            result = np.sinc(t) * np.cos(np.pi * beta * t) / (1 - (2 * beta * t) ** 2)
            result[np.isnan(result)] = np.pi * beta / (2 * np.sqrt(2))  # limit value when t = 1/(2*beta)
        return result
    
    # Ensure rolloff is not None
    if rolloff is None: 
        
        raise ValueError("Rolloff factor must be specified for raised cosine filter.")
    
    return lambda t: rc(t / T, rolloff)  # Impulse response to minimize ISI

T = 1  # Time period
Fs = 100  # Sampling frequency
g = get_filter('rc', T, 0.7)
binary_sequence = np.random.randint(2, size=50)  # Generating random binary data
j = binary_sequence * 2 - 1  # NRZ
t = np.arange(-2 * T, (len(j) + 2) * T, 1 / Fs)
y = sum(j[k] * g(t - k * T) for k in range(len(j)))  # Convolution

fig, ax = plt.subplots(2, 2)
ax[0][1].plot(t, y)
ax[0][1].set_title("Pulse Shaping")
x = np.arange(-T, T, 1 / Fs)

for i in range(2 * Fs, len(y) - 3 * Fs, Fs):
    ax[1][1].plot(x, y[i:i + 2 * Fs], 'blue')

ax[1][1].set_title("Eye Diagram")
ax[0][0].step(np.arange(len(binary_sequence)), binary_sequence)
ax[0][0].set_title("Binary Message")
t_impulse = np.arange(-5, 5, 0.01)
ax[1][0].plot(t_impulse, g(t_impulse))
ax[1][0].set_title("Impulse Response RC")
plt.show()