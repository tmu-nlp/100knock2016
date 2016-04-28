#!/usr/bin/python
#_*_coding:utf-8_*_


def main():
    source_str = "パタトクカシーー"
    source_str = source_str.decode("utf-8")
    for index in [(i * 2) for i in range(4)]:
        print source_str[index:index + 1],


if __name__ == '__main__':
    main()
