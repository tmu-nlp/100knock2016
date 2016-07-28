from gensim.models import word2vec
from knock96 import mk_country
from sklearn.cluster import KMeans

model=word2vec.Word2Vec.load("knock90.model")

d=mk_country(open("../chapter09/country_list.txt","r"))
vec_list=[]
name_list=[]

for key,value in d.items():
    vec_list+=[value]
    name_list+=[key]

kmeans_model=KMeans(n_clusters=5).fit(vec_list)
labels=kmeans_model.labels_

for label,name in zip(labels,name_list):
    print(label,name)
