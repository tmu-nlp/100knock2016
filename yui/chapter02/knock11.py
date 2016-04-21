# -*- coding: utf-8 -*-


# タブをスペースに置換
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，
# trコマンド，もしくはexpandコマンドを用いよ．

file_tab_to_space = open("hightemp.txt")

# ファイルを読み込んでstringにする。
tab_file_content = file_tab_to_space.read()

# ストリング内のタブをスペースに置き換える。
tab_to_space = tab_file_content.replace("\t", " ")

print tab_to_space
