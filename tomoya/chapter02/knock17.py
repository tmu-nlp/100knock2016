#coding: utf-8
import sys
f_in = open("hightemp.txt", "r")
prefectures = set()
for line in f_in:
  col = line.split("\t")
  prefectures.update([col[0]])
for x in prefectures:
  print(x)
f_in.close()

#flamie:chapter02 tomoya$ cut -f1 hightemp.txt | sort | uniq
#千葉県
#埼玉県
#大阪府
#山形県
#山梨県
#岐阜県
#愛媛県
#愛知県
#群馬県
#静岡県
#高知県
#和歌山県
