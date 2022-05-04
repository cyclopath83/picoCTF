#!/usr/bin/env python

import socket

def main():
    HOST = "mercury.picoctf.net"
    PORT = 49039

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(1024)

    chars = data.split()
    FLAG = ""
    for c in chars:
        FLAG += chr(int(c))
    print(FLAG)

if __name__ == '__main__':
    main()
