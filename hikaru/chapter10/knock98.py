import numpy as np
from scipy.cluster.hierarchy import dendrogram, ward
from matplotlib.pyplot import show
from gensim.models import word2vec


model = word2vec.Word2Vec.load("knock90_word2vec")
country_list = list()
vector_list = list()
for country in open('country_list.txt'):
    country = country.strip('\n')
    if country in model:
        country_list.append(country)
        vector_list.append(model[country])
features = np.array(vector_list)
clustring =  ward(features)
dendrogram(clustring, labels = country_list, orientation='left', leaf_font_size=10)
show()
