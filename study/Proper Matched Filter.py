import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square #you can use any signal


fm = 10
fs = 30*fm
t = np.arange(0,4/fm,1/fs)

message = np.sign(square(2*np.pi*fm*t))  
plt.subplot(2,1,1)
plt.plot(t,message)


message_flip = np.sign(np.flip(square(2*np.pi*fm*(t))))

final = np.convolve(message,message_flip)
plt.subplot(2,1,2)
plt.plot(final)  
plt.show()