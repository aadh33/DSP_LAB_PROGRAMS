import numpy as np
import matplotlib.pyplot as plt

# Define message signal parameters
time = np.arange(0, 0.1, 0.0001)
mssg_f = 100 #message frequency
dc = 2  #dc offset

sig = np.sin(2 * np.pi * mssg_f * time) + dc #Sine wave signal
 
# Plot the basic message signal
plt.plot(time, sig)
plt.title("Signal")
plt.show()

# Sampling
fs = 16 * mssg_f  #Nyquist Criteria and factor of 16 is used for high resolution data representation 
ts = np.arange(0, 0.1, 1/fs) # Corrected to match the message signal duration
sampled_signal = dc + np.sin(2 * np.pi * mssg_f * ts)#sampled_signal is the actual sampled signal. We take our original message signal formula and apply it to our sampling time array ts. This gives us the values of our message signal at each point in time that we decided to sample

# Plot sampled signal
plt.plot(ts, sampled_signal, "r.-")
plt.title("Sampled Signal")
plt.show()

# Quantization
L = 4
sig_min = min(sig)
sig_max = max(sig)
q_levels = np.linspace(sig_min, sig_max,L +1)
q_sig = np.digitize(sampled_signal, q_levels) -1
quantized_signal = q_levels[q_sig] + (q_levels[1] - q_levels[0]) / 2


"""
The function np.digitize maps each value in sampled_signal to an index that corresponds
 to the interval of q_levels it falls into. Since Python uses 0-based indexing, 
 we subtract 1 to align with our quantization levels array.
"""

# Plot quantized signal
plt.plot(ts, quantized_signal, "b", ts, quantized_signal, "m*")
'''The command is used to plot the quantized signal. It plots the signal twice:
    once as a continuous blue line ("b") and once as magenta stars ("m*") at 
    the sample points. This helps to visualize both the overall trend of the 
    quantized signal and the individual quantized values at each sampling time.

'''
plt.title("Quantized Signal")
plt.show()

# Encoding
bit_no = int(np.log2(L))
encoded_signal = [format(code, f'0{bit_no}b') for code in q_sig]
"""
This part of the list comprehension iterates over each element in the q_sig list. 
Each element, referred to as code, represents a quantization level index.
For each code, the format function is used to convert it into a binary string.
 The format specifier f'0{bit_no}b' tells Python to format the number as binary (b),
 with leading zeros (0) to make up the width specified by bit_no.
 This ensures that all binary strings have the same length,
 equal to the number of bits necessary to represent the largest quantization level index.
"""
# Plot encoded signal
plt.plot(ts, encoded_signal, "b", ts, encoded_signal, "g*")
plt.title("Encoded Signal")
plt.show()

print("Binary Coded Signal:", encoded_signal)

# Quantization Noise Calculation
q_noise = quantized_signal - sampled_signal

# Plot quantization noise
plt.plot(ts, q_noise)
plt.title("Quantization Noise")
plt.show()

# SNR Calculation
p_signal = np.mean(sig**2)#p_signal calculates the average power of the original signal (sig). Power is defined as the mean (average) of the squared signal values. Squaring the signal values ensures that all values are positive and emphasizes larger values.
p_noise = np.mean(q_noise**2)#p_noise calculates the average power of the quantization noise (q_noise). Quantization noise is the difference between the original signal and the quantized signal. It represents the error introduced by quantization.
snr = p_signal / p_noise#snr is the ratio of signal power to noise power. A higher SNR indicates a cleaner signal with less noise.
snr_db = 10 * np.log10(snr)# converts the SNR ratio to a logarithmic scale measured in decibels (dB)

print("Signal-to-Noise ratio in dB: ", snr_db)

# SNR vs Number of bits per symbol
snr_db_list = []
for R in range(1, 11):
    L = 2**R #For each bit number R, L calculates the number of quantization levels, which is (2^R). This is because each bit can represent two states, so R bits can represent (2^R) different states or levels.
    step_size = (sig_max - sig_min) / L
    power_noise = (step_size**2) / 12  # Corrected formula for quantization noise power for uniform quantizer
    snr = p_signal / power_noise
    snr_db_list.append(10 * np.log10(snr))

# Plot SNR vs Number of bits per symbol
plt.plot(range(1, 11), snr_db_list, "r*-")
plt.xlabel("Number of Bits per symbol")
plt.ylabel("SNR in dB")
plt.title("SNR vs Number of bits per symbol")
plt.show()
