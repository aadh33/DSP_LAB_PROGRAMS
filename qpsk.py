import numpy as np
import matplotlib.pyplot as plt

def cosineWave(f, overSamplingRate, nCycles, phase):
    fs = overSamplingRate * f
    t = np.arange(0, nCycles * 1/f, 1/fs)
    g = np.cos(2 * np.pi * f * t + phase)
    return list(g)

fm = 10
fc = 30
overSamplingRate = 20
fs = overSamplingRate * fc
x = np.random.rand(30) >= 0.5
str_x = [str(int(i)) for i in x]
x = "".join(str_x)
print("Message string: {}".format(x))

message = [x[2*i : 2*(i+1)] for i in range(int(len(x)/2))]
print("Message string grouped as combinations of 2 bits each: {}".format(message))

mod_00 = cosineWave(fc, overSamplingRate, fc/fm, 7*np.pi/12  )
mod_01 = cosineWave(fc, overSamplingRate, fc/fm, np.pi/12)
mod_10 = cosineWave(fc, overSamplingRate, fc/fm, -7*np.pi/12)
mod_11 = cosineWave(fc, overSamplingRate, fc/fm, -np.pi/12)

modulated_signal = []
for i in message:
    if i == '00':
        modulated_signal += mod_00
    if i == '01':
        modulated_signal += mod_01
    if i == '10':
        modulated_signal += mod_10
    if i == '11':
        modulated_signal += mod_11

t = np.arange(0, (len(x)/2) * 1/fm, 1/fs)
print(len(t), len(modulated_signal))

plt.figure(figsize=(28, 6))
plt.plot(t, modulated_signal)
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.title("Modulated signal")
plt.grid(True)
plt.show()

# Error performance of QPSK
N = 500000
EbN0dB_list = np.arange(0, 50)
BER = []

for i in range(len(EbN0dB_list)):
    EbN0dB = EbN0dB_list[i]
    EbN0 = 10**(EbN0dB/10)
    x = np.random.rand(N) >= 0.5
    x_str = [str(int(i)) for i in x]
    x_str = "".join(x_str)
    message = [x_str[2*i : 2*(i+1)] for i in range(int(len(x)/2))]
   
    noise = 1/np.sqrt(2 * EbN0)
  
    channel = x + np.random.randn(N) * noise
    received_x = channel >= 0.5
    xReceived_str = [str(int(i)) for i in received_x]
    xReceived_str = "".join(xReceived_str)
    messageReceived = [xReceived_str[2*i : 2*(i+1)] for i in range(int(len(x)/2))]
    message = np.array(message)
    messageReceived = np.array(messageReceived)
    errors = (message != messageReceived).sum()
    BER.append(errors/N)

print(BER)

plt.plot(EbN0dB_list, BER, "-", EbN0dB_list, BER, "go")
plt.xscale('linear')
plt.yscale('log')
plt.grid()
plt.xlabel("EbN0 in dB")
plt.ylabel("BER")
plt.title("BER in BPSK")
plt.show()
