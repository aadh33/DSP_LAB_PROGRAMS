import numpy as np
import matplotlib.pyplot as plt

def cosineWave(f, overSamplingRate, nCycles, phase):
    fs = overSamplingRate * f
    t = np.arange(0, nCycles*1/f, 1/fs)
    g = np.cos(2 * np.pi * f * t + phase)
    return list(g)

fm = 10 #Sets the message frequency
fc = 30 #carrier frequency
overSamplingRate = 20

fs = overSamplingRate * fc
#Message Generation: Generate a random binary message of length 30,
# convert it to a string, and print it.
x = ''.join(np.random.choice(['0', '1'], size=30))

#print("Message string : {}".format(x))
message = [x[i:i+2] for i in range(0, len(x), 2)]
#print("Message string grouped as combinations of 2 bits each : 
#{}".format(message))

mod_00 = cosineWave(fc, overSamplingRate, fc/fm, 3*np.pi/4)
mod_01 = cosineWave(fc, overSamplingRate, fc/fm, np.pi/4)
mod_10 = cosineWave(fc, overSamplingRate, fc/fm, -3*np.pi/4)
mod_11 = cosineWave(fc, overSamplingRate, fc/fm, -np.pi/4)

modulated_signal = []
for i in message:
    if i == '00':
        modulated_signal.extend(mod_00)
    elif i == '01':
        modulated_signal.extend(mod_01)
    elif i == '10':
        modulated_signal.extend(mod_10)
    elif i == '11':
        modulated_signal.extend(mod_11)

t = np.arange(0, (len(x)/2) * 1/fm, 1/fs)
"""
stop: The end point, calculated as (len(x)/2) * 1/fm. 
Since each pair of bits in x corresponds to one QPSK symbol
and each symbol lasts for 1/fm seconds, the total duration is half the length of x times the symbol duration.
step: The time step between each point in the array,
which is 1/fs, where fs is the sampling frequency.

"""
plt.figure(figsize=(28, 6))
plt.plot(t, modulated_signal) # Ensure t and signal are same length
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Modulated signal")
plt.grid(True)
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt

def cosineWave(f, overSamplingRate, nCycles, phase):
    fs = overSamplingRate * f
    t = np.arange(0, nCycles*1/f, 1/fs)
    g = np.cos(2 * np.pi * f * t + phase)
    return list(g)

def qpsk_modulation(binary_sequence, fm=10, fc=30, overSamplingRate=20):
    # Ensure the length of binary_sequence is even
    if len(binary_sequence) % 2 != 0:
        raise ValueError("Binary sequence length must be even.")
    

    # Sampling frequency
    fs = overSamplingRate * fc
    
    # Split the binary sequence into pairs of bits
    message = [binary_sequence[i:i+2] for i in range(0, len(binary_sequence), 2)]
    
    # Generate the modulated signals for each pair of bits
    mod_00 = cosineWave(fc, overSamplingRate, fc/fm, 3*np.pi/4)
    mod_01 = cosineWave(fc, overSamplingRate, fc/fm, np.pi/4)
    mod_10 = cosineWave(fc, overSamplingRate, fc/fm, -3*np.pi/4)
    mod_11 = cosineWave(fc, overSamplingRate, fc/fm, -np.pi/4)
    
    modulated_signal = []
    for i in message:
        if i == '00':
            modulated_signal += mod_00
        elif i == '01':
            modulated_signal += mod_01
        elif i == '10':
            modulated_signal += mod_10
        elif i == '11':
            modulated_signal += mod_11
    
    # Time array for plotting
    t = np.arange(0, (len(binary_sequence)/2) * 1/fm, 1/fs)
    
    # Plot the modulated signal
    plt.figure(figsize=(28, 6))
    plt.plot(t, modulated_signal)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.title("Modulated signal")
    plt.grid(True)
    plt.show()

# Prompt the user for input
binary_sequence = input("Enter a binary sequence: ")
qpsk_modulation(binary_sequence)

'''

"""
In QPSK, each pair of bits is represented by a unique phase of the carrier wave. 
These lines create the modulated signals corresponding to each possible pair of bits 
by calling the cosineWave function with the carrier frequency (fc), oversampling rate,
the ratio of carrier to message frequency (fc/fm), and the respective phase 
shift for each symbol
"""
