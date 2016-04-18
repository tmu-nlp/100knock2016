# -*- coding: utf-8 -*-


# 元素記号
# "Hi He Lied Because Boron Could Not Oxidize Fluorine.
# New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の
# 1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から
# 単語の位置（先頭から何番目の単語か）への
# 連想配列（辞書型もしくはマップ型）を作成せよ．


sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#上のsentenceをwordごとに区切って並べる。
words = sentence.split(" ")

#上のwordsそれぞれから,と.を取り除く。
# for word in words:
#     word_stripped = word.strip(",.")

# made an empty dictionary to put key/value later.
dict_w1 = {}

# 先頭1文字の単語のリストを作って、それぞれの先頭1文字を上のdict_w1に入れる。
for i in [0,4,5,6,7,8,14,15,18]:
    #words[i]の先頭の1文字をw1にする。
    w1 = words[i][0]
    #[w1]は先頭の1文字。dict_w1はdictionary。i+1は何番目に出てくるか。
    #dict_w1[w1]は、例えばdict_w1[H]で、＝１となる（Hi）。
    dict_w1[w1] = i+1
# w2 = words[4][0]
# w3 = words[5][0]
# w4 = words[6][0]
# w5 = words[7][0]
# w6 = words[8][0]
# w7 = words[14][0]
# w8 = words[15][0]
# w9 = words[18][0]
print(dict_w1)
#{w1:1, w2:5, w3:6, w4:7, w5:8, w6:9, w7:15, w8:16, w9:19}

#2,3,4,10,11,12,13,14,17,18,20
dict_w2 = {}

for i in [1,2,3,9,10,11,11,12,13,16,17,19]:
    w2 = words[i][:2]
    dict_w2[w2] = i+1
print(dict_w2)
# w10 = words[1][1]
# w11= words[2][1]
# w12 = words[3][1]
# w13 = words[9][1]
# w14 = words[10][1]
# w15 = words[11][1]
# w16 = words[12][1]
# w17 = words[13][1]
# w18= words[16][1]
# w19= words[17][1]
# w20= words[19][1]
#
# {w10:2, w11:3, w12:4, w13:10, w14:11, w15:12, w16:13, w17:14, w18:17, w19:18, w20:20}

