# -*- coding: utf-8 -*-

# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．


from knock30 import get_sentences

list_n = []

for line in get_sentences():
    for morph in line:
        if morph['pos'] == '名詞':
            list_n.append(morph['surface'])
        else:
            if len(list_n) > 1:
                print(list_n)
            list_n = []
