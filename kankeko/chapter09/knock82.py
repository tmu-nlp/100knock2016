import random

for line in open('new_corpus.txt'):
    tokens = line.strip().split()
    precon = ''
    postcon = ''
    for i in range(len(tokens)):
        window = random.randint(1, 5)
        target = tokens[i]
        start = max(0, i - window)
        finish = min(len(tokens), i + window + 1)
        precon = '\t'.join(tokens[start:i])
        postcon = '\t'.join(tokens[i + 1:finish])
        print('{}\t{}\t{}'.format(tokens[i], postcon, precon))
