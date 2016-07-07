from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

y_true = list()
y_pred = list()
for line in open("knock76.txt", "r"):
    true, predict, predict_proba = line.split("\t")
    y_true.append(true)
    y_pred.append(predict)
_target_names = ['-1', '1']
print (classification_report(y_true, y_pred, target_names=_target_names))
print (accuracy_score(y_true, y_pred))
