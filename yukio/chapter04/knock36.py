from knock30 import read_mecab
from collections import defaultdict

sentences = read_mecab()
word_count = defaultdict(lambda: 0)

for line in sentences:
    for morpheme in line:
        word_count[morpheme["surface"]] += 1

for word, count in sorted(word_count.items(), key = lambda x: x[1], reverse = True):
    print("{} {}".format(count, word))
