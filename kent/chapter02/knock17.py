#!/usr/bin/python
#_*_coding:utf-8_*_


def main():
    fin = open("col1.txt")
    col1_list = list()
    for line in sorted(fin):
        col1_list.append(line.strip())
    for col in set(col1_list):
        print col
    print len(set(col1_list))


if __name__ == "__main__":
    main()

