from gensim.models import word2vec
from knock96 import mk_country
import numpy as np
import pandas as pd
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

model=word2vec.Word2Vec.load("knock90.model")

d=mk_country(open("../chapter09/country_list.txt","r"))
vec_list=[]
name_list=[]

for key,value in d.items():
    vec_list+=[value]
    name_list+=[key]

TSNE_model=TSNE(n_components=2)
result=TSNE_model.fit_transform(vec_list)

plt.plot(result[:,0],result[:,1],".")
plt.show()
