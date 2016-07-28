from gensim.models import word2vec

data = word2vec.Text8Corpus('corpus.txt')
model = word2vec.Word2Vec(data)
model.save('word2vec90.model')

print("knock86\n")
print(model["United_States"])

print("knock87\n")
print(model.similarity('United_States', 'US'))

print("knock88\n")
for word_pro in model.most_similar(positive=['England'], topn = 10):
        print(word_pro)

print("knock89\n")
for word_pro in model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn = 10):
    print(word_pro)
