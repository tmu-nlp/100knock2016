#!/usr/bin/python
#_*_coding:utf-8_*_


def main():
    word2index = dict()
    source_str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    words = source_str.strip().split(" ")
    nums = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    for i, word in enumerate(words):
        if i + 1 in nums:
            word2index[i] = word[:1]
        else:
            word2index[i] = word[:2]
    for i, j in word2index.items():
        print i, j


if __name__ == '__main__':
    main()
