#!/usr/bin/env python


#
# NOT WORKING YET!!!
#


import math

# INPUT
CIPHER = "Ta _7N6DDDhlg:W3D_H3C31N__0D3ef sHR053F38N43D0F i33___NA"
N = 4


# Global Vars
L = 0
K = 0
x = 0
y = 0



def printGrid(grid):
    for i in range(N):
        line = ""
        for j in range(len(grid[i])):
            line += grid[i][j]
        print(line)
    print()

def emptyGrid():
    global L, K, x, y

    # Do some math
    L = len(CIPHER)
    K = math.ceil(L / (2*(N-1)))
    
    # Create the empty grid
    grid = [[" " for i in range(L)] for j in range(N)]

    # Fill in '*' where a char should be.
    i = 0
    j = 0
    dir = 1
    for c in range(L):
        grid[i][j] = '*'
        j += 1
        if (i == 0) and (dir == -1):
            dir = 1
        if (i == N-1) and (dir == 1):
            dir = -1
        i += dir

    printGrid(grid)
    return grid 

def fillGrid(grid):
    c = 0
    for i in range(N):
        for j in range(L):
            if(grid[i][j] == '*'):
                grid[i][j] = CIPHER[c]
                c += 1
    printGrid(grid)
    return grid

def extractPlain(grid):
    i = 0
    j = 0
    dir = 1
    plain = ""
    for c in range(L):
        plain += grid[i][j]
        j += 1
        if (i == 0) and (dir == -1):
            dir = 1
        if (i == N-1) and (dir == 1):
            dir = -1
        i += dir
    print(plain)
    print()
    return plain

def main():
    # Create an empty grid with the correct dimensions
    grid = emptyGrid()

    # Fill each character of the cipher-text, on all the '*' starting with the first row, 2nd row, ... left to right.
    grid = fillGrid(grid)

    # Now let's extract the plaintext from the grid
    plain = extractPlain(grid)

    # Extract the picoCTF flag from the plaintext
    flag = "picoCTF{" + plain.split()[-1] + "}"
    print(flag)
    





if __name__ == '__main__':
    main()