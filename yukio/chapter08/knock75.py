from knock73 import LR_model, all_features
from sklearn.linear_model import LogisticRegression

weight = {}
for feature, value in zip(all_features, *LR_model.coef_):
    weight[feature] = value

print("High_Top10")
for key, value in sorted(weight.items(), key = lambda x : x[1], reverse = True)[:10]:
    print("{}:{}".format(key, value))
print("Low_Top10")
for key, value in sorted(weight.items(), key = lambda x : x[1])[:10]:
    print("{}:{}".format(key, value))
