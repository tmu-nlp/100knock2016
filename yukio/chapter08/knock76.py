from knock72 import extract_feature
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib

LR_model = joblib.load('model.pkl')
DictoVec = joblib.load('vec.pkl')

def predict_all(LR_model, sentence_list):
    features_list = []
    for sentence in sentence_list:
        features_list.append(extract_feature(sentence))
    label_list = LR_model.predict([[features[feature] for feature in DictoVec.get_feature_names()] for features in features_list])
    prob_list = LR_model.predict_proba([[features[feature] for feature in DictoVec.get_feature_names()] for features in features_list])
    return label_list, prob_list

result = []
ans_list = []
sentence_list = []
for line in open("sentiment.txt", "r"):
    ans_list.append(int(line[:2]))
    sentence_list.append(line[3:])

label_list, prob_list = predict_all(LR_model, sentence_list)
for ans, label, prob in zip(ans_list, label_list, prob_list):
    max_prob = max(prob)
    result.append([str(ans), str(label), str(max_prob)])

if __name__ == "__main__":
    for line in result:
        print("\t".join(line))
