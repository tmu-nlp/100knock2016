# -*- coding: utf-8 -*-

from knock41 import get_sentences


for sentence in get_sentences():
    for chunk in sentence:
        if chunk.has_noun():    #knock41にある。名詞の文節
            path = chunk.get_path_to_root(sentence)
            if len(path) >= 2:
                print('->'.join(path))
