# -*- coding: utf-8 -*-


# 先頭からN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行
# だけを表示せよ．確認にはheadコマンドを用いよ．

import sys

print sys.argv

n = int(sys.argv[1])

input_file = open("hightemp.txt", "r")

i = 0

for line in input_file:
    i += 1
    if i == n:
        break

    print (line)

#
# import sys
#
# n = int(sys.argv[1])
# input_file = open("hightemp.txt", "r")
# line_list =[]
#
# for line in input_file:
#     line_list.append(line.strip())
#
# for line in line_list[:n]:
#     print line

#head -n 5 hightemp.txt
