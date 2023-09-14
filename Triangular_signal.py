import numpy as np
import matplotlib.pyplot as plt
#CT Signal

t = np.linspace(-2, 2, 400)

triangular_pulse_signal = np.zeros_like(t)
triangular_pulse_signal[(t >= -1) & (t <= 0)] = 1 + t[(t >= -1) & (t <= 0)]
triangular_pulse_signal[(t > 0) & (t <= 1)] = 1 - t[(t > 0) & (t <= 1)]


plt.figure(figsize=(8, 4))
plt.plot(t, triangular_pulse_signal, label='Triangular Pulse Signal')
plt.title('Continuous-Time Triangular Pulse Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()


#DT Signal
a = np.arange(6)
b = np.arange(4, -1, -1)
x = np.concatenate([a, b])


plt.stem(x)
plt.xticks(np.arange(11));
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
