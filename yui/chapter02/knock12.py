# -*- coding: utf-8 -*-


# 1列目をcol1.txtに，2列目をcol2.txtに保存
# 各行の1列目だけを抜き出したものをcol1.txtに，
# 2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

# hightemp.txtをoriginal_fileとして開く
original_file = open("hightemp.txt")


# type of original_file.readlenes() is a list of strings
lines = original_file.readlines()

column1 = []

for words in lines:
    line_string = words.split("\t")
    first_column = line_string[0]
    second_column = line_string[1]

    #"col1.txt"ファイルを書き込みモードで開いて書いて閉じる。
    file_column1 = open("col1.txt", "a+")
    file_column1.write(first_column+"\n")
    file_column1.close()

    #"col2.txt"ファイルを書き込みモードで開いて書いて閉じる。
    file_column2 = open("col2.txt", "a+")
    file_column2.write(second_column+"\n")
    file_column2.close()

# for words in lines:
#     line_string = words.split("\t")
#     second_column = line_string[1]
#
#
#     file_column2 = open("col2.txt", "a+")
#     file_column2.write(second_column+"\n")
#     file_column2.close()
