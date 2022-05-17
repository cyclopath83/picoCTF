#!/usr/bin/env python

from pwn import *
from Crypto.Cipher import DES
import binascii
from tqdm import tqdm

HOST = 'mercury.picoctf.net'
PORT = 37751



# Reused from ddes.py
def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()


# From the ddes.py script, we see that keys are only 6-decimals in length. This should be easily bruteforceable.
# Double DES is vulnerable to a meet-in-the-middle attack. 
# 1) Encrypt 0x01 with all possible keys, and store the results
# 2) Decrypt the double-encrypted 0x01 once with all possible keys, and store the results
# 3) Find a value that exists in both results. This will give you the two keys that were used.
def bruteforce(encdata):
    # 1)
    plain01 = pad(binascii.unhexlify("01".rstrip()).decode())
    plain01results = {}
    for k1 in tqdm(range(999999), desc="Bruteforce Phase 1"):
        key1 = pad(str(k1).zfill(6))
        cipher1 = DES.new(key1, DES.MODE_ECB)
        plain01results[cipher1.encrypt(plain01)] = key1

    # 2)
    enc01 = binascii.unhexlify(encdata.rstrip())
    enc01results = {}
    for k2 in tqdm(range(999999), desc="Bruteforce Phase 2"):
        key2 = pad(str(k2).zfill(6))
        cipher2 = DES.new(key2, DES.MODE_ECB)
        enc01results[cipher2.decrypt(enc01)] = key2
    
    # 3)   
    print("Finding intersection")
    k1set = set(plain01results.keys())
    k2set = set(enc01results.keys())
    for v in k1set.intersection(k2set):
        key1 = plain01results[v]
        key2 = enc01results[v]
        print(f"Found the keys!!!!   K1: {key1}  -  K2: {key2}")
        return key1, key2
    



def main():
    # STEP 1: Connect to the host, and grab the encrypted flag
    r = remote(HOST, PORT)
    r.recvuntil(bytearray('flag:\n', 'utf-8'))
    encflag = r.recvlineS(keepends = False)
    print(f"Encrypted flag found: {encflag}")

    # STEP 2: Enter 01 as data to encrypt, and grab the encrypted data.
    r.sendlineafter(bytearray('encrypt? ', 'utf-8'), bytearray('01', 'utf-8'))
    enc01 = r.recvlineS(keepends = False)
    print(f"Received encrypted data for '0x01': {enc01}")

    # STEP 3: Bruteforce the 0x01 encrypted data
    k1, k2 = bruteforce(enc01)

    # STEP 4: Decrypt the flag with the 2 keys (first with k2, then with k1)
    cipher1 = DES.new(k2, DES.MODE_ECB)
    decrypt1 = cipher1.decrypt(binascii.unhexlify(encflag))
    cipher2 = DES.new(k1, DES.MODE_ECB)
    plainflag = cipher2.decrypt(decrypt1).decode()
    print(f"Flag found: {plainflag}")



if __name__ == '__main__':
    main()