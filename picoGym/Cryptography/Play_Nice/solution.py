#!/usr/bin/env python

from pwn import *

HOST = "mercury.picoctf.net"
PORT = 40742
SQUARE_SIZE = 6


# Grabbed from the provided script, if we can extract the alphabet, we can create our encoding-square
def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

# Grabbed from provided script.
def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

# Converted with info from the encrypt_pair function of the provided script.
def decrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix)
	p2 = get_index(pair[1], matrix)

    # If it's a column, they go one row down. So we need to go one row up. (Hence -1 instead of +1)
	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
    # If it's a row, they go 1 column to the right. So we need to go one column to the left. (Hence -1 instead of +1)
	elif p1[1] == p2[1]:
		return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
	else:
    # If it's a rectangle, they go same row, opposite colums. We need to do the same. (no change)
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]


def decrypt_string(enc, matrix):
    result = ""
    for i in range(0, len(enc), 2):
        result += decrypt_pair(enc[i:i+2], matrix)
    return result


def main():
    # Connect and grab the alphabet and encrypted message
    r = remote(HOST, PORT)
    r.recvuntil(bytearray("alphabet: ", 'utf-8'))
    abc = r.recvlineS(keepends = False)
    print(f"alpabet found: {abc}")
    r.recvuntil(bytearray("message: ", 'utf-8'))
    enc = r.recvlineS(keepends = False)
    print(f"encrypted message found: {enc}")
    print()

    # Create the encoding-square
    matrix = generate_square(abc)
    print("Created encoding matrix:")
    for row in matrix:
        print(row)
    print()

    # Decrypt the message and send it to the server
    plain = decrypt_string(enc, matrix)
    print(f"Found the unencrypted message: {plain}")
    r.sendlineafter(bytearray("message? ", 'utf-8'), bytearray(plain, 'utf-8'))
    flag = r.recvlineS(keepends = False)
    print(f"Received the flag: {flag}")
    print("\nUse the flag like this, not with the picoCTF{flag} format!!!")


if __name__ == '__main__':
    main()