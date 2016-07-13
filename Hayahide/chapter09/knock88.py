import pickle
import scipy.spatial.distance as dis

with open('knock85_result.dump', 'rb') as f:
    word_matrix = pickle.load(f)

similarity = dict()
for word, vector in word_matrix.items():
    similarity[word] = dis.cosine(word_matrix['England'], word_matrix[word])

for word, similar in sorted(similarity.items(), key=lambda x:x[1], reverse=True)[:10]:
    print(word + '\t' + str(similar))
