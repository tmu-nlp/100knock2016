from knock30 import get_sentences
from collections import Counter


def get_all_words():
    for sentence in get_sentences():
        for m in sentence:
            yield m['surface']

vocab = Counter(get_all_words())

for tok, freq in vocab.most_common():
    print(freq, tok)
