#!/usr/bin/env python

from pwn import *


HOST = "mercury.picoctf.net"
PORT = 11188
KEY_LEN = 50000

def main():
    # Connect and grab the encrypted flag
    r = remote(HOST, PORT)
    r.recvuntil(bytearray("flag!\n", 'utf-8'))
    enc = r.recvlineS(keepends = False)
    print(f"Encryted flag found: {enc}")
    binenc = unhex(enc)

    # Send A's untill the end of the OTP length, causing a wrap around back to the start of the OTP
    bytesToSend = KEY_LEN - len(binenc)
    while bytesToSend > 0:
        r.sendlineafter(bytearray("encrypt? ", 'utf-8'), bytearray("A" * min(100, bytesToSend), 'utf-8'))
        bytesToSend -= 100

    # Now send the encrypted flag again, to get the flag in cleartext (XOR is 2 way)
    r.sendlineafter(bytearray("encrypt? ", 'utf-8'), binenc)
    r.recvlineS()
    binflag = r.recvlineS()
    flag = str(unhex(binflag)).split('\'')[1]
    print(f'Decrypted flag found: picoCTF{{{flag}}}')


if __name__ == '__main__':
    main()
