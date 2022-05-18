#!/usr/bin/env python


# experimenting with the nc inputs, it was clear that the output was just the encryption of the individual characters combined, but sometimes the order of the characters was scrambled (hence the name I guess)
# My initial thought was to encrypt each of the possible characters individually, and then map the encryption to the flag.
# However, it seems if I encrypted 'p' and 'i' and 'pi' (to make picoCTF), I always found 'p' in 'pi'/'pic'/'pico'/... but never the 'i', 'c', ...
# But if I removed the encrypted 'p' from the encrypted 'pi', I got the encrypted 'i' on the 2nd location, and that string I was able to find in 'pi'/'pic'/'pico'
# So, I'll have to bruteforce char by char, and removing the previous encrypted chars to get the encryped last char (if that makes sense: remove enc_p from enc_pi to get enc_i on spot 2)


from re import M
from pwn import *
from tqdm import tqdm

HOST = "mercury.picoctf.net"
PORT = 61477
r = remote(HOST, PORT)

CHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_{}"

FLAGENC = ""
MAP = {}

def findnext():
    pre = ''
    for c in MAP.values():
        pre += c
    for c in CHARS:
        testflag = pre + c
        r.sendlineafter(bytearray('give me: ', 'utf-8'), bytearray(testflag, 'utf-8'))
        r.recvuntil(bytearray('go: ', 'utf-8'))
        check = r.recvlineS(keepends = False)
        for e in MAP.keys():
            check = check.replace(e, "")
        if FLAGENC.find(check) != -1:
            print(f"Found next char: {c}")
            MAP[check] = c
            return c


def main():
    global FLAGENC
    r.recvuntil(bytearray('flag: ', 'utf-8'))
    FLAGENC = r.recvlineS(keepends = False)
    r.recvlineS(keepends = False)
    r.recvlineS(keepends = False)
    print("Grabbed Encrypted flag")

    
    
    while True:
        c = findnext()
        if c == '}':
            break
    
    flag = ''
    for c in MAP.values():
        flag += c
    print(f"Flag found: {flag}")


if __name__ == '__main__':
    main()