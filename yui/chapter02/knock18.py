# -*- coding: utf-8 -*-


# 各行を3コラム目の数値の降順にソート
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに
# 並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで
# 実行した時の結果と合わなくてもよい）．


original_file = open("hightemp.txt", "r")
lines = original_file.readlines()

split_lines = [line.split("\t") for line in lines]
sorted_lines = sorted(split_lines, key=lambda x: x[2], reverse=True)

for line in reversed(sorted_lines):
    print "\t".join(line).strip()

#sort -rk 3 hightemp.txt
