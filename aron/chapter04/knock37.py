# knock37.py
# -*- coding: utf-8 -*-

import knock30
# import numpy as np
import matplotlib.pyplot as plt
import numpy as np

from collections import defaultdict
ktsList = knock30.getMorphology("neko.txt.mecab")

freqDic = defaultdict(lambda :0 )

for item in ktsList:
	freqDic[item["surface"]] += 1

X = []
X_= []#["a","a","a","a","a","a","a","a","a","a"]
for i in range(10):
	X.append(i)
Y = []
for key, value  in sorted(freqDic.items(), key=lambda x:-x[1], ):
	X_.append(key)
	Y.append(value)

plt.bar(X, Y[0:10])
plt.xticks(X, X_[0:10]) # 目盛りを数字からkeyに書き換える
plt.show()
