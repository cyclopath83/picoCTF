#!/usr/bin/env python
  
import requests

def main():
    # Get the file
    print("Getting the file")
    URL = 'https://mercury.picoctf.net/static/a5683698ac318b47bd060cb786859f23/flag'
    response = requests.get(URL)

    # Print the file content
    print("The flag is:")
    fo = open("flag")
    print(fo.read())
    fo.close()

if __name__ == '__main__':
    main()
