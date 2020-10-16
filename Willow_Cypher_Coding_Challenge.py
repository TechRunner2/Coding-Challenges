"""
Author: Willow Behar
Date Created: 10/16/20
Description: A Caesar Cipher coding challenge given by the Crunix Club"
"""

import sys
import random

help_text = """
        NAME
            wcc - Willow Caesar Cipher
        SYNOPSIS
            wcc -k [Cyper Key (Int)] [ENCRYPTION FLAG] [STRING]
        DESCRIPTION
            Encrypt or Decrypt a string using a Caesar Cipher (Warning: Does not change special characters)
            -E
                Encrypts String
            -D
                Decrypts String
            -h
                Prints Help Screen
        AUTHOR
            Written by Willow Behar.
        LICENSING
            GPLv3
        """

def main():
    #Help
    if "-h" in sys.argv:
        print(help_text)
    #Get Key
    if "-k" in sys.argv:
        #Find key flag location
        key_flag_location = sys.argv.index("-k")
        #Get Key Integer
        key = int(sys.argv[key_flag_location + 1])
    else:
        #Randomly generate a key
        key = random.randint(0, 100)
        print("Key:", key)
    if "-E" in sys.argv:
        #Get Encrypt Flag Location
        encrypt_flag_location = sys.argv.index("-E")
        #Get String to encrypt
        encrypt_string = str(sys.argv[encrypt_flag_location + 1])
        #Encrypt
        print(Encrypt(key, encrypt_string))
    elif "-D" in sys.argv:
        #Get Decrypt flag location
        decrypt_flag_location = sys.argv.index("-D")
        #Get String
        decrypt_string = sys.argv[decrypt_flag_location + 1]
        #Decrypt
        print(Decrypt(key, decrypt_string))
    else:
        print(help_text)

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