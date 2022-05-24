#!/usr/bin/env python

# I have the feeling this looks aweful lot like Mini_RSA.
# N and e are known, and e=3, which is too small to be secure.
# So trying the same approach. Except here I don't know which message starts with 'picoCTF{', however, if we find any of the other messages, we know we can stop as well.


from decimal import *


def int_to_ascii(m):
    # Decode to ascii (from https://crypto.stackexchange.com/a/80346)
    m_hex = hex(int(m))[2:]  # Number to hex
    m_ascii = "".join(
        chr(int(m_hex[i : i + 2], 16)) for i in range(0, len(m_hex), 2)
    )  # Hex to Ascii
    return m_ascii




def crack(c, N, e):
    # It seems this function was even easier than in miniRSA. With a low precision you could already decrypt the entire message.

    getcontext().prec = 300
    for x in range(0, 1_000):
        # And e=3, thus we need to get the 3-rd square root of M**e to get M.
        # M**3**1/3 = M
        # M = (x*N + c)**1/3
        M = pow(x * N + c, 1 / e)

        # Convert the binary number to an ascii string
        m_ascii = int_to_ascii(M)
        if ("pico" in m_ascii) or ("I just" in m_ascii) or ("I hope" in m_ascii) or ("Rowing" in m_ascii):
            # For some reason my flag ends in a pipe, instead of a closed curly bracket. Could be my mistake of from the challenge. Either way, doesn't matter.
            print(int_to_ascii(M).replace("|", "}"))
            break

    return




def main():
    n = Decimal(0)
    e = Decimal(3)
    c = Decimal(0)
    with open('encrypted-messages.txt', 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        if line[0:3] == "n: ":
            n = Decimal(line[3:])
        if line[0:3] == "c: ":
            c = Decimal(line[3:])
        if line == '\n':
            crack(c, n, e)


if __name__ == '__main__':
    main()
