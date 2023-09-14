import numpy as np
import matplotlib.pyplot as plt
#CT Signal
#sampling rate = sr
sr = 44100.0
# sampling interval = ts
ts = 1.0/sr
t = np.arange(0,1,ts)
# frequency of the signal
my_freq = float(input("Enter the frequency: "))
y = np.sin(2*np.pi*my_freq*t)


plt.figure(figsize = (6, 4))
plt.title('frequency = '+str(my_freq)+ ' Hz')
plt.plot(t, y)
plt.ylabel('Amplitude')
plt.xlabel('Time (sec)')
plt.show()

#DT Signal


n = np.arange(0, 10) 


frequency = 0.2  
amplitude = 1.0


discrete_sine_wave = amplitude * np.sin(2 * np.pi * frequency * n)


plt.stem(n, discrete_sine_wave, basefmt=' ', markerfmt='bo', linefmt='b-', label='Sine Wave')
plt.title('Discrete-Time Sine Wave')
plt.xlabel('Time (n)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.show()

