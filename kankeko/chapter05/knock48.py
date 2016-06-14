from knock41 import get_sentences


for sentence in get_sentences():
    for chunk in sentence:
        if chunk.has_noun():
            path = chunk.get_path_to_root(sentence)
            if len(path) >= 2:
                print('->'.join(path))