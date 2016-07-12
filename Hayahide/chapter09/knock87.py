import pickle
import scipy.spatial.distance as dis

with open('knock85_result.dump', 'rb') as f:
    word_matrix = pickle.load(f)

print(dis.cosine(word_matrix['United_States'], word_matrix['US']))
