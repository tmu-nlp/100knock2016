# coding utf-8
import sys, nltk, knock71
from  collections import defaultdict

stemming = nltk.stem.PorterStemmer()
features_dict = defaultdict(lambda: 0)

with open("sentiment.txt") as file:
	for line in file:
		word_list = nltk.word_tokenize(line.strip())
		polarity = int(word_list.pop(0))
		for word in word_list:
			stem = stemming.stem(word)
			if not knock71.is_stop_word(stem) :
				features_dict[stem] += 1

for word, value in sorted(features_dict.items(), key=lambda x:-x[1]):
	print (word, value)

