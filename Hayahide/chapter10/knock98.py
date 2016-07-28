from scipy.cluster.hierarchy import ward, dendrogram
from knock96 import make_country_vector
import matplotlib.pyplot as plt

country_dict = make_country_vector()
country_list = list()
country_vector = list()
for name, vector in sorted(country_dict.items()):
    country_list.append(name)
    country_vector.append(vector)

result = ward(country_vector)

dendrogram(result, labels=country_list, leaf_font_size=5)
plt.show()
