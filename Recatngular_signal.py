import numpy as np
import matplotlib.pyplot as plt
#CT signal
t = np.arange(-10,10,0.01)
print("Enter the width of the rectangle:")
T = float(input())
y = np.zeros(len(t))
y[np.all([(t>=-T/2), (t<=T/2)], axis = 0)]=1
plt.plot(t, y)
plt.show()


#DT Signal
n = np.arange(-5, 6)
x = np.zeros_like(n)
x[(n >= 0) & (n <= 4) ] = 1
plt.stem(n, x)
plt.xticks(n);