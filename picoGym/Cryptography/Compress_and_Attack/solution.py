#!/usr/bin/env python

# Look at my modified compress_and_attack.py script.
# I've created my own flag (CyclopathRocks)
# And added some debugging print() functions. (was not needed in the end)
# Googled a lot, no known attacks on Salsa20, so had to look somewhere else
# Played around, and noticed if I provided parts of my known flag (2 or more chars), the length of my encrypted data stayed the same.
# If I entered a wrong char, the length of the encrypted data encreased.
# This obviously is due to the compacting (same chars only stored once or so)
# This allows for a bruteforce attack to guess the flag char by char.


from pwn import *

HOST = "mercury.picoctf.net"
PORT = 33976
# Connect to the remote host
r = remote(HOST, PORT)

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}_'


# I'll need to be sending a lot of test flags, and grabbing the length of the encrypted data.
# So to not have to repeat my code...
def sendFlagGetLength(flag):
    r.sendlineafter(bytearray('encrypted: ', 'utf-8'), bytearray(flag, 'utf-8'))
    # don't care about the nonce
    r.recvlineS(keepends = False)
    # don't care about the encrypted data
    r.recvlineS(keepends = False)
    # do care about the length
    l = r.recvlineS(keepends = False)
    return l




def findNextChar(flag, l):
    for c in CHARS:
        testflag = flag + c
        check = sendFlagGetLength(testflag)
        if l == check:
            print(f"Found next char: {c}")
            return c
    print("Didn't find next char... :-(")
    return '?'






def main():
    # We know the flag should start with picoCTF{
    # Provide this as input and let's see what the lenght of our encryped data will be.
    flag = 'picoCTF{'
    l = sendFlagGetLength(flag)
    print(f"Found target length: {l}")


    # Now we can bruteforce guessing the flag, untill we end with a }
    while True:
        c = findNextChar(flag, l)
        flag += c
        if c == '}':
            break
    print(f"Flag found: {flag}")

if __name__ == '__main__':
    main()
