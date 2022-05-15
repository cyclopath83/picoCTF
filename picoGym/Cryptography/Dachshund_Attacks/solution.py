#!/usr/bin/env python

# A quick search with dachshund and rsa gives you the explanation of the Wiener's attack : https://en.wikipedia.org/wiki/Wiener%27s_attack
# Which is a method to expose the private key d when d is too small.
# And since a Wiener is also a dachshund, this sounds like the way to go.
# And I found a nice python script to do this: https://github.com/pablocelayes/rsa-wiener-attack/blob/master/RSAwienerHacker.py
# (Credits to pablocelayes)

from pwn import *
import ContinuedFractions, Arithmetic

HOST = "mercury.picoctf.net"
PORT = 37455


def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = ContinuedFractions.rational_to_contfrac(e, n)
    convergents = ContinuedFractions.convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = Arithmetic.is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d


# Int to ASCII, grabbed from my Mini_RSA solution
def int_to_ascii(m):
    # Decode to ascii (from https://crypto.stackexchange.com/a/80346)
    m_hex = hex(int(m))[2:-1]  # Number to hex
    m_ascii = "".join(
        chr(int(m_hex[i : i + 2], 16)) for i in range(0, len(m_hex), 2)
    )  # Hex to Ascii
    return m_ascii



def main():
    # Connect and grab e, n and c
    r = remote(HOST, PORT)
    r.recvuntil(bytearray("e: ", 'utf-8'))
    e = int(r.recvlineS(keepends = False))
    print(f"Found e: {e}")
    r.recvuntil(bytearray("n: ", 'utf-8'))
    n = int(r.recvlineS(keepends = False))
    print(f"Found n: {n}")
    r.recvuntil(bytearray("c: ", 'utf-8'))
    c = int(r.recvlineS(keepends = False))
    print(f"Found c: {c}")

    d = hack_RSA(e, n)
    print(f"Found d: {d}")


    # M = c**d mod n
    m = pow(c, d, n)
    print(f"Message found: {m}")
    M = int_to_ascii(m)
    print(f"Message: {M}")


if __name__ == '__main__':
    main()
