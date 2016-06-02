# knock36.py
import knock30
from collections import defaultdict
ktsList = knock30.getMorphology("neko.txt.mecab")

freqDic = defaultdict(lambda :0 )

for item in ktsList:
	try:
		freqDic[item["surface"]] += 1
	except :
		print(item)

# sortedDic = 
for key, value  in sorted(freqDic.items(), key=lambda x:-x[1]):
	print (key, value)
