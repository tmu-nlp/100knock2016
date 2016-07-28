from gensim.models import word2vec

model=word2vec.Word2Vec.load("knock90.model")

def mk_country(f):
    d=dict()
    for country in f:
        country=country.strip("\n").replace(" ","_")
        if country in model:
            d[country]=model[country]
    return d

if __name__=="__main__":
    d=mk_country(open("../chapter09/country_list.txt","r"))
    print(d)    
