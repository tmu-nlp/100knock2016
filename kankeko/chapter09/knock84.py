import pickle
import numpy as np
import math
from collections import defaultdict
from scipy.sparse import lil_matrix
from scipy import io

N = 68971901
tgt = ''
con = ''
ppmi = defaultdict(lambda : defaultdict(float))
word_id = defaultdict(lambda: len(word_id))
co_occ_freq = pickle.load(open('co_occurence_freq.txt', 'rb'))
t_freq = pickle.load(open('target_freq.txt', 'rb'))
c_freq = pickle.load(open('context_freq.txt', 'rb'))


[word_id[k]for k, v in c_freq.items()]

X = lil_matrix((len(t_freq),len(c_freq)))
for pair, freq in co_occ_freq.items():
    if freq > 2:
       tgt, con = pair
       ppmi[tgt][con] = max(0, math.log((N*freq)/(t_freq[tgt]*c_freq[con]), 2))
       if ppmi[tgt][con] > 0.0:
           X[word_id[tgt],word_id[con]] = ppmi[tgt][con]

io.savemat("X_matrix", {"PPMI":X})
