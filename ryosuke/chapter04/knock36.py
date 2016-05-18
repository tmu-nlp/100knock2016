from knock30 import get_sentences
from collections import Counter


vocab = Counter()
for sentence in get_sentences():
    vocab += Counter(m['surface'] for m in sentence)

for tok, freq in vocab.most_common():
    print(freq, tok)
