from gensim.models import word2vec

data = word2vec.Text8Corpus('knock81_corpus.txt')
model = word2vec.Word2Vec(data, size=300)
model.save('knock90.model')

print('knock86.py -Word2Vec Ver.-')
print(model['United_States'])

print('\nknock87.py -Word2Vec Ver.-')
print(model.similarity('United_States', 'US'))

print('\nknock88.py -Word2Vec Ver.-')
for x in model.most_similar(positive=['England']):
    print(x[0], x[1])

print('\nknock89.py -Word2Vec Ver.-')
for x in model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid']):
    print(x[0], x[1])
