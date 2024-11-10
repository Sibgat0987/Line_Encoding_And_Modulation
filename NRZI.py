import matplotlib.pyplot as plt

# NRZ-I Encoding function
def nrz_i_encoding(bits):
    encoded_bits = []
    current_level = 1  # Start with high level

    for bit in bits:
        if bit == '1':
            current_level = -current_level  # Invert the level for '1'
        encoded_bits.append(current_level)
    return encoded_bits

# NRZ-I Decoding function
def nrz_i_decoding(encoded_bits):
    decoded_bits = []
    previous_level = encoded_bits[0]

    # Assuming initial high level means '0' and low level means '1'
    decoded_bits.append('0' if previous_level == 1 else '1')

    # Decode each level transition
    for level in encoded_bits[1:]:
        if level != previous_level:
            decoded_bits.append('1')  # Level change indicates '1'
        else:
            decoded_bits.append('0')  # No change indicates '0'
        previous_level = level  # Update previous level to current

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

# Plotting NRZ-I Encoded Data
# Plotting NRZ-I Encoded Data
def plot(nrz_i_data):
    # Extend the data by duplicating the last value for visualization purposes
    extended_data = nrz_i_data + [nrz_i_data[-1]]
    
    plt.step(range(len(extended_data)), extended_data, where='post', color='red', linewidth=2)
    plt.title('NRZ-I Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='blue')
    plt.ylim(-1.5, 1.5)
    
    # Add vertical grid lines at each bit transition
    for i in range(len(nrz_i_data)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    
    plt.show()


# Main Execution
binaryBits = input("Enter the data: ")
NRZIdata = nrz_i_encoding(binaryBits)
palindrome = longest_palindrome(binaryBits)

print("Binary Data:", list(binaryBits))
print("NRZ-I Encoded Data:", NRZIdata)
print("Longest palindrome in data stream:", palindrome)

# Plotting the NRZ-I encoded data
plot(NRZIdata)

# Ask the user if they want to decode the signal
decode_choice = input("Do you want to decode the signal? (yes/no): ").strip().lower()
if decode_choice == 'yes':
    decoded_bits = nrz_i_decoding(NRZIdata)
    print("Decoded Binary Data:", decoded_bits)
else:
    print("Decoding skipped.")
