# -*- coding: utf-8 -*-


#  col1.txtとcol2.txtをマージ
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
# タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを
# 用いよ．


file_column1 = open("col1.txt", "r")
file_column2 = open("col2.txt", "r")

file_col1_2 = open("col1_2.txt", "w")
file_col1_2.write("\n".join([col1.strip("\n") + "\t" + col2.strip("\n") for col1, col2 in zip(file_column1, file_column2)]))

file_column1.close()
file_column2.close()
file_col1_2.close()

#paste -d "¥t" col1.txt col2.txt
