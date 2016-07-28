from gensim.models import word2vec
data = word2vec.Text8Corpus("../chapter09/knock81.txt")
model = word2vec.Word2Vec(data, size=300)
model.save('knock90_word2vec')

def knock86():
    return model['United_States']
def knock87():
    return model.similarity('United_States', 'U.S')
def knock88():
    top = model.most_similar(positive=['England'], topn=10)
    for word, value in top:
        print ('{} --> {}'.format(word, value))
def knock89():
    top = model.most_similar(positive=['Spain', 'Madrid'], negative=['Athens'], topn=10)
    for word, value in top:
        print ('{} --> {}'.format(word, value))

if __name__ == '__main__':
    print (knock86())
    print (knock87())
    print ('----')
    knock88()
    print ('----')
    knock89()
