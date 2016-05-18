from knock30 import get_sentences


for sentence in get_sentences():
    indexes = [i for i, m in enumerate(sentence) if m['pos'] == '名詞']
    if len(indexes) == 0:
        continue
    start_i = indexes[0]
    nps = list()
    for e, s in zip(indexes, indexes[1:]):
        if s - e == 1:
            continue
        nps.append(' '.join(sentence[i]['surface'] for i in range(start_i, e + 1)))
        start_i = s
    e = indexes[-1]
    nps.append(' '.join(sentence[i]['surface'] for i in range(start_i, e + 1)))
    print('|'.join(nps))
