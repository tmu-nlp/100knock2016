from collections import defaultdict
from knock73 import feature_vector, feature_making
from knock78 import prediction, cv_prediction
import matplotlib.pyplot as plt

feature_dict = defaultdict(int)
for line in open('knock72_result.txt'):
    word, value = line.strip('\n').split('\t')
    feature_dict[word] = int(value)

polarity = list()
feature = list()
for line in open('sentiment.txt'):
    sentence = line.strip('\n').split()
    polarity.append(int(sentence.pop(0)))
    feature.append(feature_vector(feature_making(sentence)))

folds = 5
thd = list()
[thd.append(i / 10) for i in range(1, 10)]

precision = list()
recall = list()
for threshold in thd:
    accuracy, prec, rec, f1 = cv_prediction(feature_dict, feature, polarity, threshold, folds)
    precision.append(prec / folds)
    recall.append(rec / folds)
    print('threshold({}) experimented.'.format(threshold))

plt.plot(precision, recall)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.show()
