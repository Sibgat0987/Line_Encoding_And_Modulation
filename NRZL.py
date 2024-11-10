import matplotlib.pyplot as plt

# NRZ-L (Non Return to Zero-Level) Encoding
def nrz_l_encoding(bits): 
    encoded_data = []
    for bit in bits:
        encoded_data.append(1 if bit == '1' else -1)  # High voltage for '1', low voltage for '0'
    encoded_data.append(encoded_data[-1])  # Extend the last level
    return encoded_data

# NRZ-L Decoding
def nrz_l_decoding(encoded_data):
    decoded_bits = ''.join(['1' if level == 1 else '0' for level in encoded_data[:-1]])
    return decoded_bits

# Longest Palindrome Finder
def longest_palindrome(s):
    longest_palindrome = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

# Plotting NRZ-L Encoded Data
def plot(nrzl_data):
    plt.step(range(len(nrzl_data)), nrzl_data, where='post', color='red', linewidth=2)
    plt.title('NRZ-L Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='blue')
    plt.ylim(-1.5, 1.5)
    for i in range(len(nrzl_data)):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    plt.show()

# Function Calling and Printing Values
binary_bits = input("Enter the data: ")
nrzl_data = nrz_l_encoding(binary_bits)
palindrome = longest_palindrome(binary_bits)

print("Binary Data:", list(binary_bits))
print("NRZ-L Encoded Data:", nrzl_data)
print("Longest palindrome in data stream:", palindrome)

# Plotting the NRZ-L encoded data
plot(nrzl_data)

decode_choice = input("Would you like to decode the signal? (yes/no): ").strip().lower()
if decode_choice == "yes":
    decoded_data = nrz_l_decoding(nrzl_data)
    print("Decoded Data:", decoded_data)

else:
    print("Decoding skipped.")