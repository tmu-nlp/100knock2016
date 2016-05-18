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


plt.hist(X, bins = 30, range = (1, 30))
plt.xlabel("word_count")
plt.ylabel("the number of type")
plt.show()
