from collections import Counter
import pickle

target = []
context = []
co_occurence = []

for line in open('context.txt'):
    line = line.strip().split('\t')
    t = line[0]
    c = line[1:]
    co_occurence += ((t, y) for y in c)
    target.append(t)
    context += c

fco = open('co_occurence_freq.txt', 'wb')
ft = open('target_freq.txt', 'wb')
fc = open('context_freq.txt', 'wb')

pickle.dump(dict(Counter(co_occurence)), fco)
pickle.dump(dict(Counter(target)), ft)
pickle.dump(dict(Counter(context)), fc)
print('N: ', len(co_occurence))
