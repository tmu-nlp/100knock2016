#coding: utf-8
import sys
f_in = open("hightemp.txt", "r")
col1 = open("col1.txt", "w")
col2 = open("col2.txt", "w")
for line in f_in:
        col = line.split("\t")
        col1.write(col[0] + "\n")
        col2.write(col[1] + "\n")
f_in.close()
col1.close()
col2.close()

#flamie:chapter02 tomoya$ cut -f1,2 hightemp.txt
#高知県  江川崎
#埼玉県  熊谷
#岐阜県  多治見
#山形県  山形
#山梨県  甲府
#和歌山県    かつらぎ
#静岡県  天竜
#山梨県  勝沼
#埼玉県  越谷
#群馬県  館林
#群馬県  上里見
#愛知県  愛西
#千葉県  牛久
#静岡県  佐久間
#愛媛県  宇和島
#山形県  酒田
#岐阜県  美濃
#群馬県  前橋
#千葉県  茂原
#埼玉県  鳩山
#大阪府  豊中
#山梨県  大月
#山形県  鶴岡
#愛知県  名古屋

