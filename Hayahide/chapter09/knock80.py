import re

corpus = list()
w_file = open('knock80_corpus.txt', 'w')
for line in open('enwiki-20150112-400-r100-10576.txt', 'r'):
    tokens = line.strip('\n').split()
    token_list = list()
    for token in tokens:
        token = re.sub('\.|,|!|\?|;|:|\(|\)|\[|\]|\'|\"','',token)
        if len(token) != 0:
            token_list.append(token)
    w_file.write(' '.join(token_list) + '\n')
w_file.close()
