#!/usr/bin/env python
  
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
msg = "202 137 390 235 114 369 198 110 350 396 390 383 225 258 38 291 75 324 401 142 288 397".split()

def main():
    flag = "picoCTF{"
    for num in msg:
        i = int(num) % 37
        flag += abc[i]
    flag += "}"
    print(flag)

if __name__ == '__main__':
    main()
