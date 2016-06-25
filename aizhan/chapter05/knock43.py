from knock41 import get_sentences

for sentence in get_sentences():
    for chunk in sentence:
        if chunk.dst != -1:
            tgt_chunk = sentence[chunk.dst]
            if not chunk.has_noun() or not tgt_chunk.has_verb():
                continue
            src = chunk.join_surface_wo_symbol()
            dst = tgt_chunk.join_surface_wo_symbol()
            if src == '' or dst == '':
                continue
            print('{}\t{}'.format(src, dst))