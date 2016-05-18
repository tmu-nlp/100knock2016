from knock30 import get_sentences
from collections import Counter
import matplotlib.pyplot as plt

vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

names, freqs = zip(*vocab.most_common())

plt.bar(range(1, len(names)+1), freqs)
plt.xscale('log')
plt.yscale('log')
plt.show()
