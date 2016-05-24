# -*- coding: utf-8 -*-

#形態素解析結果の読み込み
#形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
#ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとする
#マッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
#第4章の残りの問題では，ここで作ったプログラムを活用せよ．




def get_sentences():
    sentence = list()
    for line in open('neko.txt.mecab'):
        if line.startswith('EOS'):
            if len(sentence) != 0:
                yield sentence
                sentence = list()
        else:
            surface = line.split('\t')[0]
            base = line.split('\t')[1].split(',')[6]
            pos = line.split('\t')[1].split(',')[0]
            pos1 = line.split('\t')[1].split(',')[1]
            morph = dict()
            morph['surface'] = surface if surface != '*' else ''
            morph['base'] = base if base != '*' else ''
            morph['pos'] = pos if pos != '*' else ''
            morph['pos1'] = pos1 if pos1 != '*' else ''
            sentence.append(morph)


if __name__ == '__main__':
    for sentence in get_sentences():
        for morph in sentence:
            print(morph)
        print('EOS')
