#!/usr/bin/env python



# Both the flag and the study-guide are encrypted using the same scrambled alphabet.
# The study-guide is for a spelling test, so it will contain all English words
alphabet ='abcdefghijklmnopqrstuvwxyz'
encflag = 'brcfxba_vfr_mid_hosbrm_iprc_exa_hoav_vwcrm'

def main():
    # Step 1 : Do a frequency analyses of the study guide
    guide = open('study-guide.txt', 'r').read()
    # Using the first 100 words in the study-guide, I got the following decoding string from https://www.boxentriq.com/code-breaking/cryptogram
    freq = "sprgwhkjoqzldcuvyemnbtiafx"

    # Step 2 : decrypt 20 words from study-guide to see if we get the same result as the above website. (optional)
    word = ''
    i=0
    for c in guide:
        if c in alphabet:
            word += freq[ord(c) - ord('a')]
        else:
            print(word)
            word = ''
            i += 1
            if i > 20:
                break
    print("\n\n")

    # Step 3: decrypt our flag
    flag = ''
    for c in encflag:
        if c in alphabet:
            flag += freq[ord(c) - ord('a')]
        else:
            flag += c
    print(f"Flag found: {flag}")



if __name__ == '__main__':
    main()