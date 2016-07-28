import numpy as np
from gensim.models import word2vec
from sklearn.manifold import TSNE
from matplotlib import pyplot as plt

model = word2vec.Word2Vec.load("knock90_word2vec")
country_list = list()
vector_list = list()
for country in open('country_list.txt'):
    country = country.strip('\n')
    if country in model:
        country_list.append(country)
        vector_list.append(model[country])

#print (len(country_list))
features = np.array(vector_list)
tsne = TSNE(n_components = 2).fit_transform(features)
#print (len(tsne[:, 0]))


plt.plot(tsne[:, 0], tsne[:, 1], ".")
for i, country in enumerate(country_list):
    plt.text(tsne[i, 0], tsne[i, 1], country, color='black', size=5)
plt.show()
#print (tsne[:, 0])
#print (tsne[:, 1])


