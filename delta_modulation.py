import numpy as np
import matplotlib.pyplot as plt

# Input Parameters
sampling_frequency = float(input("Enter sampling frequency: "))
signal_duration = float(input("Enter signal duration: "))
time = np.arange(signal_duration * sampling_frequency) / sampling_frequency

freq_cosine = float(input("Enter the frequency of the cosine component: "))
freq_sine = float(input("Enter the frequency of the sine component: "))
amp_cosine = float(input("Enter the amplitude of the cosine component: "))
amp_sine = float(input("Enter the amplitude of the sine component: "))

# Signal Generation
cosine_signal = amp_cosine * np.cos(2 * np.pi * freq_cosine * time)
sine_signal = amp_sine * np.sin(2 * np.pi * freq_sine * time)
message_signal = cosine_signal + sine_signal

# Signal Bandwidth and Sampling Frequency for Delta Modulation
signal_bandwidth = max(freq_cosine, freq_sine)
nyquist_rate = float(input("Enter the nyquist_rate: "))
dm_sampling_frequency = nyquist_rate * 2 * signal_bandwidth
dm_step_size = float(input("Enter the step size (epsilon) for delta modulation: "))

# Delta Modulation Time and Signal Sampling
dm_time = np.arange(signal_duration * dm_sampling_frequency) / dm_sampling_frequency
sampled_cosine = amp_cosine * np.cos(2 * np.pi * freq_cosine * dm_time)
sampled_sine = amp_sine * np.sin(2 * np.pi * freq_sine * dm_time)
sampled_message = sampled_cosine + sampled_sine

# Delta Modulation Process
predicted_signal = np.zeros(len(sampled_message)) 
modulation_output = np.zeros_like(predicted_signal)

for i in range(1, len(sampled_message)):
    amp_diff = sampled_message[i] - predicted_signal[i - 1]
    modulation_output[i] = (2 * int(amp_diff > 0) - 1) * dm_step_size
    predicted_signal[i] = predicted_signal[i - 1] + modulation_output[i]

# Decoding (Reconstructing) the Signal
decoded_signal = np.zeros(len(modulation_output))
for i in range(1, len(modulation_output)):
    decoded_signal[i] = decoded_signal[i - 1] + modulation_output[i]

# Plotting
plt.figure(figsize=(20, 15))
display_time = 0.1

# First Plot - Original and Delta-Modulated Signals
plt.subplot(3, 1, 1)
plt.plot(time, message_signal, color='black', label='Original Message')
plt.step(dm_time, predicted_signal, color='red', where='post', label='Predicted Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Delta-Modulated Signals')
plt.legend()
plt.xlim(0, display_time)
plt.ylim(min(message_signal) - 0.5, max(message_signal) + 0.5)
plt.xticks(np.arange(0, display_time, display_time / 10))
plt.grid()

# Second Plot - Delta Modulation Output
plt.subplot(3, 1, 2)
plt.stem(dm_time, modulation_output, linefmt='r', markerfmt='ro', basefmt='k')
plt.xlabel('Time (s)')
plt.ylabel('Step Amplitude')
plt.title('Delta Modulation Output')
plt.xlim(0, display_time)
plt.ylim(-2 * dm_step_size, 2 * dm_step_size)
plt.xticks(np.arange(0, display_time, display_time / 10))
plt.grid()

# Third Plot - Decoded Signal vs. Original Message Signal
plt.subplot(3, 1, 3)
plt.plot(time, message_signal, color='black', label='Original Message')
plt.step(dm_time, decoded_signal, color='blue', where='post', label='Decoded Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Decoded Signal (Reconstructed) vs. Original Message')
plt.legend()
plt.xlim(0, display_time)
plt.ylim(min(message_signal) - 0.5, max(message_signal) + 0.5)
plt.xticks(np.arange(0, display_time, display_time / 10))
plt.grid()

plt.tight_layout()
plt.show()

