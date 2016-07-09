from knock84 import PPMI_matrix
from sklearn.decomposition import PCA
from scipy import sparse
import datetime

def dimension_reduction():
    X, word_id = PPMI_matrix()
    print('PPMI_matrix finished. time: {}'.format(datetime.datetime.today()))

    pca = PCA(n_components = 300)
    X_dense = X.todense()
    print(X_dense)
    pca.fit(X_dense)
    X_pca = pca.transform(X_dense)
    print('PCA finished. time: {}'.format(datetime.datetime.today()))
    
    word_list = list()
    [word_list.append(key) for key, value in sorted(word_id.items(), key=lambda x:x[1])]

    word_matrix = dict()
    for word, vector in zip(word_list, X_pca):
        word_matrix[word] = vector
    return word_matrix

if __name__ == '__main__':
    print('Starting time: {}'.format(datetime.datetime.today()))
    word_matrix = dimension_reduction()
    print('dimension_reduction finished. time: {}'.format(datetime.datetime.today()))
    w_file = open('knock85_result.txt', 'w')
    for word, vector in sorted(word_matrix.items()):
        w_file.write('{}\t{}\n'.format(word, vector))
    w_file.close()
    

