import matplotlib.pyplot as plt

# Differential Manchester Encoding function
def differential_manchester_encoding(bit_stream):
    encoded_signal = []
    current_voltage = 1  # Initial voltage state

    for bit in bit_stream:
        if bit == '0':  # Inversion for '0'
            encoded_signal.extend([current_voltage, -current_voltage])
        elif bit == '1':
            encoded_signal.extend([-current_voltage, current_voltage])
            current_voltage = -current_voltage  # Invert the voltage level for the next bit

    return encoded_signal

# Corrected Differential Manchester Decoding function
def decode_differential_manchester(signal):
    decoded = []
    prev_end_level = signal[0]  # Start with the first level

    # Process signal in pairs of levels (bit periods)
    for i in range(0, len(signal) - 1, 2):
        # Check if there's a transition at the beginning of the bit period
        if signal[i] == prev_end_level:
            decoded.append('1')  # No transition means '1'
        else:
            decoded.append('0')  # Transition means '0'
        
        # Update the previous end level to the current period's end level
        prev_end_level = signal[i + 1]
    
    return ''.join(decoded)

# Longest Palindrome Finder
def longest_palindrome(data_stream):
    max_palindrome = ""
    for start in range(len(data_stream)):
        for end in range(start, len(data_stream)):
            substring = data_stream[start:end + 1]
            if substring == substring[::-1] and len(substring) > len(max_palindrome):
                max_palindrome = substring
    return max_palindrome

# Plotting Differential Manchester Encoded Data
def plot(encoded_signal):
    extended_data = encoded_signal + [encoded_signal[-1]]
    plt.step(range(len(extended_data)), extended_data, where='post', color='blue', linewidth=2)
    plt.title('Differential Manchester Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red')
    plt.ylim(-1.5, 1.5)

    for i in range(len(encoded_signal)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    plt.show()

# Main Execution
binary_input = input("Enter the binary data: ")
encoded_data = differential_manchester_encoding(binary_input)
longest_palindrome_in_data = longest_palindrome(binary_input)

print("Binary Data:", list(binary_input))
print("Differential Manchester Encoded Data:", encoded_data)
print("Longest palindrome in data stream:", longest_palindrome_in_data)

# Plotting the encoded data
plot(encoded_data)

# Ask the user if they want to decode the signal
decode_choice = input("Do you want to decode the signal? (yes/no): ").strip().lower()
if decode_choice == 'yes':
    decoded_data = decode_differential_manchester(encoded_data)
    print("Decoded Binary Data:", decoded_data)
else:
    print("Decoding skipped.")
