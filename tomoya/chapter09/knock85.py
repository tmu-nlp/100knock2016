from knock84 import getPPMI
from sklearn.feature_extraction import DictVectorizer
import sklearn.decomposition
from scipy.sparse.linalg import svds
import numpy as np
import pickle


def dim_reduction():
  dic2vec = DictVectorizer(sparse=True)
  PPMI = getPPMI()
  tc = list()
  token_list = list()
  for token, contexts in sorted(PPMI.items()):
    token_list.append(token)
    contexts = dict(contexts)
    tc.append(contexts)

  tc_vec = dic2vec.fit_transform(tc)
  tc_svd = svds(tc_vec, 300)
  tc_pca = np.dot(tc_svd[0], np.diag(tc_svd[1]))

  word_vec = dict()
  for token, vec in zip(token_list, tc_pca):
    word_vec[token] = vec

  return word_vec

def main():
  word_vec = dim_reduction()
  with open('knock85_result.dump', 'wb') as fp:
    pickle.dump(word_vec, fp)

  for token, vec in word_vec.items():
    print('{}\t{}'.format(token, vec))

if __name__ == '__main__':
  main()
