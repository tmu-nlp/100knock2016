from knock72 import extract_feature
from knock73 import make_features_vectors, all_features, LR_model
from sklearn.linear_model import LogisticRegression
import sys

def predict_one(all_features, LR_model, sentence):
    label = str(*LR_model.predict(make_features_vectors(all_features, [extract_feature(sentence)])))
    if label == "1":
        label = "+1"
    prob = LR_model.predict_proba(make_features_vectors(all_features, [extract_feature(sentence)]))
    return label, prob

if __name__ == "__main__":
    label, prob = predict_one(all_features, LR_model, sys.argv[1])
    print("{}\nlabel:{}\nprob:{}".format(sys.argv[1], label, max(*prob)))
