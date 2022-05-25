#!/usr/bin/env python

from pwn import *
import string
from tqdm import tqdm
import hashlib
import itertools
import gmpy2
from Crypto.Util.number import inverse, getPrime, bytes_to_long, GCD


HOST = "mercury.picoctf.net"
PORT = 41175
r = remote(HOST, PORT)


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



def crackRSA(n, e):
    while True:
        x = getPrime(20)
        xe = pow(x, e, n)
        xed = 1
        for dp in tqdm(range(1<<20), desc=f"Bruteforce RSA using x={x}"):
            xed = (xed * xe) % n
            check = GCD(xed - x, n)
            if check != 1:
                print(check)
                return check
                break


def main():
    # 1) First part is the MD5 hash challenge. 
    # Grab the start of the string, and the requested hash ending, and search for a string that starts with the provided string, and produces an MD5 hash with that ending.
    line = r.recvlineS(keepends = False)
    strstart = line.split('"')[1]
    hashend = line[-6:]
    print(f"Grabbed startstring '{strstart}' and hash ending '{hashend}'.")
    print("Looking for a valid string... (this can take a while)")
    validstring = findhash(strstart, hashend, 5)
    print(f"Found a valid string to produce the requested hash: {validstring}")
    r.sendline(bytearray(validstring, 'utf-8'))

    # 2) Grab the Public Modulus, and the Clue
    r.recvuntil(bytearray('Public Modulus :  ', 'utf-8'))
    pubmod = int(r.recvlineS(keepends = False))
    r.recvuntil(bytearray('Clue :  ', 'utf-8'))
    clue = int(r.recvlineS(keepends = False))
    print(f"Pubmod = {pubmod}")
    print(f"Clue = {clue}")
    
    # 3) Crack the flag
    # Using the description of the challenge, I started searching for RSA CRT attacks. But most of the results were describing a side-channel (or fault) attack.
    # So google-fu to : RSA CRT attack -fault     gave me some other possibilities.
    #   https://mathoverflow.net/questions/120160/attack-on-crt-rsa
    print("Cracking RSA... (hopefully under 15min)")
    p = crackRSA(pubmod, clue)
    q = pubmod // p
    r.sendline(bytearray(str(p + q), 'utf-8'))
    flag = r.recvlineS(keepends = False)
    print(f"Flag: {flag}")




if __name__ == '__main__':
    main()