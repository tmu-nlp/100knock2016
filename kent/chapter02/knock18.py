#!/usr/bin/python
#!_*_coding:utf-8_*_



def main():
    fin = open("hightemp.txt")
    temp_list = list()
    for line in fin:
        line = line.strip().split("\t")
        temp_list.append(float(line[2]))
    for line in sorted(temp_list, key=lambda x: -x):
        print line


if __name__ == "__main__":
    main()

