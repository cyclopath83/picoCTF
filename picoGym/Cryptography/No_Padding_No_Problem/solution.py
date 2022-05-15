#!/usr/bin/env python


# When you connect to the challenge manually, it welcomes you to the "Padding Oracle Challange"
# A quick google search resulted in the "RSA Padding Oracle Attack" : 
#   https://en.wikipedia.org/wiki/Padding_oracle_attack
#   https://shainer.github.io/crypto/matasano/2017/10/14/rsa-padding-oracle-attack.html
# What it drills down to is that RSA is homomorphic:
# E(m1) * E(m2) = ( m1**e  *  m2**e) mod n = (m1 * m2)**e mod n = E(m1 * m2)
# We get E(m1), and we can easily encrypt a chosen m2 ourselves using e and n.
# If we multiply those 2 encrypted messages, and give that as a ciphertext, it will decrypt that multiplied message.
# So we can get m1 by dividing the returned decrypted text by our chosen m2.


from pwn import *

HOST = "mercury.picoctf.net"
PORT = 10333



def main():
    r = remote(HOST, PORT)
    r.recvuntil(bytearray("n: ", 'utf-8'))
    n = int(r.recvlineS(keepends = False))
    print(f"Found n: {n}")
    r.recvuntil(bytearray("e: ", 'utf-8'))
    e = int(r.recvlineS(keepends = False))
    print(f"Found e: {e}")
    r.recvuntil(bytearray("ciphertext: ", 'utf-8'))
    ct1 = int(r.recvlineS(keepends = False))
    print(f"Found ciphertext: {ct1}")


    # Encrypt a known easy value (ex 2)
    ct2 = pow(2, e, n)
    
    # Multiply those 2 encrypted messages
    ct12 = ct1 * ct2
    # Send the multiplied ciphertext to decrypt
    r.sendlineafter(bytearray("decrypt: ", 'utf-8'), bytearray(str(ct12), 'utf-8'))
    r.recvuntil(bytearray("go: ", 'utf-8'))
    pt12 = int(r.recvlineS(keepends = False))

    # Divide the received decrypted text by our chosen easy value
    pt1 = pt12 // 2
    PT = bytearray.fromhex(format(pt1, 'x')).decode()
    print(PT)

if __name__ == '__main__':
    main()