from stemming.porter2 import stem
from collections import defaultdict
from knock71 import in_stoplist


def get_feature(sentence):
    feature = defaultdict(int)
    for tok in sentence.split():
        tok = tok.lower()
        if not in_stoplist(tok):
            feature[stem(tok)] += 1
    return dict(feature)


if __name__ == '__main__':
    s = 'This is a test sentence .'
    print(s)
    print(get_feature(s))
