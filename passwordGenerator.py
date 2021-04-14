import string 
import random

def gen():                                                           # A function to generate the passwords
    s1 = string.ascii_uppercase                                      # Create a variable to hold all alphabet letters in an upprecase string
    s2 = string.ascii_lowercase                                      # Create a variable for all lowercase letters
    s3 = string.digits                                               # Create a variable to hold 0-9
    s4 = string.punctuation                                          # Create a variable to hold all special characters
    
    passLength = int(input('Please enter a password length: '))      # Accept a length valuse from the keyboard 
    s = []                                                           # Create an empty list variable 
    s.extend(list(s1))                                               # The extend method adds all the characters from s1 - 4 into the list of s
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)                                                # Randomly shuffle the contents of the list 
    password = (''.join(s[:passLength]))                             # Take a blank string and join the first random characters from 0 to the specified length
    print(password)                                                  # Print the password

    pw = ''
    for letter in range(passLength):                                 # This method demonstrates hoe to use string concatination to provide the same outcome
        pw+=s[letter]                                                # Because pw was declared outside the loop, every iteration the character at position letter is appended
    print(pw)    

    wp = []
    for char in range(passLength):                                   # This method demonstrates hot to achieve the same objective with a list of characters
        wp.append(s[char])
    print(''.join(wp))
gen()

