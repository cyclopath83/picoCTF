#!/usr/bin/env python

from tqdm import tqdm

output = open('output.txt', 'r').read()
random_strs = [         # We need to go in the reverse order
    b'break it',
    b'ever',
    b'and you will never',
    b'is absolutely impenetrable',
    b'my encryption method'
]
enc_flags = []
enc_flags.append(bytes.fromhex(output))  # If all randoms were even, the encrypted flag would be our output, so let's already add that as a possible encrypted flag. Plus we need to start with something in our recursive method.

# Grabbed from encrypt.py
def encrypt(ptxt, key):
    ctxt = b''
    for i in range(len(ptxt)):
        a = ptxt[i]
        b = key[i % len(key)]
        ctxt += bytes([a ^ b])
    return ctxt



def get_possible_encrypted_flags():
    global enc_flags
    for random_str in tqdm(random_strs, desc="Calculating possible encrypted flags"):
        temp_enc_flags = []
        for enc_flag in enc_flags:
            enc = encrypt(enc_flag, random_str)
            if enc not in enc_flags and enc not in temp_enc_flags:
                temp_enc_flags.append(enc)
        enc_flags += temp_enc_flags
    print(f"Found {len(enc_flags)} unique possible encrypted flags")
    return


def main():
    # Step 1) Get all possible encrypted flags
    #
    # During the encrypt script, first the flag is being encrypted with the key. This is the encrypted flag we are looking for.
    # After the flag is encrypted, it is re-encrypted multiple times with those 'random_strs'.
    # The encryption is just an XOR, so no matter how many times your XOR a string with the same key, you don't get different values.
    # If you XOR it 1, 3, 5, ... times you get the same value. If you XOR it 0, 2, 4, 6, ... times you also get a same value.
    # So we only have 2 different possible values per 'random_str' (if it was XOR'ed an even or odd number of times)
    # Since we only have a handful of random_strs (5 unique ones), we only have 2**5 = 32 possible encrypted flags.
    # Lets find those
    get_possible_encrypted_flags()


    # Step 2) Grab all the potential keys
    # Now that we have all the possible encrypted flags, we can only decrypt it with the key (which we don't have)
    # Luckily we do know that the flag will start with 'picoCTF{', so if we XOR our pottential encrypted flags with 'picoCTF{', we get the first part (and hopefully the full key) of the key
    # And as we know, with XOR, the encryption function is also the decryption function.
    keys = []
    for enc_flag in tqdm(enc_flags, desc="Calculate possible encryption keys"):
        keys.append(encrypt(enc_flag, b'picoCTF{')[:7])

    
    # Step 3) Let's try all possible keys, to all possible encrypted flags, and see if some cleartext starts with 'picoCTF{'
    for enc_flag in enc_flags:
        for key in keys:
            check = encrypt(enc_flag, key)
            if "picoCTF{" in check.decode():
                print(f"Found the flag: {check}")
                break

if __name__ == '__main__':
    main()