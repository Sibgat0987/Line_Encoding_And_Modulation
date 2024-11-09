import numpy as np 
import matplotlib.pyplot as plt

def pcm_encode(input_signal, quantization_levels):
    
    normalized_signal = (input_signal - np.min(input_signal)) / (np.max(input_signal) - np.min(input_signal))
    
    
    quantized_output = np.round(normalized_signal * (quantization_levels - 1))
    
    return quantized_output

time = np.arange(0, 1, 0.001)
amplitude = float(input("Enter the signal amplitude: "))
frequency = float(input("Enter the signal frequency: "))
analog_wave = amplitude * np.sin(2 * np.pi * frequency * time) + amplitude * np.sin(2 * np.pi * (2 * frequency) * time)

# Specify the quantization levels for PCM
levels = 8

# Perform PCM encoding
encoded_signal = pcm_encode(analog_wave, levels)

# Plot the original signal and the quantized PCM signal
plt.subplot(2, 1, 1)
plt.plot(time, analog_wave, color='blue')
plt.title('Original Analog Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.step(time, encoded_signal, color='orange', linewidth=1)
plt.title('PCM Quantized Signal')
plt.xlabel('Time')
plt.ylabel('Quantized Level')

plt.tight_layout()
plt.show()

print(encoded_signal)