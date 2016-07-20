from knock96 import extract_countries
from scipy.cluster.hierarchy import ward, dendrogram
import matplotlib.pyplot as plt

countries = []
vectors = []
for country, vector in sorted(extract_countries().items()):
    countries.append(country)
    vectors.append(vector)

dendrogram(ward(vectors), labels = countries, orientation = "left")
plt.show()
