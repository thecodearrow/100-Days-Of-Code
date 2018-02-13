"""

Julius Caesar protected his confidential information by encrypting it in a cipher.
 Caesar's cipher rotated every letter in a string by a fixed number, , making it unreadable by his enemies. Given a string, , and a number, , encrypt  
 and print the resulting string.

"""

#!/bin/python3

import sys

def caesarCipher(s, k):
    # Complete this function
    cipher=""
    for char in s:
        if(not char.isalpha()):
            cipher=cipher+char
        else:
            k=k%26
            if(char.islower()):
                if(ord(char)+k<=ord('z')):
                    cipher=cipher+chr(ord(char)+k)
                else:
                     cipher=cipher+chr(ord('a')+ord(char)+k-ord('z')-1)
            elif(char.isupper()):
                if(ord(char)+k<=ord('Z')):
                    cipher=cipher+chr(ord(char)+k)
                else:
                     cipher=cipher+chr(ord('A')+ord(char)+k-ord('Z')-1)
                
    return cipher
    

if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    k = int(input().strip())
    result = caesarCipher(s, k)
    print(result)
