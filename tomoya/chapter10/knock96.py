from gensim.models import word2vec


def getCountrydict():
    country_vector = dict()
    model = word2vec.Word2Vec.load('knock90.model')
    for line in open('country-name.txt', 'r'):
        line_rep = line.strip('\n').replace(' ', '_')
        if line_rep in model.vocab.keys():
            country_vector[line_rep] = model[line_rep]
    return country_vector


def main():
    country_vector = getCountrydict()
    print(country_vector.keys())

if __name__ == '__main__':
    main()
