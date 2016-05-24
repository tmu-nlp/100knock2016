# -*- coding: utf-8 -*-

# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

from knock30 import get_sentences
from collections import Counter
import matplotlib.pyplot as plt # ImportError: No module named 'matplotlib'
from matplotlib.font_manager import FontProperties

vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

names, freqs = zip(*vocab.most_common()[:10])
x = range(len(names))


plt.bar(x, freqs)
fp = FontProperties(fname='/Library/Fonts/ヒラギノ角ゴ Pro W3.otf')

# 位置の調整
plt.xticks([nx + 0.5 for nx in x], names, fontproperties=fpd)
plt.show()
