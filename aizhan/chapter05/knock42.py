from knock41 import get_cabocha

for sentence in get_cabocha():
    for chunk in sentence:
        if chunk.dst != -1:
            src = chunk.join_surface_wo_symbol()
            dst = sentence[chunk.dst].join_surface_wo_symbol()
            if src == '' or dst == '':
                continue
            print('{}\t{}'.format(src, dst))