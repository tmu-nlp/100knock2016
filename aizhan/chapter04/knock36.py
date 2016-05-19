from collections import defaultdict
from knock30 import neko_mecab

words_mecab = defaultdict(lambda:0)
count_of_words = 0

for line in neko_mecab():
    for word in line['surface']:
        if word not in words_mecab: count_of_words += 1
        words_mecab[word] += 1

for key, value in reversed(sorted(words_mecab.items(), key=lambda x:x[1])):
    print(str(value) + '\t' + str(key))
