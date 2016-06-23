# -*- coding: utf-8 -
#python 3系じゃ動かんぞい なぜ？
import random
concatenate = list()
for line in open("rt-polarity.pos", "r", encoding="latin-1"):
    concatenate.append("+1 " + line)
for line in open("rt-polarity.neg", "r", encoding='latin-1'):
    concatenate.append("-1 " + line)

random.shuffle(concatenate)
f = open("sentiment.txt", "w")
for line in concatenate:
    f.write(line)
f.close()
