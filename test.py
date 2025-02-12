import numpy as np
import matplotlib.pyplot as plt

# Define parameters
A = 1  # Amplitude
frequencies = [500, 1000, 10000]  # Frequencies in Hz
sampling_rates = [500, 1000, 5000, 50000]  # Sampling frequencies in Hz
time_interval = (-0.01, 0.01)  # Shortened time range in seconds to show oscillations

# Plot signals
plt.figure(figsize=(10, 8))

for i, f in enumerate(frequencies):
    for j, fs in enumerate(sampling_rates):
        if fs < 2 * f:
            continue  # Skip cases where fs is less than 2*f (Nyquist criterion)
        
        t = np.linspace(time_interval[0], time_interval[1], int(fs * (time_interval[1] - time_interval[0])))
        x_t = A * np.sin(2 * np.pi * f * t)
        
        plt.subplot(len(frequencies), len(sampling_rates), i * len(sampling_rates) + j + 1)
        plt.plot(t, x_t, label=f'f={f}Hz, fs={fs}Hz')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.grid()

plt.suptitle('Plot of A sin(2πft) for different frequencies and sampling rates')
plt.tight_layout()
plt.show()
