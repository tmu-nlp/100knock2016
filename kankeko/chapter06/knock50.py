# -*- coding: utf-8 -*-
import re


def get_end_of_sentence():
    ptn = re.compile("(?P<end>\.|;|:|\?|!) (?P<start>[A-Z])")
    for sentence in open("nlp.txt"):
        sentence = sentence.rstrip('\n')
        if sentence == '':
            continue
        yield ptn.sub(lambda m: m.group('end') + '\n' + m.group('start'), sentence)


if __name__ == '__main__':
    for line in get_end_of_sentence():
        print(line)
