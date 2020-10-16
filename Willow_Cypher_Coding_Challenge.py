"""
Author: Willow Behar
Date Created: 10/16/20
Description: A Caesar Cipher coding challenge given by the Crunix Club"
"""

import sys

if __name__ == "__main__":
    main()

def main():
    if "-E" in sys.argv:
        #Encrypt
        encrypt()
    if "-D" in sys.argv:
        #Decrypt
    if "-h" in sys.argv:
        #Help
        