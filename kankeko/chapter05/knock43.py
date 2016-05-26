from knock41 import get_cabocha

for sentence in get_cabocha():
    for chunk in sentence:
        if chunk.dst != -1:
            tgt_chunk = sentence[chunk.dst]
            for m in chunk.morphs:
                if m.pos != "名詞" or m.pos != "動詞":
                    continue
            src = "".join(m.surface for m in chunk.morphs)
            dst = "".join(m.surface for m in sentence[chunk.dst].getMorphs() )
            if src == '' or dst == '':
                continue
            print('{}\t{}'.format(src, dst))
