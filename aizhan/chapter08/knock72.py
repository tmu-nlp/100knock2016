from stemming.porter2 import stem
from knock71 import if_stopword
import pprint


def get_feature():
    target = []
    feature = []
    for line in open("sentiment.txt"):
        y = line.split(" ")[0]
        x = [stem(w) for w in line.strip("\n").split(" ")[1:] if not if_stopword(w)]
        target.append(int(y))
        feature.append(x)
    return target, feature


if __name__ == '__main__':
    y_train, x_train = get_feature()
    for y, x in zip(y_train, x_train):
        print(y, x)
