# -*-coding:utf-8-*-

# 40. 係り受け解析結果の読み込み（形態素）
# 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):  #組み込み関数str()とprint文によって呼び出される。戻り値は文字列オブジェクトでなければならん。
        return "surface:{}, base:{}, pos:{}, pos1:{}".format(   #ここで切れてるのはなんかルールがある？##だいたい左のかっこできる。
        self.surface, self.base, self.pos, self.pos1)

def get_sentences():
    sentence = list()
    for line in open('neko.txt.cabocha'):
        if line.startswith('EOS'):
            if len(sentence) != 0:
                yield sentence
                sentence = list()   #直前のsentenceとは違う。次の処理のために初期化している。
            continue    #これはなぜここにいるの？何も書かないのとどう違うのか？    #ここから下は実行しないで次のやつにいく。う
        if line.startswith('*'):
            continue
        surface = line.split('\t')[0]
        pos = line.split('\t')[1].split(',')[0]
        pos1 = line.split('\t')[1].split(',')[1]
        base = line.split('\t')[1].split(',')[6]
        morph = Morph(surface, base, pos, pos1)
        sentence.append(morph)

#3文目の形態素列を表示
for i, sentence in enumerate(get_sentences()):  #enumerateはループする時にインデックス付きで要素を返す。
    if i == 2:  #ここでは３文目が欲しいから、「i (index)が２だったら」という条件をつけている
        for morph in sentence:  #?
            print(morph)
        break
