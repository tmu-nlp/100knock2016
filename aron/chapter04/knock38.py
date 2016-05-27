# knock38.py
# -*- coding: utf-8 -*-

import knock30
# import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


from collections import defaultdict
ktsList = knock30.getMorphology("neko.txt.mecab")

freqDic = defaultdict(lambda :0 )

for item in ktsList:
	freqDic[item["surface"]] += 1
X = sorted(freqDic.values())
# for x in X:
# 	print(x)
print (len(freqDic))
print (len(set(X)))
plt.hist(X, bins=len(set(X)), range=(1, 256))

plt.title("Histgram")
plt.xlabel("frequency")
plt.ylabel("num of word")
plt.show()