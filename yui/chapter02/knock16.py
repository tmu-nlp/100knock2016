# -*- coding: utf-8 -*-


# ファイルをN分割する
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを
# 行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．



import sys

n = int(sys.argv[1])
input_file = open("hightemp.txt", "r")
line_list =[]

for line in input_file:
    line_list.append(line.strip())

file_line_num = len(line_list)
line_num_per_file = -(-file_line_num / n)
for file_index in range(1, n+1):
    output_file = open("hightemp_split%d.txt" % file_index, "w")
    for i in range(line_num_per_file):
        output_file.write("%s\n" %line_list.pop(0))
        if len(line_list) == 0:
            break
    output_file.close()
