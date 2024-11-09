import os

def choose_modulation():
    print("\nYou have chosen Analog Signal\n")
    modulation_choice = input(
        "Enter the modulation technique you want to use:\n"
        "1. Pulse Code Modulation (PCM)\n"
        "2. Delta Modulation (DM)\n"
    )
    
    if int(modulation_choice) == 1:
        os.system("python pcm.py")
    else:
        os.system("python dm.py")

def choose_line_encoding():
    print("\nYou have chosen Digital Signal\n")
    encoding_choice = int(input(
        "Enter the encoding technique you want to implement:\n"
        "1. NRZ-L\n"
        "2. NRZ-I\n"
        "3. Manchester\n"
        "4. Differential Manchester\n"
        "5. AMI\n"
    ))

    if encoding_choice == 1:
        os.system("python NRZL.py")
    elif encoding_choice == 2:
        os.system("python NRZI.py")
    elif encoding_choice == 3:
        os.system("python manchester.py")
    elif encoding_choice == 4:
        os.system("python DIFFERENTIAL_MANCHESTER.py")
    elif encoding_choice == 5:
        choose_ami_encoding()

def choose_ami_encoding():
    ami_scrambling_choice = int(input("Choose AMI option:\n1. With Scrambling\n2. Without Scrambling\n"))
    
    if ami_scrambling_choice == 1:
        scrambling_type = int(input("Choose scrambling type:\n1. B8ZS\n2. HDB3\n"))
        if scrambling_type == 1:
            os.system("python B8ZS.py")
        else:
            os.system("python HDB3.py")
    else:
        os.system("python AMI.py")

if __name__ == '__main__':
    signal_type = input("Enter the type of signal:\n1. Analog Signal\n2. Digital Signal\n")
    
    if int(signal_type) == 1:
        choose_modulation()
    else:
        choose_line_encoding()
