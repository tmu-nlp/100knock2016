from gensim.models import word2vec
import sys
import pickle
sys.path.append('/Users/tomoya/Work/100knock2016/tomoya/chapter09/')
from knock89 import getVectorSim

def printSim(infile, outfile, sim):
    with open(outfile, 'w') as f:
        for analogy in open('knock91.data', 'r'):
            words = analogy.strip('\n').split(' ')
            if not set(words[0:3]).issubset(set(sim.vocab)):
                continue
            vec = sim.model[words[1]] - sim.model[words[0]] + sim.model[words[2]]
            sim_word, wsim = sim.calcSim(vec, words)
            print("{} {} {}".format(analogy.strip('\n'), sim_word, wsim), file=f)


class WordSim1:
    def __init__(self, model):
        self.model = model
        self.vocab = model.keys()

    def calcSim(self, vec, words):
        similarity = getVectorSim(self.model, vec)
        word, sim = sorted(similarity.items(), key=lambda x: x[1], reverse=True)[0]
        return word, sim


class WordSim2:
    def __init__(self, model):
        self.model = model
        self.vocab = model.vocab.keys()

    def calcSim(self, vec, words):
        w = self.model.most_similar(positive=[words[1], words[2]], negative=[words[0]])
        return w[0][0], w[0][1]
def main():
    with open('../chapter09/knock85_result.dump', 'rb') as fp:
        model = pickle.load(fp)
    w1 = WordSim1(model)
    model = word2vec.Word2Vec.load("knock90.model")
    w2 = WordSim2(model)
    printSim('knock91.data', 'knock85.data', w1)
    print('finish:w1')
    printSim('knock91.data', 'knock92.data', w2)
    print('finish:w2')

if __name__ == '__main__':
    main()
