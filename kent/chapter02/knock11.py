#/usr/bin/python
#_*_coding:utf-8_*_


def main():
    fin = open("hightemp.txt")
    for line in fin:
        words = line.strip().split("\t")
        print " ".join(words)
    fin.close()


if __name__ == "__main__":
    main()

