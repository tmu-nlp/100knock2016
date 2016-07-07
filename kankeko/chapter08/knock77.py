from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from knock72 import get_feature
from collections import Counter
from knock76 import predict_function


def get_score(pred, y_train, prob):
    total = 0
    correct = 0
    pos_correct = 0
    pos_total = 0
    answer_total = 0
    for p, a in zip(pred, y_train):
        total += 1
        if int(p) == a:
            correct += 1
            if a == 1:
                pos_correct += 1
        if int(p) == 1:
            pos_total += 1
        if a == 1:
            answer_total += 1
    accuracy = correct/total
    positive_accuracy = pos_correct/pos_total
    recall = pos_total/answer_total
    f_value = 2*accuracy*recall/(accuracy+recall)
    
    return accuracy, positive_accuracy, recall, f_value


if __name__ == '__main__':
    pred, y_train, prob = predict_function()
    print("正解率:{}\t適合率:{}\t再現率:{}\tF1スコア:{}".format(*get_score(pred, y_train, prob)))
