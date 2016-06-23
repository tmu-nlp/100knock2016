from knock41 import get_sentences

for sentence in get_sentences():
    for chunk in sentence:
        if chunk.dst != -1:
            src = chunk.join_surface_wo_symbol()
            dst = sentence[chunk.dst].join_surface_wo_symbol()
            if src == '' or dst == '':
                continue
            print('{}\t{}'.format(src, dst))