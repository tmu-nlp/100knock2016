from knock72 import getFeatureList
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib


def getFeatureVector(feature_list, all_feature):
    feature_vector = list()
    for feature in sorted(all_feature):
        if feature in feature_list:
            feature_vector.append(1)
        else:
            feature_vector.append(0)
    return feature_vector


def getFeatureMatrix(input_file):
    all_feature, features = getFeatureList(input_file)
    feature_matrix = list()
    label_vector = list()
    for label, feature_vector in features:
        feature_matrix.append(getFeatureVector(feature_vector, all_feature))
        label_vector.append(label)
    return feature_matrix, label_vector

if __name__ == '__main__':
    feature_matrix, label_vector = getFeatureMatrix('sentiment.txt')
    lr = LogisticRegression()
    lr.fit(feature_matrix, label_vector)
    joblib.dump(lr, 'lr.pkl')
