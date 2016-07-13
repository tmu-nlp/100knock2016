import random

w_file = open('knock82_context.txt', 'w')

context = list()
for line in open('knock81_corpus.txt', 'r'):
    words = line.strip('\n').split()
    for i in range(len(words)):
        d = random.randint(1, 5)
        for j in range(i - d, i + d + 1):
            if j > 0 and j < len(words) and i != j:
                w_file.write('{}\t{}\n'.format(words[i], words[j]))
w_file.close()
