from knock30 import get_sentences
from collections import Counter
import matplotlib.pyplot as plt

vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

names, freqs = zip(*vocab.most_common())

plt.hist(freqs, bins=len(set(freqs)))
plt.show()
