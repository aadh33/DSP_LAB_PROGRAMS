import numpy as np
import matplotlib.pyplot as plt
#CT signal

t = np.linspace(-1, 1, 400)


impulse_signal = np.zeros_like(t)
impulse_signal[t == 0] = 1  # Impulse at t=0


plt.figure(figsize=(8, 4))
plt.plot(t, impulse_signal, label='Impulse Signal')
plt.title('Continuous-Time Impulse Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.grid(True)
plt.legend()
plt.show()

#DT signal
n = np.arange(-5, 6)
x = np.zeros_like(n)
x[n == 0] = 1
plt.stem(n, x)
plt.xticks(n);
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)



