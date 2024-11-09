import matplotlib.pyplot as plt
import numpy as np

# Differential Manchester Encoding
# NRZI (complement) 0 -> invert + RZ

def differential_manchester_encoding(bit_stream):
    encoded_signal = []
    current_voltage = 1  # Initial voltage state

    for bit in bit_stream:
        if bit == '0': #will be inversion
            encoded_signal.extend([current_voltage, -current_voltage])
        elif bit == '1':
            encoded_signal.extend([-current_voltage, current_voltage])
            current_voltage = -current_voltage  # Invert the voltage level for the next bit

    # Append an extra value to maintain the last bit's value until the end of the plot
    # the last data point in encoded_signal does not extend to the end of the plot, as there is no further step beyond it.
    encoded_signal.append(encoded_signal[-1])
    
    return encoded_signal



# Longest Palindrome Finder
def longest_palindrome(data_stream):
    max_palindrome = ""
    for start in range(len(data_stream)):
        for end in range(start, len(data_stream)):
            substring = data_stream[start:end + 1]
            if substring == substring[::-1] and len(substring) > len(max_palindrome):
                max_palindrome = substring
    return max_palindrome



# Output printing
binary_input = input("Enter the data: ")
encoded_data = differential_manchester_encoding(binary_input)
longest_palindrome =longest_palindrome(binary_input)

print("Binary Data:", list(binary_input))
print("Differential Manchester Encoded Data:", encoded_data)
print("Longest palindrome in data stream: ", longest_palindrome)


# Plotting values on a graph
def plot(encoded_signal):
    # line will step to the next value after each index
    plt.step(range(len(encoded_signal)), encoded_signal, where='post', color='blue', linewidth=2)
    plt.title('Differential Manchester Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(len(encoded_signal)):
        plt.axvline(i, color='grey', linestyle='--')
    plt.show()

plot(encoded_data)
