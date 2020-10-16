#!/bin/python3
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
            -EF
                Encrypt File
            -DF
                Decrypt File
            -o
                Save output to file instead of printing to terminal
        AUTHOR
            Written by Willow Behar.
        LICENSING
            GPLv3
        """


def main():
    file_output_flag = False
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
        key = random.randint(1, 100)
        print("Key:", key)

    if "-o" in sys.argv:
        #Set flag to true
        file_output_flag = True
        #Get Location of Flag
        file_output_location = sys.argv.index("-o")
        #Get File Name
        file_output_name = sys.argv[file_output_location + 1]
        #Open file
        file_output_open = open(file_output_name, "w")

    if "-E" in sys.argv:
        #Get Encrypt Flag Location
        encrypt_flag_location = sys.argv.index("-E")
        #Get String to encrypt
        encrypt_string = str(sys.argv[encrypt_flag_location + 1])
        #Encrypt
        encrypted_phrase = Encrypt(key, encrypt_string)
        if file_output_flag:
            file_output_open.write(encrypted_phrase)
        else:
            print(encrypted_phrase)

    elif "-D" in sys.argv:
        #Get Decrypt flag location
        decrypt_flag_location = sys.argv.index("-D")
        #Get String
        decrypt_string = sys.argv[decrypt_flag_location + 1]
        #Decrypt
        print(Decrypt(key, decrypt_string))

    elif "-EF" in sys.argv:
        #Get Encrypt File Flag
        encrypt_file_location = sys.argv.index("-EF")
        #Get File Location
        encrypt_file_name = str(sys.argv[encrypt_file_location + 1])
        #Open File
        encrypt_file_open = open(encrypt_file_name, "r")
        #Read File
        encrypt_file_data = encrypt_file_open.read()
        #Encrypt File
        encrypted_file_data = Encrypt(key, encrypt_file_data)
        if file_output_flag:
            file_output_open.write(encrypted_file_data)
        else:
            print(encrypted_file_data)

    elif "-DF" in sys.argv:
        #Get Decrypt File Flag
        decrypt_file_location = sys.argv.index("-DF")
        #Get File location
        decrypt_file_name = str(sys.argv[decrypt_file_location + 1])
        #Open File
        decrypt_file_open = open(decrypt_file_name, "r")
        #Read File
        decrypt_file_data = decrypt_file_open.read()
        #Decrypt File
        decrypted_file_data = Decrypt(key, decrypt_file_data)
        if file_output_flag:
            file_output_open.write(decrypted_file_data)
        else:
            print(decrypted_file_data)
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