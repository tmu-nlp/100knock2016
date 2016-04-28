#!/usr/bin/pyhton
#_*_coding:utf-8_*_



def main():
    fin = open("hightemp.txt")
    count = 0
    for line in fin:
        line = line.strip()
        count += 1
    print count


if __name__ == "__main__":
    main()

