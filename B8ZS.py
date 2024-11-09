import matplotlib.pyplot as plt
import numpy as np

# B8ZS (Scrambled AMI Encoding)
# 8 consecutive zeros -> 000VB0VB
# V -> same polarity as previous pulse (1st) and B opposite
def b8zs_encoding(bitstream):
    encoded_signal = []
    zero_count = 0
    current_polarity = 1

    for bit in bitstream:
        if bit == '1':
            # Represent binary 1 as an alternating positive and negative level
            encoded_signal.append(current_polarity)
            zero_count = 0
            current_polarity = -current_polarity
        elif bit == '0':
            zero_count += 1
            if zero_count == 8:
                # Replace eight consecutive zeros with the special code (000VB0VB)
                for _ in range(7):
                    encoded_signal.pop()
                encoded_signal.extend([0, 0, 0, -current_polarity, current_polarity, 0, current_polarity, -current_polarity])
                zero_count = 0
            else:
                # Represent binary 0 as a zero level
                encoded_signal.append(0)

    # Add an extra value at the end to complete the last step on the graph
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

# Printing values and function calling
bitstream = input("Enter the data: ")
b8zs_encoded_data = b8zs_encoding(bitstream)
longest_palindrome_in_stream = longest_palindrome(bitstream)

print("Binary Data:", list(bitstream))
print("B8ZS Encoded Data:", b8zs_encoded_data)
print("Longest palindrome in data stream:", longest_palindrome_in_stream)

# Plotting values on a graph
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

plot_b8zs(b8zs_encoded_data)
