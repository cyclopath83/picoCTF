#!/usr/bin/env python

#
# NOT WORKING YET!
#

enc = 'Tmnmfiwk Cmlnvkh vnwqm, peyt v lnvam vkh qyvymcb ven, vkh onwflty dm ytm ommycm jnwd v lcvqq uvqm ek pteut ey pvq mkucwqmh. Ey pvq v omvfyejfc quvnvovmfq, vkh, vy ytvy yedm, fkzkwpk yw kvyfnvceqyq—wj uwfnqm v lnmvy inerm ek v quemkyejeu iweky wj aemp. Ytmnm pmnm ypw nwfkh ocvuz qiwyq kmvn wkm mgynmdeyb wj ytm ovuz, vkh v cwkl wkm kmvn ytm wytmn. Ytm quvcmq pmnm mgummheklcb tvnh vkh lcwqqb, peyt vcc ytm viimvnvkum wj ofnkeqtmh lwch. Ytm pmelty wj ytm ekqmuy pvq amnb nmdvnzvocm, vkh, yvzekl vcc yteklq ekyw uwkqehmnvyewk, E uwfch tvnhcb ocvdm Sfieymn jwn teq wiekewk nmqimuyekl ey. Ytm jcvl eq: ieuwUYJ{5FO5717F710K_3A0CF710K_357OJ9JJ}'
key = "VOUHMJLTESZCDKWIXNQYFAPGBR"

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    flag = ""
    k = 0
    for char in enc:
        if char.upper() in ALPHABET:
            j = (ord(char) - ord('A') - ord(key[k]) - ord('A')) % 26
            if char in ALPHABET:
                flag += ALPHABET[j]
            else:
                flag += ALPHABET[j].lower()
            k = (k + 1) % (len(key))
        else:
            flag += char

    print(flag)



if __name__ == '__main__':
    main()
