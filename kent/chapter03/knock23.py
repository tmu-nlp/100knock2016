#!/usr/bin/python
#_*_coding:utf-8_*_

from knock20 import get_UK_text
import re

def main():
    char_1 = re.compile("(?P<section>=+)(?P<name>[^=]+)=+")
    for line in get_UK_text().split("\n"):
        matchOBJ = char_1.match(line)
        if matchOBJ:
            print line
            name = matchOBJ.group("name")
            level = len(matchOBJ.group("section"))
            print "name: %s" % name
            print "level: %s" % level


if __name__ == "__main__":
    main()

