from gensim.models import word2vec

model = word2vec.Word2Vec.load("knock90_word2vec")
country_list = list()
for country in open('country_list.txt'):
    country = country.strip('\n')
    if country in model:
        country_list.append(country)
        vector_list.append(model[country])
        print (country)
        print (model[country])
