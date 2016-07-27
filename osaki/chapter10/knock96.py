from gensim.models import word2vec

model=word2vec.Word2Vec.load("knock90.model")
d=dict()

for country in open("../chapter09/country_list.txt","r"):
    country=country.strip("\n").replace(" ","_")
    if country in model:
        d[country]=model[country]

print(d)    
