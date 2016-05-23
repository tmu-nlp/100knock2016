from knock41 import get_sentences

for sentence in get_sentences():
    for chunk in sentence:
        if chunk.dst != -1:
            print('{}\t{}'.format(chunk.join_surface(), sentence[chunk.dst].join_surface()))
