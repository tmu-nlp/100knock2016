from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib

LR_model = joblib.load('model.pkl')
DictoVec = joblib.load('vec.pkl')

weight = {}
for feature, value in zip(DictoVec.get_feature_names(), *LR_model.coef_):
    weight[feature] = value

print("High_Top10")
for key, value in sorted(weight.items(), key = lambda x : x[1], reverse = True)[:10]:
    print("{}:{}".format(key, value))
print("Low_Top10")
for key, value in sorted(weight.items(), key = lambda x : x[1])[:10]:
    print("{}:{}".format(key, value))
