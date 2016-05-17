from knock30 import get_sentences
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

names, freqs = zip(*vocab.most_common()[:10])
x = range(len(names))

plt.bar(x, freqs)
fp = FontProperties(fname='/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc')
plt.xticks([nx + 0.5 for nx in x], names, fontproperties=fp)
plt.show()
