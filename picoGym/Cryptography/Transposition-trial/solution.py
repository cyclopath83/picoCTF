#!/usr/bin/env python

# 1st word = 3 letters => The
# Seems the 1st letter of those 3-letter-blocks has moved to the back, so we need to bring those to the front.
CIPHER = 'heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V9AAB1F8}7'

def main():
    PLAIN = ""
    for i in range(0, len(CIPHER), 3):
        PLAIN += CIPHER[i+2] + CIPHER[i:i+2]
    print(PLAIN)

if __name__ == '__main__':
    main()