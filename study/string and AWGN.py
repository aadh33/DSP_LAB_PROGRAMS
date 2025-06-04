import numpy as np

# Generate the message string
message_string = '0246'
# Repeat the message for 5 cycles
message = message_string * 5

# Define signal parameters
amplitude = 1.0  # Amplitude of the baseband signal
EbN0_dB = 10     # Energy per bit to noise power spectral density ratio in dB
N = len(message) # Number of bits in the message

# Convert message string to binary representation
binary_message = ''.join(format(ord(char), '08b') for char in message)

# Convert binary message to array of integers
binary_array = np.array([int(bit) for bit in binary_message])

# Generate AWGN channel noise
EbN0 = 10 ** (EbN0_dB / 10) # Convert Eb/N0 from dB to linear
noise_power = 1 / EbN0       # Noise power spectral density
noise = np.sqrt(noise_power) * np.random.randn(N * 8) # Generate Gaussian noise

# Add noise to the signal
received_signal = binary_array + noise

# Thresholding to detect errors
received_signal[received_signal >= 0.5] = 1
received_signal[received_signal < 0.5] = 0

# Convert received signal back to string
received_message = ''.join([str(int(bit)) for bit in received_signal])

# Calculate number of errors
num_errors = np.sum(np.abs(binary_array - received_signal))

# Print results
print("Original Message:", message)
print("Received Message:", received_message)
print("Number of Errors:", num_errors)