# -*- coding: utf-8 -*-


# 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

#
# original_file = open("hightemp.txt", "r")
# lines = original_file.readlines()
#

import sys
from collections import defaultdict


with open("hightemp.txt", "r") as f:
    lines = f.readlines()

    freq_dict = defaultdict(int)
    for line in lines:
        col1 = line.split("\t")[0]
        freq_dict[col1] += 1

    for s, f in sorted(sorted(freq_dict.items(), reverse=True), key=lambda x: x[1], reverse=True):
        print s, f

#cut -f 1 hightemp.txt | sort | uniq -c | sort -nr
