import numpy as np
import matplotlib.pyplot as plt
x = np.array([float(i) for i in input("Enter space seperated sequence: ").split(' ')])
t0 = float(input("Enter shifting factor: "))
A = float(input("Enter Scale factor: "))
t = np.linspace(min(0, t0-1),max(t0+1, len(x)),len(x))
print('The original sequence is = ',x)
plt.plot(t, x)
plt.plot(-t, x)
plt.plot(t+t0, x)
plt.plot(t, A*x)
plt.plot(t+t0, A*x)
plt.legend(["Original", "Reversed", f"Shifted by{t0}", f"Scaled by {A}", "Shifted and Scaled"])
plt.ylabel('Amplitude')
plt.xlabel('Time (sec)')
plt.show()

