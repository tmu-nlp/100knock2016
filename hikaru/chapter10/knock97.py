from gensim.models import word2vec
import numpy as np
from sklearn.cluster import KMeans

model = word2vec.Word2Vec.load("knock90_word2vec")
country_list = list()
vector_list = list()
for country in open('country_list.txt'):
    country = country.strip('\n')
    if country in model:
        country_list.append(country)
        vector_list.append(model[country])

features = np.array(vector_list)
kmeans_model = KMeans(n_clusters=5).fit(features)
labels = kmeans_model.labels_
for label, country in zip(labels, country_list):
    print (label, country)
