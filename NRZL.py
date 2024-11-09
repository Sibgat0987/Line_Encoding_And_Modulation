import matplotlib.pyplot as plt

# NRZ-L (Non Return to Zero-Level) Encoding
# High voltage for '1' and low voltage for '0'
def nrz_l_encoding(bits): 
    encoded_data = []
    for bit in bits:
        if bit == '1':
            encoded_data.append(1)  # High voltage for '1'
        else:
            encoded_data.append(-1)  # Low voltage for '0'
    encoded_data.append(encoded_data[-1])  # Extend the last level
    return encoded_data

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
def plot(NRZLdata):
    plt.step(range(len(NRZLdata)), NRZLdata, where='post', color='red', linewidth=2)
    plt.title('NRZ-L Encoded Data')
    plt.xlabel('Bit Index')
    plt.ylabel('Voltage Level')
    plt.axhline(0, color='blue')
    plt.ylim(-1.5, 1.5)  
    for i in range(len(NRZLdata) ):
        plt.axvline(i, color='grey', linestyle='--', linewidth=0.5)
    plt.show()

# Function Calling and printing values 
binaryBits = input("Enter the data: ")
NRZLdata = nrz_l_encoding(binaryBits)
palindrome = longest_palindrome(binaryBits)

print("Binary Data:", list(binaryBits))
print("NRZ-L Encoded Data:", NRZLdata)
print("Longest palindrome in data stream:", palindrome)

# Plotting the NRZ-L encoded data
plot(NRZLdata)
