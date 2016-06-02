# knock39.py
# coding = utf-8

import knock30
# import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


from collections import defaultdict
ktsList = knock30.getMorphology("neko.txt.mecab")

freqDic = defaultdict(lambda :0 )

for item in ktsList:
	freqDic[item["surface"]] += 1

# Rank = [i  for i in enumerate()]
# sorted(freqDic, key= lambda: x)
freqList = list(reversed(sorted(freqDic.values())))
print (type(freqList))
# Rank = [i for i in range(1, len(freqList) + 1)]

plt.bar(range(1, len(freqList) + 1), freqList, align = 'center')
# plt.xticks(X, X_label, fontproperties=fp)
# plt.xscale('log')
# plt.yscale('log')
plt.show()