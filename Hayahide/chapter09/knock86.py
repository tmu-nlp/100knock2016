import pickle

with open('knock85_result.dump', 'rb') as f:
    word_matrix = pickle.load(f)

print(word_matrix['United_States'])
