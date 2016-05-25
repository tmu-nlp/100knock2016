from knock30 import get_sentences

for sentence in get_sentences():
    for morph in sentence:
        if morph['pos'] == '動詞':
            print(morph['surface'])
