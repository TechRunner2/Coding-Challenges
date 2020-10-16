"""
Author: Willow Behar
Date Created: 10/16/20
Description: A Caesar Cipher coding challenge given by the Crunix Club"
"""

import sys

if __name__ == "__main__":
    main()

def main():
    #Get Key
    if "-k" in sys.argv:
        key_flag_location = sys.argv.index("-k")
        key = sys.argv[key_flag_location + 1]
    if "-E" in sys.argv:
        #Get String
        encrypt_flag_location = sys.argv.index("-E")
        encrypt_string = sys.argv[encrypt_flag_location + 1]
        #Encrypt
        Encrypt(key, encrypt_string)
    if "-D" in sys.argv:
        #Get String
        decrypt_flag_location = sys.argv.index("-D")
        decrypt_string = sys.argv[decrypt_flag_location + 1]
        #Decrypt
        Decrypt(key, decrypt_string)
    if "-h" in sys.argv:
        #Help
        
def Encrypt(key, phrase):
    new_string = ""
    if phrase is not "":
        for letter in phrase:
            letter_value = ord(letter)
            if 94 <= letter_value >= 122:
                letter_value += key
                if letter_value > 122:
                    while letter_value > 122:
                        offset = letter_value - 122
                        letter_value = 94 + offset
                if letter_value < 94:
                    while letter_value < 94:
                        offset = letter_value - 94
                        letter_value = 122 + offset
                new_string += chr(letter_value)
            else:
                new_string += letter

def Decrypt(key, phrase):
    if phrase is not "":