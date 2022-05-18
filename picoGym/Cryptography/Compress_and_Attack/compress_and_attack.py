#!/usr/bin/python3 -u

from pydoc import plain
import zlib
from random import randint
import os
from Crypto.Cipher import Salsa20

flag = open("./flag").read()


def compress(text):
    print(f"compress - text = {text}")
    c =  zlib.compress(bytes(text.encode("utf-8")))
    print(f"compress - compressed = {c}")
    return c

def encrypt(plaintext):
    print(f"encrypt - plaintext = {plaintext}")
    secret = os.urandom(32)
    print(f"encrypt - secret = {secret}")
    cipher = Salsa20.new(key=secret)
    c = cipher.nonce + cipher.encrypt(plaintext)
    print(f"encrypt - encryped = {c}   (nonce={cipher.nonce})")
    return c

def main():
    while True:
        usr_input = input("Enter your text to be encrypted: ")
        compressed_text = compress(flag + usr_input)
        encrypted = encrypt(compressed_text)
        
        nonce = encrypted[:8]
        encrypted_text =  encrypted[8:]
        print(nonce)
        print(encrypted_text)
        print(len(encrypted_text))

if __name__ == '__main__':
    main() 



