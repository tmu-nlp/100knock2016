# -*- coding: utf-8 -*-

# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ


from knock30 import get_sentences
from collections import Counter


vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

for tok, freq in vocab.most_common():
    print(freq, tok)
