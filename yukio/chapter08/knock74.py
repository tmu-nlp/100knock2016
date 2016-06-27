from knock72 import extract_feature
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
import sys

LR_model = joblib.load('model.pkl')
DictoVec = joblib.load('vec.pkl') 

def predict_one(LR_model, sentence):
    label = str(*LR_model.predict([[extract_feature(sentence)[feature] for feature in DictoVec.get_feature_names()]]))
    if label == "1":
        label = "+1"
    prob = LR_model.predict_proba([[extract_feature(sentence)[feature] for feature in DictoVec.get_feature_names()]])
    return label, prob

if __name__ == "__main__":
    label, prob = predict_one(LR_model, sys.argv[1])
    print("{}\nlabel:{}\nprob:{}".format(sys.argv[1], label, max(*prob)))
