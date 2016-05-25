# -*- coding: utf-8 -*-

from knock30 import read_mecab
from collections import defaultdict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

sentences = read_mecab()
word_count = defaultdict(lambda: 0)

for line in sentences:
    for morpheme in line:
        word_count[morpheme["surface"]] += 1

X = range(1,11)
X_list = []
Y = []
i = 0

for word, count in sorted(word_count.items(), key = lambda x: x[1], reverse = True):
    X_list.append(word)
    Y.append(count)
    i += 1
    if i >= 10:
        break

plt.bar(X, Y, align = "center")
plt.xticks(X, X_list, fontproperties = FontProperties(fname = "ipaexg.ttf"))
plt.ylabel("word_count")
plt.show()
