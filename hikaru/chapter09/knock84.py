import math
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse import lil_matrix, csr_matrix
from scipy import sparse, io
import numpy as np
import pickle

tc_dict = defaultdict(int)
t_dict = defaultdict(int)
c_dict = defaultdict(int)

for line in open('f_tc.txt'):
    tc, value = line.split(' ')
    tc_dict[tc] = int(value)
for line in open('f_t.txt'):
    t, value = line.split(' ')
    t_dict[t] = int(value)
for line in open('f_c.txt'):
    c, value = line.split(' ')
    c_dict[c] = int(value)

def cal(t, value):
    if value >= 10:
        res = (N * value) / (t_dict[t] * c_dict[t])
        X_tc[key] = max(math.log(res), 0)
    else:
        X_tc[key] = 0
    return X_tc

N = 17611099
'''
X_tc = defaultdict(float)
feature_matrix = list()
tmp = 'NULL1'
for key, value in sorted(tc_dict.items()):
    t, c = key.split('\t')
    if tmp == t:
        X_tc.update(cal(t, value))
    elif tmp != t and tmp != 'NULL1':
        tmp = t
        feature_matrix.append(X_tc)
        X_tc = defaultdict(float)
        X_tc.update(cal(t, value))
    elif tmp != t and tmp == 'NULL1':
        tmp = t
        X_tc.update(cal(t, value))
vec = DictVectorizer()
X = vec.fit_transform(feature_matrix)
'''
'''
for key, value in X_tc.items():
    if value != 0:
        print ('{}\t{}'.format(key, value))
'''
t_index = defaultdict(int)
c_index = defaultdict(int)
for i, (t, _) in enumerate(sorted(t_dict.items(), key=lambda x: -x[1])):
    t_index[t] = i
for i, (t, _) in enumerate(sorted(c_dict.items(), key=lambda x: -x[1])):
    c_index[t] = i
with open('t_index.pickle', mode='wb') as f:
    pickle.dump(t_index, f)
#print (t_index['United_States']) #7645
#exit()
#print (t_index['U.S']) #182
#exit()
print (t_index['England'])
print (t_index['Raw'])

#X = lil_matrix((178764, 200910))  cat f_t.txt | wc -l
X = lil_matrix((178764, 200910))
X1 = np.zeros((178764, 200910))
for key, value in sorted(tc_dict.items(), key=lambda x: -x[1]):
    t, c = key.split('\t')
    if value >= 10:
        res = (N * value) / (t_dict[t] * c_dict[t])
        X[t_index[t], c_index[c]] = max(math.log(res), 0)
X = X[0:30000, 0:30000]

X = X.tocsr() #lil_matrixをcsr_matrixに変換する
print (X)
io.savemat("matrix_X", {"X":X})
print (X.todense())
print (type(X.todense()))
