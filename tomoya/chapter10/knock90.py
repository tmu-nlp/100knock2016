from gensim.models import word2vec
import os


def main():
    sentences = word2vec.Text8Corpus("./enwiki-corpus2.txt")
    if "knock90.model" in os.listdir("/Users/tomoya/Work/100knock2016/tomoya/chapter10/"):
        model = word2vec.Word2Vec.load("knock90.model")
    else:
        model = word2vec.Word2Vec(sentences, size=200, min_count=20, window=15)
        model.save("knock90.model")
    print("knock86.py")
    print(model['United_States'], end='\n\n')
    print("knock87.py")
    print(sim_2word(model, 'United_States', 'U.S'), end='\n\n')
    print("knock88.py")
    s(model, ['England'])
    print("knock89.py")
    vec = model['Spain'] - model['Madrid'] + model['Athens']
    for sim in model.similar_by_vector(vec):
        print(sim)


def sim_2word(model, w1, w2):
    return model.similarity(w1, w2)


def s(model, posi, nega=[], n=10):
    cnt = 1
    result = model.most_similar(positive=posi, negative=nega, topn=n)
    for r in result:
        print(cnt, ' ', r[0], ' ', r[1])
        cnt += 1
    print()


if __name__ == '__main__':
    main()
