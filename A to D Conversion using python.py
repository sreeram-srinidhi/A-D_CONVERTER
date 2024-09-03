import numpy as np
import matplotlib.pyplot as plt

# Parameters
time_of_view = 1.0  # seconds
sampling_rate = 100  # Hz
quantizing_bits = 8  # Number of quantizing bits

# Generate time samples
num_samples = int(time_of_view * sampling_rate)
time_samples = np.linspace(0, time_of_view, num_samples, endpoint=False)

# Generate analog signal (sine wave in this case)
frequency = 5  # Frequency of the sine wave
analog_signal = np.sin(2 * np.pi * frequency * time_samples)

# Calculate quantization parameters
quantizing_levels = 2 ** quantizing_bits
quantizing_step = 2 / quantizing_levels

# Perform quantization
quantized_signal = np.round(analog_signal / quantizing_step) * quantizing_step

# Convert quantized signal to digital signal (0s and 1s)
digital_signal = np.where(quantized_signal >= 0, 1, 0)

# Plotting
fig, axs = plt.subplots(4, 1, figsize=(10, 8))

# Plot analog signal
axs[0].plot(time_samples, analog_signal, label='Analog Signal')
axs[0].set_title('Analog Signal')
axs[0].set_xlabel('Time')
axs[0].set_ylabel('Amplitude')
axs[0].legend()

# Plot sampled signal
axs[1].stem(time_samples, analog_signal, linefmt='b-', markerfmt='ro', basefmt='b-', label='Sampled Signal')
axs[1].set_title('Sampled Signal')
axs[1].set_xlabel('Time')
axs[1].set_ylabel('Amplitude')
axs[1].legend()

# Plot quantized signal
axs[2].stem(time_samples, quantized_signal, markerfmt='rs', basefmt='r-', label='Quantized Signal')
axs[2].set_title('Quantized Signal (A/D Conversion)')
axs[2].set_xlabel('Time')
axs[2].set_ylabel('Quantized Values')
axs[2].legend()

# Plot digital signal
axs[3].stem(time_samples, digital_signal, markerfmt='go', basefmt='g-', label='Digital Signal')
axs[3].set_title('Digital Signal')
axs[3].set_xlabel('Time')
axs[3].set_ylabel('Digital Values')
axs[3].legend()

plt.tight_layout()
plt.show()
