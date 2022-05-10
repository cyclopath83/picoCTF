#!/usr/bin/env python

# We did a similar thing in the challenge 'Easy1', so reusing that code
CIPHER = 'rgnoDVD{O0NU_WQ3_G1G3O3T3_A1AH3S_2951c89f}'
KEY = 'CYLAB'

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    flag = ""
    i = 0
    for c in CIPHER:
        if(c.upper() in ALPHABET):
            j = (ord(c.upper()) - ord('A') - ord(KEY[i]) - ord('A')) % 26
            if(c in ALPHABET):
                flag += ALPHABET[j]
            else:
                flag += ALPHABET[j].lower()
            i = (i + 1) % len(KEY)
        else:
            flag += c
    print(flag)



if __name__ == '__main__':
    main()
