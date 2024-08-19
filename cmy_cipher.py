# colorama import
import sys
from colorama import Fore, init

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(start) + shift) % 26 + ord(start))
        else:
            result += char
    return result

print(caesar_cipher('HELLO', 5))