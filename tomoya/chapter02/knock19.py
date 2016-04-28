#coding: utf-8
import sys
f_in = open("hightemp.txt", "r")
Data = dict()
for line in f_in:
  col = line.split("\t")[0]
  Data.setdefault(col, []).append(line)
for k, v in sorted(Data.items(), key=lambda x:len(x[1]), reverse=True):
  print("".join(v), end="")

#flamie:chapter02 tomoya$ cut -f1 hightemp.txt| sort | uniq -c | sort -rk1
#   3 群馬県
#   3 山梨県
#   3 山形県
#   3 埼玉県
#   2 静岡県
#   2 愛知県
#   2 岐阜県
#   2 千葉県
#   1 和歌山県
#   1 高知県
#   1 愛媛県
#   1 大阪府
