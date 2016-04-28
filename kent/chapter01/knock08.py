#!/usr/bin/python
#_*_coding:utf-8_*_

import sys


def cipher(text):
    ans = ""
    for char in text:
        if char.islower():
            code = ord(char)
            code = 219 - code
            ans += chr(code)
        else:
            ans += char
    return ans


def main():
    input_str = sys.argv[1]
    new_text = cipher(input_str)
    print new_text


if __name__ == "__main__":
    main()

