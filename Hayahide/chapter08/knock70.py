# -*- coding: utf-8 -*-
import random

sentiment = []

for count, line in enumerate(open('rt-polaritydata/rt-polaritydata/rt-polarity.pos', 'rb')):
    sentiment.append('+1 ' + line.decode('latin-1'))
print('+1 : ' + str(count))

for count, line in enumerate(open('rt-polaritydata/rt-polaritydata/rt-polarity.neg', 'rb')):
    sentiment.append('-1 ' + line.decode('latin-1'))
print('-1 : ' + str(count))

random.shuffle(sentiment)

w_file = open('sentiment.txt', 'w')
for line in sentiment:
    w_file.write(line)
w_file.close()
