import matplotlib.pyplot as plt
import numpy as np

def get_filter(T, rolloff):
    def rc(t, beta):
        # Simplified raised cosine function without error handling
        return np.sinc(t) * np.cos(np.pi * beta * t) / (1 - (2 * beta * t) ** 2)
    
    # Return the lambda function as the filter
    return lambda t: rc(t / T, rolloff)

T = 1  # Time period
Fs = 100  # Sampling frequency
g = get_filter( T, 1)
binary_sequence = np.random.randint(0,2, size=50)  # Generating random binary data
j = binary_sequence * 2 - 1  # NRZ
t = np.arange(-2 * T, (len(j) + 2) * T, 1 / Fs)
y = sum(j[k] * g(t - k * T) for k in range(len(j)))  # Convolution


fig, ax = plt.subplots(2, 2, figsize=(9.5, 6))
ax[0][1].plot(t, y)
ax[0][1].set_title("Pulse Shaping")
x = np.arange(-T, T, 1 / Fs)

for i in range(2 * Fs, len(y) - 3 * Fs, Fs):
    ax[1][1].plot(x, y[i:i + 2 * Fs], 'red')

ax[1][1].set_title("Eye Diagram")
ax[0][0].step(np.arange(len(binary_sequence)), binary_sequence)
ax[0][0].set_title("Binary Message")
t_impulse = np.arange(-5, 5, 0.01)
ax[1][0].plot(t_impulse, g(t_impulse))
ax[1][0].set_title("Impulse Response RC")
plt.show()

'''
t = np.arange(-2 * T, (len(j) + 2) * T, 1 / Fs): This line creates a time vector t that starts at
 -2 * T and ends at (len(j) + 2) * T, with steps of 1 / Fs. Here’s what each part means:
-2 * T: The time vector starts 2 periods before the first symbol. 
This is to accommodate the filter’s impulse response, which extends before and after the symbol period.
(len(j) + 2) * T: The time vector ends 2 periods after the last symbol, ensuring that the tail
 of the filter’s impulse response is included.
1 / Fs: This is the step size, which is the inverse of the sampling frequency. 
It determines how many samples per second are taken, which defines the resolution of your time vector.

y = sum(j[k] * g(t - k * T) for k in range(len(j))): This line performs the convolution of the binary
 sequence j with the raised cosine filter g. Here’s what’s happening:
j[k]: This is the k-th element of your binary sequence, which has been mapped to NRZ (Non-Return-to-Zero)
 levels where ‘0’ maps to ‘-1’ and ‘1’ maps to ‘1’.
g(t - k * T): This applies the raised cosine filter at a delay corresponding to the k-th symbol period.
 The filter is shifted in time by k * T, where T is the symbol period.
sum(...): The sum function adds up all the individual filtered symbols to produce the final signal y. 
This is essentially what convolution does: it combines the effect of all symbols on the signal through the filter.
The result is a signal y that represents your binary sequence after being shaped by
 the raised cosine filter. This signal can then be used to generate an eye diagram,
 which helps visualize potential intersymbol interference and overall signal quality.
 
 
 
 
 range(2 * Fs, len(y) - 3 * Fs, Fs): This creates a range of indices for the signal y that we will use to plot the eye diagram.
2 * Fs: We start plotting two symbol periods into the signal to avoid the transient effects at the beginning.
len(y) - 3 * Fs: We stop plotting three symbol periods before the end of the signal to avoid transient effects at the end.
Fs: We increment by one symbol period each time. This means we plot one “eye” for each symbol period.
ax[1][1].plot(x, y[i:i + 2 * Fs], 'blue'): This plots a segment of the signal y on the subplot ax[1][1].
x: This is a time vector that spans one symbol period. It’s used as the x-axis for plotting.


y[i:i + 2 * Fs]: This is a slice of the signal y that starts at index i and extends for two symbol periods. We take two symbol periods to show how one symbol transitions to the next.
'blue': This sets the color of the plotted line to blue.
By looping through and plotting these slices on top of each other, we can see how consistently the signal transitions from one state to another. If there is little overlap between these slices, it indicates that there is little intersymbol interference and that the signal is clean. If there is a lot of overlap, it indicates potential issues with signal quality.
'''