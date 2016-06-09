from knock72 import extract_feature
from knock73 import make_features_vectors, all_features, LR_model
from sklearn.linear_model import LogisticRegression

def predict_all(all_features, LR_model, sentence_list):
    features_list = []
    for sentence in sentence_list:
        features_list.append(extract_feature(sentence))
    label_list = LR_model.predict(make_features_vectors(all_features, features_list))
    prob_list = LR_model.predict_proba(make_features_vectors(all_features, features_list))
    return label_list, prob_list

result = []
ans_list = []
sentence_list = []
for line in open("sentiment.txt", "r"):
    ans_list.append(line[:2])
    sentence_list.append(line[3:])

label_list, prob_list = predict_all(all_features, LR_model, sentence_list)
for ans, label, prob in zip(ans_list, label_list, prob_list):
    max_prob = max(prob)
    if str(label) == "1":
        label = "+1"
    else:
        label = str(label)
    result.append([str(ans), label, str(max_prob)])

if __name__ == "__main__":
    for line in result:
        print("\t".join(line))
