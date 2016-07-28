from gensim.models import word2vec
import scipy.spatial.distance as dis
import pickle

with open('../chapter09/knock85_result.dump', 'rb') as f:
    word_matrix = pickle.load(f)

w2v_model = word2vec.Word2Vec.load('knock90.model')

w_file1 = open('knock94_vector.txt', 'w')
w_file2 = open('knock94_w2v.txt', 'w')
flag = False
for line in open('combined.tab'):
    if flag is False:
        flag = True
        continue
    line = line.strip('\n')
    word = line.split('\t')
    if word[0] not in word_matrix or word[1] not in word_matrix:
        w_file1.write(line + '\t' + '0\n')
        w_file2.write(line + '\t' + '0\n')
        continue
    
    distance = 1 - dis.cosine(word_matrix[word[0]], word_matrix[word[1]])
    w_file1.write(line + '\t' + str(distance) + '\n')
    w2v = w2v_model.similarity(word[0], word[1])
    w_file2.write(line + '\t' + str(w2v) + '\n')

w_file1.close()
w_file2.close()
