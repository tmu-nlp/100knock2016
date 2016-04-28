#!/usr/bin/pyhton
#_*_coding:utf-8_*_


def main():
    nums = list()
    source_str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    words = source_str.strip().split()
    for word in words:
        nums.append(len(word))
    print nums


if __name__ == '__main__':
    main()
