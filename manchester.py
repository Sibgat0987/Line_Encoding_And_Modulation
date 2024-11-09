import matplotlib.pyplot as plt
import numpy as np

# Manchester Encoding Technique
def encode_manchester(bits):
    encoded_output = []
    for bit in bits:
        if bit == '0':
            # Encode binary 0 as high-to-low transition
            encoded_output.extend([1, -1])
        elif bit == '1':
            # Encode binary 1 as low-to-high transition
            encoded_output.extend([-1, 1])
    return encoded_output

# Longest Palindrome Finder
def longest_palindrome(s):
    longest_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

# Main Program Execution
binary_data = input("Enter the binary data: ")
encoded_data = encode_manchester(binary_data)
palindrome = longest_palindrome(binary_data)

print("Binary Data:", list(binary_data))
print("Manchester Encoded Data:", encoded_data)
print("Longest Palindromic Substring in Data Stream:", palindrome)

# Plotting the Manchester Encoded Signal
def plot_encoded_signal(encoded_data):
    plt.step(range(len(encoded_data)), encoded_data, where='post', color='blue', linewidth=2)
    plt.title('Manchester Encoded Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Signal Level')
    plt.axhline(0, color='red', linestyle='-')
    plt.ylim(-1.5, 1.5)  # Limit the y-axis for better visualization
    
    for idx in range(len(encoded_data)):
        plt.axvline(idx, color='gray', linestyle='--')
    plt.show()

plot_encoded_signal(encoded_data)
