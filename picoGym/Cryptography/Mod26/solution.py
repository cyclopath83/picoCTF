#!/usr/bin/env python
          
def main():
    CIPHER = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"
    PLAIN = ""
    abc = "abcdefghijklmnopqrstuvwxyz"
    ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for c in CIPHER:
        lower = abc.find(c)
        upper = ABC.find(c)
        if lower > -1:
            PLAIN += abc[(abc.find(c)+13)%26]
        elif upper > -1:
            PLAIN += ABC[(ABC.find(c)+13)%26]
        else:
            PLAIN += c

    print(PLAIN)

if __name__ == '__main__':
    main()
