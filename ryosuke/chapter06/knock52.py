from stemming.porter2 import stem

for line in open('knock51.txt'):
    word = line.rstrip('\n')
    print('{}\t{}'.format(word, stem(word)))
