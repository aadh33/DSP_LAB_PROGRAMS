import numpy as np
import matplotlib.pyplot as plt

#CT Signal
t = np.linspace(-2, 2, 400)


bipolar_pulse_signal = np.zeros_like(t)
bipolar_pulse_signal[(t >= -1) & (t <= 1)] = 1
bipolar_pulse_signal[(t >= -1.5) & (t <= -0.5)] = -1


plt.plot(t, bipolar_pulse_signal, label='Bipolar Pulse Signal')
plt.title('Continuous-Time Bipolar Pulse Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()

#DT Signal

n = np.arange(-5, 6)
x = np.zeros_like(n)
x[(n >= -3) & (n < 0) ] = -1
x[(n >= 0) & (n < 3) ] = 1
plt.stem(n, x)
plt.xticks(n);
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()
