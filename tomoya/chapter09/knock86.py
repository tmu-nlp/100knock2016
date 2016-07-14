import pickle

with open('knock85_result.dump', 'rb') as fp:
  word_vector = pickle.load(fp)

print(word_vector['United_States'])
