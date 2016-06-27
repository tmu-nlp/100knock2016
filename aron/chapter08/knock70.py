# coding = utf-8
import sys, random

sent_list = list()

with open("./data/rt-polaritydata/rt-polarity.pos") as pos_file:
	for line in pos_file:
		sent_list.append("+1 : %s" % (line.strip()))

with open("./data/rt-polaritydata/rt-polarity.neg") as neg_file:
	for line in neg_file:
		sent_list.append("-1 : %s" % (line.strip()))

random.shuffle(sent_list)

with open("sentiment.txt", "w") as file:
	for line in sent_list:
		file.write(line + "\r\n")