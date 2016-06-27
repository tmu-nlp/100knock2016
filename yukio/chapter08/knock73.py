from knock72 import label_list, features_list
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib

LR_model = LogisticRegression()
DictoVec = DictVectorizer()
LR_model.fit(DictoVec.fit_transform(features_list), label_list)
joblib.dump(LR_model, 'model.pkl')
joblib.dump(DictoVec, 'vec.pkl')
