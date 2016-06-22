from knock73 import feature_vector, feature_making
from sklearn.externals import joblib
import sys

feature_list = list()
for line in open('knock72_result.txt'):
    word, value = line.strip('\n').split('\t')
    feature_list.append(word)

LR = joblib.load('LR.pkl')

query = sys.argv[1:]
vector = []
query = feature_making(query)
vector.append(feature_vector(feature_list, query))

print(LR.predict(vector))
print(LR.predict_proba(vector))

