import random


neg_file = 'rt-polaritydata/rt-polarity.neg'
pos_file = 'rt-polaritydata/rt-polarity.pos'

l = list()
pos_count = 0
neg_count = 0
for line in open(pos_file, encoding='latin-1'):
    l.append('+1 {}'.format(line.rstrip('\n')))
    pos_count += 1
for line in open(neg_file, encoding='latin-1'):
    l.append('-1 {}'.format(line.rstrip('\n')))
    neg_count += 1

random.shuffle(l)

with open('sentiment.txt', 'w') as fw:
    for line in l:
        print(line, file=fw)
print('pos:{}, neg:{}'.format(pos_count, neg_count))

