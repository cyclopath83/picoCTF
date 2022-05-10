#!/usr/bin/env python

enc = 'tzvwvvfsotovmvwrpktzvwcvppvotrlpsozvyzshzoizkkpikqgntvwovinwstjikqgvtstskeoseipnysehijlvwgrtwsktreynoijlvwizrppvehvtzvovikqgvtstskeoxkinogwsqrwspjkeojotvqoryqsesotwrtskexneyrqvetrpoczsizrwvmvwjnovxnpreyqrwuvtrlpvousppozkcvmvwcvlvpsvmvtzvgwkgvwgnwgkovkxrzshzoizkkpikqgntvwovinwstjikqgvtstskesoektkepjtktvrizmrpnrlpvousppolntrpoktkhvtotnyvetosetvwvotvysereyvfistvyrlkntikqgntvwoisveivyvxveosmvikqgvtstskeorwvkxtveprlkwsknorxxrsworeyikqvykcetkwneesehizviupsotoreyvfvintsehikexshoiwsgtokxxveovketzvktzvwzreysozvrmspjxkinovykevfgpkwrtskereysqgwkmsortskereykxtvezrovpvqvetokxgprjcvlvpsvmvrikqgvtstsketknizsehketzvkxxveosmvvpvqvetokxikqgntvwovinwstjsotzvwvxkwvrlvttvwmvzsipvxkwtvizvmrehvpsoqtkotnyvetoserqvwsirezshzoizkkpoxnwtzvwcvlvpsvmvtzrtreneyvwotreysehkxkxxveosmvtvizesanvosovoovetsrpxkwqknetsehrevxxvitsmvyvxveovreytzrttzvtkkporeyikexshnwrtskexkinoveiknetvwvyseyvxveosmvikqgvtstskeoykvoektpvryotnyvetotkuekctzvswvevqjrovxxvitsmvpjrotvrizsehtzvqtkritsmvpjtzseupsuvrerttriuvwgsikitxsorekxxveosmvpjkwsvetvyzshzoizkkpikqgntvwovinwstjikqgvtstsketzrtovvuotkhvevwrtvsetvwvotseikqgntvwoisveivrqkehzshzoizkkpvwotvrizsehtzvqveknhzrlkntikqgntvwovinwstjtkgsanvtzvswinwskostjqktsmrtsehtzvqtkvfgpkwvketzvswkcereyverlpsehtzvqtklvttvwyvxveytzvswqrizsevotzvxprhsogsikITX{E6W4Q_4E41J515_15_73Y10N5_42VR1770}'
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# We need to figure out the key here. I'm doing this in several itterations.
# 1. we know that the flag has the format picoCTF, so "gsikITX" must be substituted to "picoCTF"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key      = "??I??X??S?????KG???T??????"
# 2. I see "co?p?titio?" a few times. This must be "competition", right. (ikqgvtstske)
key      = "??I?VX??S???QEKG???T??????"
# 3. 'comp?te?' somewhere in the beginnen of the text could be 'computer' (ikqgntvw)
key      = "??I?VX??S???QEKG?W?TN?????"
# 4. Which reveals 'computer?ecurit?competition' (ikqgntvwovinwstjikqgvtstske) => 'computersecuritycompetition'
key      = "??I?VX??S???QEKG?WOTN???J?"
# 5. First word 't?ere' (tzvwv) => 'there'
key      = "??I?VX?ZS???QEKG?WOTN???J?"
# 6. 'schoo?computersecuritycompetitionsinc?u?in?cy?er' (oizkkpikqgntvwovinwstjikqgvtstskeoseipnysehijlvw) => 'schoolcomputersecuritycompetitionsincludingcyber'
key      = "?LIYVXHZS??PQEKG?WOTN???J?"
# 7. 'cyberp?triot?nduscyberch?llenge' (ijlvwgrtwsktreynoijlvwizrppvehv) => 'cyberpatriotanduscyberchallenge'.
# This is sufficient to get the full flag, no need to go further.
key      = "RLIYVXHZS??PQEKG?WOTN???J?"



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
