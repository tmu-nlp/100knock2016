# -*- coding: utf-8 -*-
from knock50 import get_end_of_sentence


def get_word():
    for sentence in get_end_of_sentence():
        line = sentence.split(' ')
        for word in line:
            yield word


if __name__ == '__main__':
    for word in get_word():
        print(word)
