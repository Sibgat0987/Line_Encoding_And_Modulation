import matplotlib.pyplot as plt

# B8ZS Encoding Function
def b8zs_encoding(bitstream):
    encoded_signal = []
    zero_count = 0
    current_polarity = 1

    for bit in bitstream:
        if bit == '1':
            encoded_signal.append(current_polarity)
            zero_count = 0
            current_polarity = -current_polarity
        elif bit == '0':
            zero_count += 1
            if zero_count == 8:
                # B8ZS substitution: 000VB0VB
                for _ in range(7):
                    encoded_signal.pop()
                encoded_signal.extend([0, 0, 0, -current_polarity, current_polarity, 0, current_polarity, -current_polarity])
                zero_count = 0
            else:
                encoded_signal.append(0)
    
    encoded_signal.append(encoded_signal[-1])  # To complete the last step for plotting
    return encoded_signal

# B8ZS Decoding Function
def b8zs_decoding(encoded_signal):
    decoded_bits = []
    i = 0
    while i < len(encoded_signal) - 1:
        # Detect B8ZS pattern 000VB0VB
        if (i + 7 < len(encoded_signal) and 
            encoded_signal[i:i+8] == [0, 0, 0, -encoded_signal[i+3], encoded_signal[i+3], 0, encoded_signal[i+3], -encoded_signal[i+3]]):
            decoded_bits.extend(['0'] * 8)
            i += 8
        else:
            # Decode a '1' if it's not zero, and a '0' if it's zero level
            decoded_bits.append('1' if encoded_signal[i] != 0 else '0')
            i += 1

    return ''.join(decoded_bits)

# Longest Palindrome Finder
def longest_palindrome(data_stream):
    max_palindrome = ""
    for start in range(len(data_stream)):
        for end in range(start, len(data_stream)):
            substring = data_stream[start:end + 1]
            if substring == substring[::-1] and len(substring) > len(max_palindrome):
                max_palindrome = substring
    return max_palindrome

# Plotting B8ZS Encoded Data
def plot_b8zs(encoded_data):
    plt.step(range(len(encoded_data)), encoded_data, where='post', color='blue', linewidth=2)
    plt.title('B8ZS Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range(len(encoded_data)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    plt.show()

# Main Execution
bitstream = input("Enter the data: ")
b8zs_encoded_data = b8zs_encoding(bitstream)
longest_palindrome_in_stream = longest_palindrome(bitstream)

print("Binary Data:", list(bitstream))
print("B8ZS Encoded Data:", b8zs_encoded_data)
print("Longest palindrome in data stream:", longest_palindrome_in_stream)

# Plotting the B8ZS encoded data
plot_b8zs(b8zs_encoded_data)

# Ask the user if they want to decode the signal
decode_choice = input("Do you want to decode the signal? (yes/no): ").strip().lower()
if decode_choice == 'yes':
    decoded_data = b8zs_decoding(b8zs_encoded_data)
    print("Decoded Binary Data:", decoded_data)
else:
    print("Decoding skipped.")
