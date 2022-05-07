#!/usr/bin/env python
  
# This time they say the abc is 1-26, not 0-25 so I appended an underscore to offset with 1
abc = "_abcdefghijklmnopqrstuvwxyz0123456789_"
msg = "104 290 356 313 262 337 354 229 146 297 118 373 221 359 338 321 288 79 214 277 131 190 377".split()
m = 41

def main():
    flag = "picoCTF{"
    for num in msg:
        a = int(num) % m
        res = pow(a, -1, m)
        print(res)
        flag += abc[res]
    flag += "}"
    print(flag)

if __name__ == '__main__':
    main()
