from knock30 import get_sentences

for sentence in get_sentences():
    for morph in sentence:
        if morph['pos'] == '名詞' and morph['pos1'] == 'サ変接続':
            print(morph)
