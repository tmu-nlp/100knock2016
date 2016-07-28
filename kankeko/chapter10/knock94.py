
from gensim.models import word2vec
import scipy.spatial.distance as dis
import pickle
#from knock84 import word_id


#with open('truncated_X.dump', 'rb') as f:
    #X = pickle.load(f)
w2v_model = word2vec.Word2Vec.load('word2vec90.model')

file85 = open("knock85_94.txt", "w")
file90 = open("knock90_94.txt", "w")

for i,line in enumerate(open("combined.tab")):
    if i == 0:
        continue
    words = line.strip().split("\t")
    try:
        w2v = w2v_model.similarity(words[0],words[1])
    except:
        w2v = 0
    #cosine = 1 - dis.cosine(X[word_id[words[0]]],X[word_id[words[1]]])
    file90.write("{}\t{}\t{}\n".format(words[0],words[1], w2v))
    #file_85.write("{}\t{}".format(line, cosine))

