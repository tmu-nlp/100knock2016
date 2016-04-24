#!/usr/bin/python
#_*_coding:utf-8_*_

import sys


def main():
    fin = open("hightemp.txt")
    n = sys.argv[1]
    for i, line in enumerate(fin):
        line = line.strip()
        if i == int(n):
            break
        else:
            print line
    fin.close()


if __name__ == "__main__":
    main()

