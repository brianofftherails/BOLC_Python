#!/usr/bin/env python3

from itertools import repeat

def char_rshift(char, int_shift):
    assert ord(char) in range(32,127)
    #only tests for chars that will break the program
    if char == " ":
        return " "
    else:
        return chr(97+(ord(char)+int_shift-97)%26)

def char_lshift(char,int_shift):
    assert ord(char) in range(32,127)
    #only tests for chars that will break the program
    if char == ' ':
        return ' '
    else:
        return chr(97 + (ord(char) - int_shift - 97) % 26)

def caesar_encrypt(plaintext,key):
    '''Encrypts plaintext using the Caesar Cipher
    Args:
        plaintext (str): a string to be encrypted (all lowercase)
        key (int): number of characters to shift
    Returns:
        str: the encrypted ciphertext
    '''
    return ''.join(list(map(char_rshift,list(plaintext),repeat(key))))


def caesar_decrypt(ciphertext,key):
    '''Decrypts ciphertext using the Caesar Cipher
    Args:
        ciphertext (str): the string to be decrypted (all lowercase)
        key (int): number of characters to shift
    Returns:
        str: the decrypted plaintext
    '''
    return ''.join(list(map(char_lshift, list(ciphertext),repeat(key))))


if __name__ == '__main__':
	pass
