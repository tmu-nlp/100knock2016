from collections import defaultdict
from knock30 import neko_mecab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

words_mecab = defaultdict(lambda:0)
count_of_words = 0
i = 0
l = []
n = []
for line in neko_mecab():
    for word in line['surface']:
        if word not in words_mecab: count_of_words += 1
        words_mecab[word] += 1

for key, value in reversed(sorted(words_mecab.items(), key=lambda x:x[1])):
    i += 1
    if i > 10:
        break
    l.append(value)
    n.append(key)

plt.bar(range(10), l)
fp = FontProperties(fname='/Library/Fonts/ヒラギノ丸ゴ ProN W4.ttc')
plt.xticks([nx + 0.5 for nx in range(10)], n, fontproperties=fp)
plt.show()
