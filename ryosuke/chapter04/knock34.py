from knock30 import get_sentences


for sentence in get_sentences():
    combination3 = zip(*[sentence[i:] for i in range(3)])
    a_no_bs = [comb for comb in combination3 if comb[0]['pos'] == '名詞' and comb[1]['surface'] == 'の' and comb[2]['pos'] == '名詞']
    for anob in a_no_bs:
        print(' '.join(m['surface'] for m in anob))
