#!/usr/bin/python
#_*_coding:utf-8_*_

import sys


def main():
    n = sys.argv[1]
    new_list = []
    for line in open("hightemp.txt", 'r'):
        line = line.strip()
        new_list.append(line)
    l = len(new_list) / int(n)
    for i, line in enumerate(new_list):
        line = line.strip()
        print line
        if i % l == l - 1:
            print("\n")

if __name__ == "__main__":
    main()

