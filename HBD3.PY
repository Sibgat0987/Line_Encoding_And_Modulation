import matplotlib.pyplot as plt

# HDB3 Encoding Function
def hdb3_encode(bits):
    encoded_bits = []
    zero_count = 0
    last_substitution_count = 0
    current_level = 1

    for bit in bits:
        if bit == '1':
            # Toggle polarity for each '1' in the encoded signal
            encoded_bits.append(current_level)
            current_level = -current_level
            zero_count = 0
            last_substitution_count = 0
        else:  # bit == '0'
            zero_count += 1
            if zero_count == 4:
                # Handle four consecutive zeros with substitutions
                encoded_bits[-3:] = []  # Remove the last three zeros

                # Substitute based on even/odd substitutions since last non-zero level
                if last_substitution_count % 2 == 0:
                    encoded_bits.extend([-current_level, 0, 0, -current_level])
                else:
                    encoded_bits.extend([0, 0, 0, -current_level])
                
                last_substitution_count += 1
                zero_count = 0
            else:
                encoded_bits.append(0)  # Maintain zero level for individual zeros

    return encoded_bits

# HDB3 Decoding Function
def hdb3_decode(encoded_bits):
    decoded_bits = []
    zero_count = 0
    last_non_zero_level = None

    for i in range(len(encoded_bits)):
        if encoded_bits[i] == 0:
            zero_count += 1
            decoded_bits.append('0')
        else:
            if zero_count == 3:
                # Detect a substitution pattern of four zeros
                if (encoded_bits[i] == last_non_zero_level) or (encoded_bits[i] == -last_non_zero_level):
                    decoded_bits[-3:] = ['0', '0', '0', '0']
                zero_count = 0

            # Append '1' for non-zero levels and reset the zero count
            decoded_bits.append('1')
            last_non_zero_level = encoded_bits[i]
            zero_count = 0

    return ''.join(decoded_bits)

# Longest Palindromic Substring Finder
def find_longest_palindrome(sequence):
    longest_palindrome = ''
    dp = [[False] * len(sequence) for _ in range(len(sequence))]

    for i in range(len(sequence)):
        dp[i][i] = True
        longest_palindrome = sequence[i]

    for start in range(len(sequence) - 1, -1, -1):
        for end in range(start + 1, len(sequence)):
            if sequence[start] == sequence[end]:
                if end - start == 1 or dp[start + 1][end - 1]:
                    dp[start][end] = True
                    if len(longest_palindrome) < end - start + 1:
                        longest_palindrome = sequence[start:end + 1]

    return longest_palindrome

# Main Execution
binary_data = input("Enter the binary data stream: ")
encoded_data = hdb3_encode(binary_data)
decoded_data = hdb3_decode(encoded_data)
longest_palindrome = find_longest_palindrome(binary_data)

print("Binary Data Stream:", list(binary_data))
print("HDB3 Encoded Sequence:", encoded_data)
print("Decoded Sequence:", decoded_data)
print("Longest Palindromic Substring in Data Stream:", longest_palindrome)

# Plotting the Encoded Data
def plot_encoded_data(data):
    bit_duration = 2  # Each bit has two steps in Manchester encoding
    time_axis = range(len(encoded_data))

    plt.step(time_axis, encoded_data, where='post', color='blue', linewidth=2)
    plt.title('HDB3 Encoded Signal')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='red', linestyle='-')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for visualization
    plt.xlim(0, len(encoded_data)-1)  # Ensure x-axis starts at 0

    # Add vertical lines at each bit transition
    for idx in range(0, len(encoded_data), 2):
        plt.axvline(idx, color='gray', linestyle='--', linewidth=0.5)
    plt.show()

plot_encoded_data(encoded_data)

