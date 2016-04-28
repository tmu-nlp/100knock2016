#!/usr/bin/python
#_*_coding:utf-8_*_


def main():
    fin = open("hightemp.txt")
    fout_1 = open("col1.txt", "w")
    fout_2 = open("col2.txt", "w")
    for line in fin:
        cols = line.strip().split("\t")
        fout_1.write("%s\n" % cols[0])
        fout_2.write("%s\n" % cols[1])
    fin.close()
    fout_1.close()
    fout_2.close()


if __name__ == "__main__":
    main()

