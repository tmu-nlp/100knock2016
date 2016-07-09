from sklearn.externals import joblib
from knock75 import get_feature
from sklearn.feature_extraction import DictVectorizer

if __name__ == "__main__":
    clf = joblib.load('knock75.model')
    vec = DictVectorizer()
    test_matrix = list()
    polarity_list = list()
    for line in open("sentiment.txt", "r"):
        phi, polarity = get_feature(line)
        test_matrix.append(phi)
        polarity_list.append(polarity)
    test = vec.fit_transform(test_matrix)
    f = open("knock76.txt", "w")
    count = 0
    for polarity, predict, predict_proba in zip(polarity_list, clf.predict(test), clf.predict_proba(test)):
        #print ('{}\t{}\t{}'.format(polarity, predict, predict_proba))
        f.write('{}\t{}\t{}'.format(polarity, predict, predict_proba))
        f.write('\n')
        if polarity == predict:
            count += 1
    print (count / len(polarity_list) * 100)
    f.close()