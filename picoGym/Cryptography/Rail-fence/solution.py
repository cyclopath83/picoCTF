#!/usr/bin/env python


#
# NOT WORKING YET!!!
#


import math

CIPHER = "Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NAxx".replace(" ","")
N = 4

def main():
    # Do all the math
    global CIPHER
    PLAIN = " "*len(CIPHER)
    L = len(CIPHER)
    K = math.ceil(L / (2* (N - 1)))
    x = 0
    y = 0
    if ( L % (2 * (N-1)) != 0):
        while L > (N + (N-1)*x):
            x += 1
        y = N + (N-1)*x - L
    CIPHER += "x"*y
    print(CIPHER)
    print(f"L={L}  -  K={K}  -  x={x}  -  y={y}")
    print()

    # Print all the lines
    i = 0
    for row in range(0, N):
        line = ""
        for j in range(0, K-1):
            line += ("  " * row)
            line += CIPHER[i] + " "
            PLAIN = PLAIN[0:j*K+row] + CIPHER[i] + PLAIN[j*K+row+1:]
            i += 1
            line += ("  " * (2 * (N - 1) - 1 - 2 * row) )
            if (row != 0) and (row != N-1 ):
                line += CIPHER[i] + " "
                PLAIN = PLAIN[0:j*K+row] + CIPHER[i] + PLAIN[j*K+row+1:]
                i += 1
            if row > 1:
                line += "  " * (row - 1)
            
        print(line)

    print()
    print(PLAIN)



if __name__ == '__main__':
    main()