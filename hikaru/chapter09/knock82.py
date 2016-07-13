import random

for line in open('knock81.txt'):
    words = line.split()
    for i, t in enumerate(words):
        d = random.randint(1,5)
        for j in range(d):
            if j != 0 and i - j >= 0:
                print (t + '\t' + words[i-j])
            if j != 0 and i + j < len(words):
                print (t + '\t' + words[i+j])