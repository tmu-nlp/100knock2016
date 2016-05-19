#!/usr/bin/python
#_*_coding:utf-8_*_

from knock20 import get_UK_text
import re

def main():
    char_1 = re.compile("(Category:(?P<word1>.+?)\|)|(Category:(?P<word2>.+?)])")
    for line in get_UK_text().split("\n"):
        matchOBJ = char_1.search(line)
        if matchOBJ:
            word1 = matchOBJ.group("word1")
            word2 = matchOBJ.group("word2")
            if word1:
                print word1
            else:
                print word2


if __name__ == "__main__":
    main()

