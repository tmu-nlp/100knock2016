import numpy as np
from pandas import Series
from scipy.stats import spearmanr

def spearman(X, Y):
    return 1.0 - (6 * sum((X - Y) ** 2) / (len(X) ** 3 - len(X)))

human85_list = []
human90_list = []
v85_list = []
v90_list = []

for line1, line2 in zip(open("result_94_v85.txt", "r"), open("result_94_v90.txt", "r")):
    human85_list.append(float(line1.strip().split("\t")[2]))
    human90_list.append(float(line2.strip().split("\t")[2]))
    v85_list.append(float(line1.strip().split("\t")[3]))
    v90_list.append(float(line2.strip().split("\t")[3]))

result_v85 = spearman(np.array(Series(human85_list).rank(method = "first")), np.array(Series(v85_list).rank(method = "first")))
result_v90 = spearman(np.array(Series(human90_list).rank(method = "first")), np.array(Series(v90_list).rank(method = "first")))

print("v85_spearman：{}".format(result_v85))
print("v90_spearman：{}".format(result_v90))
