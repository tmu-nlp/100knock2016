from gensim.models import word2vec
from knock92 import WordSim1, WordSim2
import scipy
import sys
import pickle
sys.path.append('/Users/tomoya/Work/100knock2016/tomoya/chapter09/')


def printSim2(infile, outfile, sim):
    with open(outfile, 'w') as f:
        for analogy in open(infile, 'r'):
            words = analogy.strip('\n').split('\t')
            if not set(words[0:2]).issubset(set(sim.vocab)):
                continue
            wsim = sim.calcSim_w2w(words[0], words[1])
            print("{}\t{}".format(analogy.strip('\n'), wsim), file=f)


class WordSim12(WordSim1):
    def __init__(self, model):
        super().__init__(
            model=model,
        )

    def calcSim_w2w(self, word1, word2):
        w1 = self.model[word1]
        w2 = self.model[word2]
        return (1 - scipy.spatial.distance.cosine(w1, w2)) * 10


class WordSim22(WordSim2):
    def __init__(self, model):
        super().__init__(
            model=model,
        )

    def calcSim_w2w(self, word1, word2):
        return self.model.similarity(word1, word2) * 10


def main():
    with open('../chapter09/knock85_result.dump', 'rb') as fp:
        model = pickle.load(fp)
    w1 = WordSim12(model)
    model = word2vec.Word2Vec.load("knock90.model")
    w2 = WordSim22(model)
    printSim2('./wordsim353/combined.tab', 'knock85at94.data', w1)
    printSim2('./wordsim353/combined.tab', 'knock94.data', w2)

if __name__ == '__main__':
    main()
