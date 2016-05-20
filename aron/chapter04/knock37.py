# knock37.py
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

X = [i + 1 for i in range(10)]
# print (X)
X_label= []#["a","a","a","a","a","a","a","a","a","a"]

Y = []
count = 0
for key, value  in sorted(freqDic.items(), key=lambda x:-x[1]):
	if(key == "EOS"):
		continue
	X_label.append(key)
	#print ("%s, %d" % (key, value))
	Y.append(value)
	count += 1
	if count >=10:
		break;
fp = FontProperties(fname='/Library/Fonts/OsakaMono.ttf')
# print (X, Y)
plt.bar(X, Y, align = 'center')
plt.xticks(X, X_label, fontproperties=fp)
plt.show()
