import numpy as np
import matplotlib.pyplot as plt

# Signal generation
fm = 50
t = np.arange(0, 0.1, 0.0001)
sig = np.sin(2 * np.pi * fm * t)

plt.plot(t, sig)
plt.title("SIGNAL")
plt.show()

# Sampling
fs = 16 * fm
ts = np.arange(0, 0.1, 1 / fs)
samp = np.sin(2 * np.pi * fm * ts)

plt.plot(ts, samp, '*-')
plt.title("Sampled")
plt.show()

# Quantization
L = 8
mini = min(sig)
maxi = max(sig)
q_lvl = np.linspace(mini, maxi, L + 1)
q_sig = np.digitize(samp, q_lvl) - 1
quant = q_lvl[q_sig] + ((q_lvl[1] - q_lvl[0]) / 2)

plt.plot(ts, quant, '*-')
plt.title("Quantized")
plt.show()

# Encoding with variable bit length
bitno = int((np.log2(L)))  # Number of bits needed to represent L levels
encoded = [format(code, f'0{bitno}b') for code in q_sig]

# Plot Quantized Signal with Binary Codes
plt.plot(ts, quant, '*-')
for i, (x, y) in enumerate(zip(ts, quant)):
    plt.text(x, y, encoded[i])
plt.title("Quantized  Binary Encoding")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

# Print encoded binary sequence
print("Encoded binary sequence:")
print(' '.join(encoded))
