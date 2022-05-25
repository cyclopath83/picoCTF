#!/usr/bin/env python

from pwn import *
import string
from tqdm import tqdm
import hashlib
import itertools


HOST = "mercury.picoctf.net"
PORT = 41175
#r = remote(HOST, PORT)


# We need to find a string that starts with 'strstart', and that will produce an MD5 hash that ends in 'hashend'.
# I don't know about any way to do this, besides trial-and-error/bruteforcing.
# So I just appened a certain (5) number of all the possible characters to the start string, and check if it produces the needed MD5 hash
def findhash(strstart, hashend, n):
    # Checking if the strstart + randomstring produces an MD5 hash that ends with hashend
    def check(strstart, hashend, randstr):
        checkstr = strstart + randstr
        check = hashlib.md5(checkstr.encode()).hexdigest()
        return check[-len(hashend):] == hashend

    # Generating all possible combo's with a length n (5)
    def iter(l):
        yield from itertools.product(*([l] * n))
    
    # Going through all possible combos of ascii_letters with a length of n (5) appended to the startstring, and if it gets a good MD5 hash, return the tested string.
    for x in iter(string.ascii_letters):
        if check(strstart, hashend, ''.join(x)):
            return strstart + ''.join(x)

def getstring():
    test = findhash("31525", "21630e", 5)
    print(test)




def main():
    
    getstring()
    


if __name__ == '__main__':
    main()