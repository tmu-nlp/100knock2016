#!/usr/bin/python
#_*_coding:utf-8_*_

import sys

def main():
    text = sys.argv[1]
    text = text.strip()
    words = text.split(" ")
    char_bi = list()
    word_bi = list()
    for index in range(len(text)):
        char_bi.append(text[index:index+2])
    print "char_bi-gram"
    print char_bi
    print "word_bi-gram:"
    for i in range(len(words)):
        print words[i:i+2],


if __name__ == "__main__":
    main()

