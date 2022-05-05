#!/usr/bin/env python

import hashlib

pos_pw_list = ["6997", "3ac8", "f0ac", "4b17", "ec27", "4e66", "865e"]

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()


def main():
    correct_pw_hash = open('level3.hash.bin', 'rb').read()
    for pw in pos_pw_list:
        pwhash = hash_pw(pw)
        if pwhash == correct_pw_hash:
            print("The correct password is: "+pw)


if __name__ == '__main__':
    main()
