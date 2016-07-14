import numpy as np

def spearman(X, Y):
    print(X)
    print(Y)
    return 1.0 - (6 * sum(X - Y) ** 2) / float(len(X) ** 3 - len(X))

human_list = []
v85_list = []
v90_list = []

for i, (line1, line2) in enumerate(zip(open("result_94_v85.txt", "r"), open("result_94_v90.txt", "r"))):
    human_list.append((i, float(line1.strip().split()[2])))
    v85_list.append((i, float(line1.strip().split()[3])))
    v90_list.append((i, float(line2.strip().split()[3])))

result_v85 = spearman(np.array([v1 for v1, v2 in sorted(human_list, key = lambda x: x[1])]), np.array([v1 for v1, v2 in sorted(v85_list, key = lambda x: x[1])]))
result_v90 = spearman(np.array([v1 for v1, v2 in sorted(human_list, key = lambda x: x[1])]), np.array([v1 for v1, v2 in sorted(v90_list, key = lambda x: x[1])]))

print("v85_spearman：{}".format(result_v85))
print("v90_spearman：{}".format(result_v90))
