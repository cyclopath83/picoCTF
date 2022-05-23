#!/usr/bin/env python

from pwn import *
from Crypto.Util.number import *
from decimal import *

HOST = "jupiter.challenges.picoctf.org"
PORT = 18821


getcontext().prec = MAX_PREC


# Int to ASCII, grabbed from my Mini_RSA solution
def int_to_ascii(m):
    # Decode to ascii (from https://crypto.stackexchange.com/a/80346)
    m_hex = hex(int(m))[2:]  # Number to hex
    m_ascii = "".join(
        chr(int(m_hex[i : i + 2], 16)) for i in range(0, len(m_hex), 2)
    )  # Hex to Ascii
    return m_ascii



def main():
    # 1st Challenge (n = p*q)
    r = remote(HOST, PORT)
    r.recvuntil(bytearray('q : ', 'utf-8'))
    q = int(r.readlineS(keepends = False))
    r.recvuntil(bytearray('p : ', 'utf-8'))
    p = int(r.readlineS(keepends = False))
    n = p * q
    print(f"1)  p={p}  -  q={q}  => n={n}")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('Y', 'utf-8'))
    r.sendlineafter(bytearray('n: ', 'utf-8'), bytearray(str(n), 'utf-8'))


    # 2nd Challenge (q = n/p)
    r.recvuntil(bytearray('p : ', 'utf-8'))
    p = int(r.readlineS(keepends = False))
    r.recvuntil(bytearray('n : ', 'utf-8'))
    n = int(r.readlineS(keepends = False))
    q = int(n/p)
    print(f"2)  p={p}  -  n={n}  => q={q}")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('Y', 'utf-8'))
    r.sendlineafter(bytearray('q: ', 'utf-8'), bytearray(str(q), 'utf-8'))


    # 3rd Challenge (p and q from N : not possible)
    print("3)  Not possible")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('N', 'utf-8'))
    

    # 4th Challenge  phi = (p-1)*(q-1)
    r.recvuntil(bytearray('q : ', 'utf-8'))
    q = int(r.readlineS(keepends = False))
    r.recvuntil(bytearray('p : ', 'utf-8'))
    p = int(r.readlineS(keepends = False))
    phi = ((p-1)*(q-1))
    print(f"4)  p={p}  -  q={q}  => phi={phi}")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('Y', 'utf-8'))
    r.sendlineafter(bytearray('totient(n): ', 'utf-8'), bytearray(str(phi), 'utf-8'))


    # 5th Challenge C = (M**e) mod n
    r.recvuntil(bytearray('plaintext : ', 'utf-8'))
    plain = int(r.readlineS(keepends = False))
    r.recvuntil(bytearray('e : ', 'utf-8'))
    e = int(r.readlineS(keepends = False))
    r.recvuntil(bytearray('n : ', 'utf-8'))
    n = int(r.readlineS(keepends = False))
    ctxt = pow(plain, e, n)
    print(f"5)  plaintext={plain}, e={e}, n={n}  => ciphertext={ctxt}")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('Y', 'utf-8'))
    r.sendlineafter(bytearray('ciphertext: ', 'utf-8'), bytearray(str(ctxt), 'utf-8'))


    # 6th Challenge Not possible
    print("6)  Not possible")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('N', 'utf-8'))
    

    # 7th Challenge : d = inv(e, phi) 
    r.recvuntil(bytearray('q : ', 'utf-8'))
    q = int(r.readlineS(keepends = False))
    r.recvuntil(bytearray('p : ', 'utf-8'))
    p = int(r.readlineS(keepends = False))
    r.recvuntil(bytearray('e : ', 'utf-8'))
    e = int(r.readlineS(keepends = False))
    phi = (p-1)*(q-1)
    d = inverse(e, phi)
    print(f"7)  q={q}, p={p}, e={e}  => d={d}")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('Y', 'utf-8'))
    r.sendlineafter(bytearray('d: ', 'utf-8'), bytearray(str(d), 'utf-8'))


    # 8th Challenge : q = n/p  -->  phi = (p-1)(q-1)  -->  d = inv(e,phi)  -->  M = (ctxt**d) mod(n)
    # Had to use Decimal here, for all the other challenges, int was big enough
    r.recvuntil(bytearray('p : ', 'utf-8'))
    p = Decimal(r.readlineS(keepends = False))
    r.recvuntil(bytearray('ciphertext : ', 'utf-8'))
    ctxt = Decimal(r.readlineS(keepends = False))
    r.recvuntil(bytearray('e : ', 'utf-8'))
    e = Decimal(r.readlineS(keepends = False))
    r.recvuntil(bytearray('n : ', 'utf-8'))
    n = Decimal(r.readlineS(keepends = False))
    q = n/p
    phi = (p-1)*(q-1)
    d = inverse(e, phi)
    plain = pow(ctxt, d, n)
    print(f"8)  p={p}, ctxt={ctxt}, e={e},  n={n}  => q={q},  phi={phi},  d={d},  plain={plain}")
    r.sendlineafter(bytearray('(Y/N):', 'utf-8'), bytearray('Y', 'utf-8'))
    r.sendlineafter(bytearray('plaintext: ', 'utf-8'), bytearray(str(plain), 'utf-8'))


    # Done, time to decode the flag
    flag = int_to_ascii(plain)
    print(f"Flag = {flag}")

if __name__ == '__main__':
    main()