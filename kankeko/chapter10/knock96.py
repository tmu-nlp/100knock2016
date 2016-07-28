from gensim.models import word2vec

data = word2vec.Text8Corpus('corpus.txt')
model = word2vec.Word2Vec(data)
countries_dict = {}
countries = []

with open("countries.txt") as f:
    countries = f.read().split("\n")

for country in countries:
    try:
        value = model[country]
    except:
        pass
    countries_dict[country] = value

