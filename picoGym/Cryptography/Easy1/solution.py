#!/usr/bin/env python

enc = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    flag = "picoCTF{"
    for i in range(0, len(enc)):
        j = (ord(enc[i]) - ord('A') - ord(key[i]) - ord('A')) % 26
        flag += ALPHABET[j]
    flag += "}"
    print(flag)



if __name__ == '__main__':
    main()
