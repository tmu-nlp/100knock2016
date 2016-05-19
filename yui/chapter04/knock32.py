# -*- coding: utf-8 -*-

#動詞の原形をすべて抽出せよ．

from knock30 import get_sentences

for sentence in get_sentences():
    for morph in sentence:
        if morph['pos'] == '動詞':
            print(morph['base'])
