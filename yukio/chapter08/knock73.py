from knock72 import label_list, features_list
from sklearn.linear_model import LogisticRegression

all_features = []
for features in features_list:
    for feature in features:
        if feature not in all_features:
            all_features.append(feature)
all_features.sort()

def make_features_vectors(all_features, features_list):
    features_vectors = []
    for features in features_list:
        temp = []
        for one_feature in all_features:
            if one_feature in features:
                temp.append(1)
            else:
                temp.append(0)
        features_vectors.append(temp)
    return features_vectors

LR_model = LogisticRegression()
LR_model.fit(make_features_vectors(all_features, features_list), label_list)
