from knock72 import label_list, features_list
from knock77 import calc_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import KFold

LR_model = LogisticRegression()
DictoVec = DictVectorizer()
kf = KFold(len(label_list), n_folds = 5)

acc_list = []
pre_list = []
rec_list = []
f1s_list = []
i = 0

for train_ids, test_ids in kf:
    i += 1
    LR_model.fit(DictoVec.fit_transform([features_list[train_id] for train_id in train_ids]), [label_list[train_id] for train_id in train_ids])
    predict_list = LR_model.predict([[features_list[test_id][feature] for feature in DictoVec.get_feature_names()] for test_id in test_ids])
    answer_list = [label_list[test_id] for test_id in test_ids]

    result = []
    for answer, predict in zip(answer_list, predict_list):
        result.append([str(answer), str(predict)])
    accuracy, precision, recall, f1score = calc_score(result)
    
    acc_list.append(accuracy)
    pre_list.append(precision)
    rec_list.append(recall)
    f1s_list.append(f1score)

    print("{}".format(i))
    print("Accuracy:{}%".format(100 * accuracy))
    print("Precision:{}%".format(100 * precision))
    print("Recall:{}%".format(100 * recall))
    print("F1-Score:{}%".format(100 * f1score))
    print()

print("Average")
print("Accuracy:{}%".format(100 * sum(acc_list)/ len(acc_list)))
print("Precision:{}%".format(100 * sum(pre_list)/ len(pre_list)))
print("Recall:{}%".format(100 * sum(rec_list)/ len(rec_list)))
print("F1-Score:{}%".format(100 * sum(f1s_list)/ len(f1s_list)))
