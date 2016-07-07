from knock72 import label_list, features_list
from knock77 import calc_score
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import KFold
import matplotlib.pyplot as plt

pres = []
recs = []

for thd in [x / 10 for x in range(0, 11)]:
    LR_model = LogisticRegression()
    DictoVec = DictVectorizer()
    kf = KFold(len(label_list), n_folds = 5)

    pre_list = []
    rec_list = []
    i = 0

    for train_ids, test_ids in kf:
        i += 1
        LR_model.fit(DictoVec.fit_transform([features_list[train_id] for train_id in train_ids]), [label_list[train_id] for train_id in train_ids])
        predict_list = LR_model.predict_proba([[features_list[test_id][feature] for feature in DictoVec.get_feature_names()] for test_id in test_ids])
        answer_list = [label_list[test_id] for test_id in test_ids]

        result = []
        for answer, predict in zip(answer_list, predict_list):
            if predict[1] >= thd:
                label = "1"
            else:
                label = "-1"
            result.append([str(answer), label])
        accuracy, precision, recall, f1score = calc_score(result)
    
        pre_list.append(precision)
        rec_list.append(recall)

    pres.append(100 * sum(pre_list) / len(pre_list))
    recs.append(100 * sum(rec_list) / len(rec_list))

plt.plot(recs, pres)
plt.xlabel("recall[%]")
plt.ylabel("precision[%]")
plt.xlim([0, 100])
plt.ylim([0, 100])
plt.show()
