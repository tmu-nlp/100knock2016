from knock73 import feature_vector, feature_making
from sklearn.externals import joblib

feature_list = list()
for word in open('knock72_result.txt'):
    word = word.strip('\n').split('\t')[0]
    feature_list.append(word)

LR = joblib.load('LR.pkl')

weight_dict = dict()
for word, weight in zip(feature_list, LR.coef_[0]):
    weight_dict[word] = weight

print('best 10')
for key, value in sorted(weight_dict.items(), key = lambda x:x[1], reverse = True)[:10]:
    print(key, value)

print('\nworst 10')
for key, value in sorted(weight_dict.items(), key = lambda x:x[1])[:10]:
    print(key, value)
