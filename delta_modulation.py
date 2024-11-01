import numpy as np
import matplotlib.pyplot as plt

sampling_frequency = float(input("Enter sampling frequency: "))
signal_duration = float(input("Enter signal duration: "))
time = np.arange(signal_duration * sampling_frequency) / sampling_frequency

freq_cosine = float(input("Enter the frequency of the cosine component: "))
freq_sine = float(input("Enter the frequency of the sine component: "))
amp_cosine = float(input("Enter the amplitude of the cosine component: "))
amp_sine = float(input("Enter the amplitude of the sine component: "))

cosine_signal = amp_cosine * np.cos(2 * np.pi * freq_cosine * time)
sine_signal = amp_sine * np.sin(2 * np.pi * freq_sine * time)
message_signal = cosine_signal + sine_signal

signal_bandwidth = max(freq_cosine, freq_sine)

nyquist_rate = float(input("Enter the nyquist_rate: "))

dm_sampling_frequency = nyquist_rate * 2 * signal_bandwidth

dm_step_size = float(input("Enter the step size (epsilon) for delta modulation: "))

dm_time = np.arange(signal_duration * dm_sampling_frequency) / dm_sampling_frequency

sampled_cosine = amp_cosine * np.cos(2 * np.pi * freq_cosine * dm_time)
sampled_sine = amp_sine * np.sin(2 * np.pi * freq_sine * dm_time)
sampled_message = sampled_cosine + sampled_sine

predicted_signal = np.zeros(len(sampled_message)) 
modulation_output = np.zeros_like(predicted_signal)

for i in range(1, len(sampled_message)):
    amp_diff = sampled_message[i] - predicted_signal[i - 1]
    modulation_output[i] = (2 * int(amp_diff > 0) - 1) * dm_step_size
    predicted_signal[i] = predicted_signal[i - 1] + modulation_output[i]

bin_output = [1] + [float(modulation_output[i] > 0) for i in range(1, len(modulation_output))]

plt.figure(figsize=(20, 12))
display_time = 0.1


plt.subplot(2, 1, 1)
plt.plot(time, message_signal, color='black', label='Original Message')
plt.step(dm_time, predicted_signal, color='red', where='post', label='Predicted Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Original and Delta-Modulated Signals')
plt.legend()
plt.axis([0, display_time, -2, 2])
plt.xticks(np.arange(0, display_time, display_time / 10))
plt.grid()


plt.subplot(2, 1, 2)
plt.stem(dm_time, modulation_output, linefmt='r', markerfmt='ro', basefmt='k')
plt.xlabel('Time (s)')
plt.ylabel('Step Amplitude')
plt.title('Delta Modulation Output')
plt.axis([0, display_time, -2 * dm_step_size, 2 * dm_step_size])
plt.xticks(np.arange(0, display_time, display_time / 10))
plt.grid()

plt.show()

