#!/usr/bin/env python

import hashlib


def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def main():
    dictlist = open('dictionary.txt').read().split()
    correct_pw_hash = open('level5.hash.bin', 'rb').read()
    for pw in dictlist:
        pwhash = hash_pw(pw)
        if pwhash == correct_pw_hash:
            print("The correct password is: "+pw)


if __name__ == '__main__':
    main()
