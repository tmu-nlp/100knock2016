# -*- coding: utf-8 -*-


# 末尾のN行を出力
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行
# だけを表示せよ．確認にはtailコマンドを用いよ．


import sys

n = int(sys.argv[1])
input_file = open("hightemp.txt", "r")
line_list =[]

for line in input_file:
    line_list.append(line.strip())

for line in line_list[-n:]:
    print (line)

#tail -n 5 hightemp.txt
