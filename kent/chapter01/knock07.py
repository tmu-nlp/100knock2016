#!/usr/bin/python
#_*_coding:utf-8_*_

import sys


def main():
    x = int(sys.argv[1])
    y = sys.argv[2]
    z = float(sys.argv[3])
    print "%s時の%sは%s" % (x, y, z)


if __name__ == "__main__":
    main()


