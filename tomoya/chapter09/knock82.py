from collections import defaultdict
import random

word_context = defaultdict(lambda: '')
for line in open('./enwiki-corpus2.txt', 'r'):
  words = line.split()
  for i in range(1, len(words) - 1):
    width = min(i, len(words) - i - 1)
    randmax = width if width < 5 else 5
    d = random.randint(1, randmax)
    for j in range(i - d, i + d + 1):
      if (i != j):
        print('{}\t{}'.format(words[i], words[j]))
