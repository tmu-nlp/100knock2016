from knock96 import make_country_vector
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

country_dict = make_country_vector()
country_list = list()
country_vector = list()
for name, vector in sorted(country_dict.items()):
    country_list.append(name)
    country_vector.append(vector)

tsne = TSNE(n_components=2)
result = tsne.fit_transform(country_vector)

hidden, graph = plt.subplots()
graph.scatter(result[:, 0], result[:, 1], s=1)
for i, country in enumerate(country_list):
    graph.annotate(country, xy=(result[i, 0], result[i, 1]), size=7)
plt.show()
