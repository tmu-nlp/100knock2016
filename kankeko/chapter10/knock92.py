from gensim.models import word2vec
import pickle
#from knock84 import word_id


data = word2vec.Text8Corpus('corpus.txt')
model = word2vec.Word2Vec(data)
model.save('word2vec92.model')

knock85_f = open("knock85_result92.txt","w")
knock90_f = open("knock90_result92.txt","w")

def analogy():
    for line in open("knock91.txt"):
        words = line.strip().split()
        for similar_word in model.most_similar(positive=[words[1],words[2]], negative=[words[0]], topn = 1):
            knock90_f.write("{} {} {} {}\n".format(words[0],words[1],words[2],similar_word[0]))
    #with open("vocab_knock85.txt") as f:
        #vocab85 = pickle.load(f)
        #knock85_f.write(vocab85[word_id[1]]-vocab85[word_id[0]]-vocab85[word_id[2]])

analogy()
