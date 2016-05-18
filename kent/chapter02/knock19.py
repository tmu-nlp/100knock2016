#!/usr/bin/python
#!_*_coding:utf-8_*_

from collections import defaultdict


def main():
    word2freq = defaultdict(lambda: 0)
    fin = open("col1.txt")
    for line in fin:
        word2freq[line.strip()] += 1
    for key, value in sorted(word2freq.items(), key=lambda x: -x[1]):
        print key, value


if __name__ == "__main__":
    main()

