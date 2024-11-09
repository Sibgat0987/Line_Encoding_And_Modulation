import matplotlib.pyplot as plt

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

# Manchester Decoding Function
def decode_manchester(encoded_data):
    decoded_bits = []
    for i in range(0, len(encoded_data), 2):
        # Check for high-to-low transition
        if encoded_data[i] == 1 and encoded_data[i + 1] == -1:
            decoded_bits.append('0')
        # Check for low-to-high transition
        elif encoded_data[i] == -1 and encoded_data[i + 1] == 1:
            decoded_bits.append('1')
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

# Main Program Execution
binary_data = input("Enter the binary data: ")
encoded_data = encode_manchester(binary_data)
decoded_data = decode_manchester(encoded_data)
palindrome = longest_palindrome(binary_data)

print("Binary Data:", list(binary_data))
print("Manchester Encoded Data:", encoded_data)
print("Decoded Data:", decoded_data)
print("Longest Palindromic Substring in Data Stream:", palindrome)

# Plotting the Manchester Encoded Signal
def plot_encoded_signal(encoded_data):
    bit_duration = 2  # Each bit has two steps in Manchester encoding
    time_axis = range(len(encoded_data))

    plt.step(time_axis, encoded_data, where='post', color='blue', linewidth=2)
    plt.title('Manchester Encoded Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Signal Level')
    plt.axhline(0, color='red', linestyle='-')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for visualization
    plt.xlim(0, len(encoded_data)-1)  # Ensure x-axis starts at 0

    # Add vertical lines at each bit transition
    for idx in range(0, len(encoded_data), 2):
        plt.axvline(idx, color='gray', linestyle='--', linewidth=0.5)
    plt.show()

plot_encoded_signal(encoded_data)
