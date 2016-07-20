from knock96 import make_country_vector
from sklearn.cluster import KMeans

country_dict = make_country_vector()
country_vector = list()
country_list = list()
for name, vector in sorted(country_dict.items()):
    country_vector.append(vector)
    country_list.append(name)

kmeans = KMeans(n_clusters = 5)
kmeans.fit(country_vector)

for country, label in zip(country_list, kmeans.labels_):
    print('country: {}\tcluster: {}'.format(country, label))
