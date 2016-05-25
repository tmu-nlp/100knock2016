# -*- coding: utf-8 -*-

from knock30 import read_mecab
from collections import defaultdict
import matplotlib.pyplot as plt

sentences = read_mecab()
word_count = defaultdict(lambda: 0)

for line in sentences:
    for morpheme in line:
        word_count[morpheme["surface"]] += 1

X = []

for count in sorted(word_count.values(), reverse = True):
    X.append(count)

X_rank = range(1, len(X) + 1) 

plt.plot(X_rank, X)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("rank")
plt.ylabel("word_count")
plt.show()
