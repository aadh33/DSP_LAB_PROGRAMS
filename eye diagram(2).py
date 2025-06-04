import numpy as np
import matplotlib.pyplot as plt
def get_filter(name, T, rolloff=None):
    def rc(t, beta):
        return np.sinc(t) * np.cos(np.pi * beta * t) / (1 - (2 * beta * t) ** 2)
    if name == 'rc':
        return lambda t: rc(t / T, rolloff)
T = 1
Fs = 100
g = get_filter("rc", T,1)
#print(g(2))
binary_sequence = [0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0]
j=np.array(binary_sequence) * 2 - 1
print(j)
t = np.arange(-2 * T, (len(j) + 2) * T, 1 / Fs)
y = sum(j[k] * g(t - k * T) for k in range(len(j))) 
fig, ax = plt.subplots(2, 2)
ax[0][1].plot(t, y)
ax[0][1].set_title("pulse Signal")
x = np.arange(-T, T, 1 / Fs)
for i in range(2 * Fs, len(y) - 3 * Fs, Fs):
    ax[1][1].plot(x, y[i:i + 2 * Fs], 'blue')
ax[1][1].set_title("Eye diagram")
ax[0][0].step(np.arange(len(binary_sequence)), binary_sequence)
ax[0][0].set_title("Binary message")
t = np.arange(-5, 5, 0.01)
ax[1][0].plot(t, g(t))
ax[1][0].set_title("impulse response rc")
plt.show()
