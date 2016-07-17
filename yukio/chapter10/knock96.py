from gensim.models import word2vec

def extract_countries():
    countries_vec = {}
    vec = word2vec.Word2Vec.load("word2vec")
    for line in open("../chapter09/countries.txt", "r"):
        country = line.strip().replace(" ", "_")
        if country in vec.vocab.keys():
            countries_vec[country] = vec[country]

    return countries_vec

if __name__ == "__main__":
    for country, vector in sorted(extract_countries().items()):
        print(country)
        print(vector)
        print()
