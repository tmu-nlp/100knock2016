# -*- coding: utf-8 -*-


# １列目の文字列の異なり
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort,
# uniqコマンドを用いよ．

#
original_file = open("col1.txt", "r")


lines = original_file.readlines()


col1_uniq = set()

for line in lines:
    col1_uniq.add(line.decode('utf8'))

for col1sets in col1_uniq:
    print col1sets.strip("\n")
