##Core Concepts:

# BPSK is a type of phase modulation that uses two phases to represent binary digits (0s and 1s).
# It’s widely used in wireless communications due to its simplicity and robustness against noise.
# Applications:

# BPSK is used in applications like satellite communication, RFID, and Bluetooth technology.
# Remember to ensure proper indentation in your code for it to run correctly.

import numpy as np 
import matplotlib.pyplot as plt 
message_frequency = 10 
carrier_frequency = 20 
sampling_frequency = 30 * carrier_frequency # To satisfy Nyquist
#Creates an array of time points
t = np.arange(0, 4/carrier_frequency, 1/sampling_frequency) 


#Generates a cosine wave as the message signal, adds Gaussian noise to it, and then converts it into a binary signal using the sign function
message =np.sign(np.cos(2 * np.pi * message_frequency * t) + 
np.random.normal(scale = 0.01, size = len(t))) 


#Generates a cosine wave as the carrier signal.
carrier = np.cos(2 * np.pi *sampling_frequency/ carrier_frequency * t) #perfection in simulationSS


#Multiplies the carrier signal with the message signal to generate the BPSK modulated signal.
modulated_signal = carrier * message 
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
plt.plot(t, carrier, ".") 
plt.show()

# =============================================================================
# 
# =============================================================================

# The np.random.normal function is used to generate random numbers from a normal (Gaussian) distribution. Here’s what each parameter means in the context of your code:

# scale = 0.01: This sets the standard deviation of the normal distribution to 0.01. In signal processing, this value represents the amplitude of the noise. A smaller scale value means less noise, and a larger value means more noise.
# size = len(t): This determines the number of random numbers to generate, which in this case is equal to the length of your time array t. This ensures that you have a noise value for each point in time for your message signal.
# When you add this noise to your message signal, it simulates real-world conditions where signals are often corrupted by random noise. In BPSK and other communication systems, understanding and mitigating the effects of noise is crucial for reliable data transmission.
'''
The 4/carrier_frequency in the code defines the duration over 
which the signal is generated. It ensures that the time array t covers at 
least four cycles of the carrier wave, which helps in visualizing
 the modulation effect properly when plotting. The number 4 is arbitrary 
 and can be changed depending on how many cycles you want to observe in your plot.
 It’s chosen to provide a clear view of both the message and carrier signals over a few cycles
 
'''



'''
import numpy as np 
import matplotlib.pyplot as plt 

# Ask user for a binary sequence input
binary_sequence = input("Enter a binary sequence: ")

# Convert the string input to a list of integers (0s and 1s)
message = np.array([int(bit) for bit in binary_sequence])

# Extend the message to match the length of time array t
repeated_message = np.repeat(message, sampling_frequency/message_frequency)

carrier_frequency = 20 
sampling_frequency = 30 * carrier_frequency # To satisfy Nyquist

# Create an array of time points
t = np.arange(0, len(repeated_message)/sampling_frequency, 1/sampling_frequency) 

# Generate a cosine wave as the carrier signal.
carrier = np.cos(2 * np.pi * carrier_frequency * t) 

# Multiply the carrier signal with the extended message signal to generate the BPSK modulated signal.
modulated_signal = carrier * repeated_message

plt.figure(figsize=(8, 6)) 
plt.subplot(3, 1, 1) 
plt.plot(t[:len(message)], message) 
plt.subplot(3, 1, 2) 
plt.plot(t, carrier) 
plt.subplot(3, 1, 3) 
plt.plot(t, modulated_signal)
plt.show() 

plt.plot(t[:len(message)], message) 
plt.plot(t, modulated_signal, "--") 
plt.plot(t, carrier, ".") 
plt.show()

'''