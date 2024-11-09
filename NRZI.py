import matplotlib.pyplot as plt

# NRZ_I (Non Return to Zero_Inverted) Encoding
# for 1 inversion will happen, if the bit is 0 no inversion
def nrz_i_encoding(bits):
    encoded_bits = []
    current_level = 1  # Start with a high level

    for bit in bits:
        if bit == '1':
            current_level = -current_level  # Invert the level for a binary 1
        encoded_bits.append(current_level)
    encoded_bits.append(current_level)  # Extend the last level to complete the cycle
    return encoded_bits

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
def plot(nrz_i_data):
    plt.step(range(len(nrz_i_data)), nrz_i_data, where='post', color='red', linewidth=2)
    plt.title('NRZ-I Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='blue')
    plt.ylim(-1.5, 1.5)  # Set y-axis limits for better visualization
    for i in range((len(nrz_i_data)+1 )- 1):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    plt.show()

# Function Calling and printing values 
binaryBits = input("Enter the data: ")
NRZIdata = nrz_i_encoding(binaryBits)
palindrome = longest_palindrome(binaryBits)

print("Binary Data:", list(binaryBits))
print("NRZ-I Encoded Data:", NRZIdata)
print("Longest palindrome in data stream:", palindrome)

# Plotting the NRZ-I encoded data
plot(NRZIdata)
