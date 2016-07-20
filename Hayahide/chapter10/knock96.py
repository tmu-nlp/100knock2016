from gensim.models import word2vec


def make_country_vector():
    model = word2vec.Word2Vec.load('knock90.model')
    country_list = list()
    for line in open('../chapter09/country.txt', 'r'):
        line = line.strip('\n')
        country_list.append(line.replace(' ', '_'))

    country_vector = dict()
    for country in country_list:
        if country in model:
            country_vector[country] = model[country]

    return country_vector

if __name__ == '__main__':
    make_country_vector()
