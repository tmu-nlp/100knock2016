# coding = utf-8
import sys
from knock72 import features_dict
from sklearn.linear_model import LogisticRegression
# features_dict = knock72.

line_vector_list = list()
polarity_list 	= list()
with open("sentiment.txt", "r") as file:
	
	for line in file:
		word_list = nltk.word_tokenize(line.strip())
		polarity = int(word_list.pop(0))
		# polarity = int(word_list)
		polarity_list.append(polarity)
		line_phi_list = list()
		for word in word_list:
			stem = stemming.stem(word)
			if not knock71.is_stop_word(stem) :
				if stem in features_dict:
					line_phi_list.append(stem)
		one_line_vector =list()
		for phi, value in features_dict:
			if phi in line_phi_list:
				one_line_vector.append(value)
			else:
				one_line_vector.append(0)

		line_vector_list.append(one_line_vector)

lr= LogisticRegression(C = 1000)
lr.fit(line_vector_list, polarity_list)