# -*- coding: utf-8 -*-

#単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

from knock30 import get_sentences
from collections import Counter
import matplotlib.pyplot as plt

vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

names, freqs = zip(*vocab.most_common())

plt.hist(freqs, bins=len(set(freqs))) # binsは縦棒の数
plt.show()
