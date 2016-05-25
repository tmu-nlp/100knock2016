from knock30 import get_sentences

for sentence in get_sentences():
    for morpoh in sentence:
        if morpoh['pos'] == '動詞':
            print(morpoh['base'])
