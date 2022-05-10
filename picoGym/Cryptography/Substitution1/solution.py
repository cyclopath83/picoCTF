#!/usr/bin/env python

enc = 'OYAt (txwsy aws ompyksb yxb ajmf) msb m yupb wa owzpkybs tboksgyu owzpbygygwd. Owdybtymdyt msb psbtbdybr lgyx m tby wa oxmjjbdfbt lxgox ybty yxbgs osbmygegyu, yboxdgomj (mdr fwwfjgdf) tqgjjt, mdr pswhjbz-twjegdf mhgjgyu. Oxmjjbdfbt ktkmjju owebs m dkzhbs wa omybfwsgbt, mdr lxbd twjebr, bmox ugbjrt m tysgdf (omjjbr m ajmf) lxgox gt tkhzgyybr yw md wdjgdb towsgdf tbsegob. OYAt msb m fsbmy lmu yw jbmsd m lgrb mssmu wa owzpkybs tboksgyu tqgjjt gd m tmab, jbfmj bdegswdzbdy, mdr msb xwtybr mdr pjmubr hu zmdu tboksgyu fswkpt mswkdr yxb lwsjr aws akd mdr psmoygob. Aws yxgt pswhjbz, yxb ajmf gt: pgowOYA{AS3CK3DOU_4774OQ5_4S3_O001_6B0659AH}'
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# We need to figure out the key here. I'm doing this in several itterations.
# 1. we know that the flag has the format picoCTF, so "pgowOYA" must be substituted to "picoCTF"
key      = "??O??A??G?????WP???Y??????"
# 2. First word is now "CTF?" which is probably "CTFs"... SO "OYAt" is substituted to "CTFs"
key      = "??O??A??G?????WP??TY??????"
# 3. I see a "m" as a single 'word' several times. Based on the English vocabolary, that is probably 'a'.
key      = "M?O??A??G?????WP??TY??????"
# 4. The 4th sentense now starts with "CTFs a?? a", which probably is "CTFs are a". (OYAt msb m)
key      = "M?O?BA??G?????WP?STY??????"
# 5. Now that first thing between the brackets starts to make sense: "OYAt (txwsy aws ompyksb yxb ajmf)" => "CTFs (s?ort for capt?re t?e f?a?)" => "CTFs (short for capture the flag)"
key      = "M?O?BAFXG??J??WP?STYK?????"
# 6. Now we can complete the rest of the key, because we can nearly read the entire plaintext. (The 3 that are still left are not needed, so we don't care.)
key      = "MHORBAFXG?QJZDWPCSTYKEL?U?"


def main():
    flag = ""
    for char in enc:
        if char.upper() in ALPHABET:
            i = key.find(char.upper())
            if i == -1:
                flag += "?"
            elif char in ALPHABET:
                flag += ALPHABET[i]
            else:
                flag += ALPHABET[i].lower()
        else:
            flag += char

    print(flag)



if __name__ == '__main__':
    main()
