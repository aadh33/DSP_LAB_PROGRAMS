import numpy as np
import matplotlib.pyplot as plt

#CT Signal
t = np.arange(-10,10,0.01)
y = np.copy(t)
y[y<0] = 0
plt.plot(t,y)

plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()


#DT signal
n = np.arange(-5, 6)
x = np.zeros_like(5)
y = np.zeros_like(5)
x= np.zeros(5)
y = np.arange(6)
z = np.concatenate([x,y])
plt.stem(n, z)
plt.xticks(n);
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
