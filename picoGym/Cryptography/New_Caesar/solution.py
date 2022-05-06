#!/usr/bin/env python

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_decode(char, key):
    offset = ord(key) - ord('a')
    t1 = (16 + ord(char[0]) - ord('a') - offset) % 16
    t2 = (16 + ord(char[1]) - ord('a') - offset) % 16
    return chr(16*t1 + t2)


# the real encrypted flag
enc = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
# "cyclopathrules" with key 'a'
#enc = "gdhjgdgmgphagbhegihchfgmgfhd"
# "cyclopathrules" with key 'b'
#enc = "heikhehnhaibhcifhjidighnhgie"


def main():
    for key in ALPHABET:
        flag = ""
        for i in range(0, len(enc), 2):
            char = enc[i] + enc[i+1]
            flag += b16_decode(char, key)
        print(f"key:{key}  :  {flag}")
        pri


if __name__ == '__main__':
    main()
