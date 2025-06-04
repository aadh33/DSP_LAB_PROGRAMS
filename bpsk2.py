import numpy as np
import matplotlib.pyplot as plt
message_frequency = 10
carrier_frequency = 20
sampling_frequency = 30 * carrier_frequency
t = np.arange(0, 4/carrier_frequency, 1/sampling_frequency)
message = np.sign(np.cos(2 * np.pi * message_frequency * t) + 
np.random.normal(scale = 0.01, size = len(t)))
carrier = np.cos(2 * np.pi * sampling_frequency/carrier_frequency * t) 
modulated_signal = carrier * message
plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1) 
plt.plot(t, message) 
plt.subplot(3, 1, 2) 
plt.plot(t, carrier) 
plt.subplot(3, 1, 3) 
plt.plot(t,modulated_signal) 
plt.show()
plt.plot(t, message)
plt.plot(t, modulated_signal, "--") 
plt.plot(t, carrier, "-") 
plt.show()

