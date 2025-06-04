# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 22:52:32 2024

@author: adith
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc

# Define the range of SNR values in dB
snr_db_range = np.linspace(0, 10, 100)

# Calculate BER for BPSK and QPSK using erfc
ber_bpsk_values = 0.5 * erfc(np.sqrt(10 ** (snr_db_range / 10)))
ber_qpsk_values = 0.5 * erfc(np.sqrt(0.5 * 10 ** (snr_db_range / 10)))

# Plot the results
plt.figure(figsize=(10, 6))
plt.semilogy(snr_db_range, ber_bpsk_values, 'b-', label='BPSK')
plt.semilogy(snr_db_range, ber_qpsk_values, 'r--', label='QPSK')
plt.xlabel('SNR (dB)')
plt.ylabel('Bit Error Rate (BER)')
plt.title('BER vs SNR for BPSK and QPSK')
plt.legend()
plt.grid(True, which='both', linestyle='--')

plt.show()
