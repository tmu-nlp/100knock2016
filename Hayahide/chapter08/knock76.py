from sklearn.externals import joblib
from knock74 import fit_feature

feature_dict = dict()
for line in open('knock72_result.txt'):
    word, value = line.strip('\n').split('\t')
    feature_dict[word] = int(value)

LR = joblib.load('LR.pkl')

for line in open('sentiment.txt'):
    query = line.strip('\n').split()
    answer = query.pop(0)
    feature = fit_feature(query, feature_dict)
    polarity = '+1' if LR.predict(feature)[0] == 1 else '-1'
    probability = LR.predict_proba(feature)[0]
    print('{}\t{}\t{}'.format(answer, polarity, max(probability[0], probability[1])))

