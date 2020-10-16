"""
Author: Willow Behar
Date Created: 10/16/20
Description: A Caesar Cipher coding challenge given by the Crunix Club"
"""

import sys

def main():
    #Get Key
    if "-k" in sys.argv:
        key_flag_location = sys.argv.index("-k")
        key = int(sys.argv[key_flag_location + 1])
    if "-E" in sys.argv:
        #Get String
        encrypt_flag_location = sys.argv.index("-E")
        encrypt_string = str(sys.argv[encrypt_flag_location + 1])
        #Encrypt
        print(Encrypt(key, encrypt_string))
    if "-D" in sys.argv:
        #Get String
        decrypt_flag_location = sys.argv.index("-D")
        decrypt_string = sys.argv[decrypt_flag_location + 1]
        #Decrypt
        print(Decrypt(key, decrypt_string))
    if "-h" in sys.argv:
        #Help
        print("Help")

def Encrypt(key, phrase):
    new_string = ""
    for letter in phrase:
        letter_value = ord(letter)
        #Lowercase
        if 97 <= letter_value <= 122:
            letter_value += key
            if letter_value > 122:
                while letter_value > 122:
                    offset = letter_value - 122
                    letter_value = 96 + offset
            if letter_value < 97:
                while letter_value < 97:
                    offset = letter_value - 97
                    letter_value = 123 + offset
            new_string += chr(letter_value)
        #Uppercase
        elif 65 <= letter_value <= 90:
            letter_value += key
            if letter_value > 90:
                while letter_value > 90:
                    offset = letter_value - 90
                    letter_value = 64 + offset
            if letter_value < 65:
                while letter_value < 65:
                    offset = letter_value - 65
                    letter_value = 91 + offset
            new_string += chr(letter_value)
        else:
            new_string += letter
    return new_string

def Decrypt(key, phrase):
    return Encrypt(-key, phrase)

if __name__ == "__main__":
    main()