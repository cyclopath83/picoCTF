#!/usr/bin/env python


def main():
    flag = open("enc").read()
    print(''.join(chr(ord(c) >> 8) + chr(ord(c) % 256) for c in flag))


if __name__ == '__main__':
    main()
