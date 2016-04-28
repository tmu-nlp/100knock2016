#!/usr/bin/python
#_*_coding:utf-8_*_


def main():
    str_1 = "パトカー"
    str_2 = "タクシー"
    str_1 = str_1.decode("utf-8")
    str_2 = str_2.decode("utf-8")
    for i in range(len(str_1)):
        print str_1[i:i+1] + str_2[i:i+1],


if __name__ == "__main__":
    main()

