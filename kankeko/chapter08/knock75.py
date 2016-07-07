from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from knock72 import get_feature
from collections import Counter


def weight_function():
    x_list = []
    predict_doc = joblib.load('logreg.pkl')
    feature_doc = joblib.load('word_vec.pkl')
    for i,weight in enumerate(sorted(zip(*predict_doc.coef_,feature_doc.get_feature_names()),reverse=True)):
        print(weight)
        if i == 9:
            break
    print("\n")
    for i,weight in enumerate(sorted(zip(*predict_doc.coef_,feature_doc.get_feature_names()))):
        print(weight)
        if i == 9:
            break

if __name__ == '__main__':
    weight_function()
