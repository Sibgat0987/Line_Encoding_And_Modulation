import matplotlib.pyplot as plt
import numpy as np

# AMI (Alternate Mark Inversion) Encoding
def ami_encoding(bits):
    encoded_bits = []
    current_level = 1  # Initial level

    for bit in bits:
        if bit == '0':
            # Represent binary 0 as a zero level
            encoded_bits.append(0)
        elif bit == '1':
            # Represent binary 1 as an alternating positive and negative level
            encoded_bits.append(current_level)
            current_level = -current_level  # Invert the level for the next bit

    return encoded_bits

# AMI Decoding
def ami_decoding(encoded_bits):
    decoded_bits = []
    previous_level = 0  # Start with no previous signal

    for level in encoded_bits:
        if level == 0:
            decoded_bits.append('0')
        else:
            decoded_bits.append('1')
        previous_level = level

    return ''.join(decoded_bits)

# Longest Palindrome Finder
def longest_palindrome(s):
    longest_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

# Plotting function
# Plotting function
def plot(ami_data):
    # Extend the last value to make the last bit fully visible on the plot
    extended_data = ami_data + [ami_data[-1]]
    
    plt.step(range(len(extended_data)), extended_data, where='post', color='blue', linewidth=2)
    plt.title('AMI Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red', linestyle='-')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    
    # Add vertical grid lines for each bit
    for i in range(len(ami_data)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    
    plt.show()


# Main Execution
binary_data = input("Enter the data: ")
ami_data = ami_encoding(binary_data)
palindrome = longest_palindrome(binary_data)

print("Binary Data:", list(binary_data))
print("AMI Encoded Data:", ami_data)
print("Longest palindrome in data stream: ", palindrome)

# Plotting the AMI encoded data
plot(ami_data)

# Ask the user if they want to decode the signal
decode_choice = input("Do you want to decode the signal? (yes/no): ").strip().lower()
if decode_choice == 'yes':
    decoded_data = ami_decoding(ami_data)
    print("Decoded Binary Data:", decoded_data)
else:
    print("Decoding skipped.")
