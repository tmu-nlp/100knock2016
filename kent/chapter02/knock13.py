#!/usr/bin/python
#_*_coding:utf-8_*_


def main():
    fin_1 = open("col1.txt")
    fin_2 = open("col2.txt")
    fout = open("merged_col1_col2.txt", "w")
    for col1, col2 in zip(fin_1, fin_2):
        col1 = col1.strip()
        col2 = col2.strip()
        fout.write("%s\t%s\n" % (col1, col2))
    fin_1.close()
    fin_2.close()
    fout.close()


if __name__ == "__main__":
    main()

