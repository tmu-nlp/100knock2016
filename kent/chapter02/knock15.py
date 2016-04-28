#/usr/bin/python
#_*_coding:utf-8_*_

import sys


def main():
    fin = open("hightemp.txt")
    n = sys.argv[1]
    text_list = list()
    for line in fin:
        line = line.strip()
        text_list.append(line)
    for i, line in enumerate(text_list):
        if i < len(text_list) - int(n):
            continue
        else:
            print line


if __name__ == "__main__":
    main()

