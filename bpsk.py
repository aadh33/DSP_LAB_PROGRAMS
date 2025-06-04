import numpy as np
import matplotlib.pyplot as plt



def generate_message_signal(t, message_frequency):
    message = np.sign(np.cos(2 * np.pi * message_frequency * t) +
                      np.random.normal(scale=0.01, size=len(t)))
    return message


def generate_carrier_signal(t, sampling_frequency, carrier_frequency):
    carrier = np.cos(2 * np.pi * sampling_frequency / carrier_frequency * t)
    return carrier


def generate_modulated_signal(message, carrier):
    modulated_signal = carrier * message
    return modulated_signal


message_frequency = 10
carrier_frequency = 20
sampling_frequency = 30 * carrier_frequency


t = np.arange(0, 4 / carrier_frequency, 1 / sampling_frequency)


message = generate_message_signal(t, message_frequency)
carrier = generate_carrier_signal(t, sampling_frequency, carrier_frequency)
modulated_signal = generate_modulated_signal(message, carrier)


plt.figure(figsize=(8, 6))

plt.subplot(3, 1, 1)
plt.plot(t, message)

plt.subplot(3, 1, 2)
plt.plot(t, carrier)

plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal)

plt.show()
plt.plot(t, message)
plt.plot(t, modulated_signal, "--")
plt.plot(t, carrier, "-")

plt.show()