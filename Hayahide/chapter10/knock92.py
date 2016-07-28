from gensim.models import word2vec
import scipy.spatial.distance as dis
import pickle

with open('../chapter09/knock85_result.dump', 'rb') as f:
    word_matrix = pickle.load(f)

w2v_model = word2vec.Word2Vec.load('knock90.model')

w_file1 = open('knock92_vector.txt', 'w')
w_file2 = open('knock92_w2v.txt', 'w')
for line in open('knock91_result.txt'):
    line = line.strip('\n')
    similar_word = ''
    similarity = 0
    word = line.split()
    if word[0] == ':':
        continue
    elif word[0] not in word_matrix or word[1] not in word_matrix or word[2] not in word_matrix:
        w_file1.write(line + '\t' + '<None>' + '\t' + '0\n')
        w_file2.write(line + '\t' + '<None>' + '\t' + '0\n')
        continue
    
    vector4 = word_matrix[word[1]] - word_matrix[word[0]] + word_matrix[word[2]]
    for key, vector in word_matrix.items():
        distance = 1 - dis.cosine(vector4, word_matrix[key])
        if similarity < distance:
            similarity = distance
            similar_word = key
    w_file1.write(line + '\t' + similar_word + '\t' + str(similarity) + '\n')
    w2v = w2v_model.most_similar(positive=[word[1], word[2]], negative=[word[0]])
    w_file2.write(line + '\t' + w2v[0][0] + '\t' + str(w2v[0][1]) + '\n')
w_file1.close()
w_file2.close()
