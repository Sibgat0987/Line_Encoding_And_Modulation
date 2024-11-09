import matplotlib.pyplot as plt
import numpy as np

# HBD3 (High-Density Bipolar 3 Zeros) Encoding with Scrambled AMI
def hdb3_encode(bit_stream):
    encoded_stream = []
    zero_count = 0
    last_polarity_change = 0
    current_voltage = 1

    for bit in bit_stream:
        if bit == '1':
            # Alternate levels for binary 1
            encoded_stream.append(current_voltage)
            zero_count = 0
            last_polarity_change = 0
            current_voltage = -current_voltage
        elif bit == '0':
            zero_count += 1
            if zero_count == 4:
                # Remove last three zeros for HBD3 rule application
                for _ in range(3):
                    encoded_stream.pop()
                # Substitute based on even/odd number of 1s since last substitution
                if last_polarity_change % 2 == 0:
                    current_voltage = -current_voltage
                    encoded_stream.extend([-current_voltage, 0, 0, -current_voltage])
                    last_polarity_change += 1
                else:
                    encoded_stream.extend([0, 0, 0, -current_voltage])
                    last_polarity_change += 1
                zero_count = 0
            else:
                encoded_stream.append(0)

    return encoded_stream

# Longest Palindrome Finder
def longest_palindrome(s):
    longest_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

# User input and function calls
binary_sequence = input("Enter the binary data stream: ")
encoded_sequence = hdb3_encode(binary_sequence)
longest_palindrome = longest_palindrome(binary_sequence)

print("Binary Data Stream:", list(binary_sequence))
print("HDB3 Encoded Sequence:", encoded_sequence)
print("Longest Palindromic Subsequence:", longest_palindrome)

# Plotting the HBD3 Encoded Data
def plot_encoded_data(data):
    plt.step(range(len(data)), data, where='post', color='blue', linewidth=2.5)
    plt.title('HBD3 Encoded Signal')
    plt.xlabel('Bit Position')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red', linestyle='-')
    plt.ylim(-1.5, 1.5)  # Set y-axis for visual clarity
    for idx in range(len(data)):
        plt.axvline(idx, color='grey', linestyle='--', linewidth=0.5)
    plt.show()

plot_encoded_data(encoded_sequence)
